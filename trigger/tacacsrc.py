# -*- coding: utf-8 -*-

"""Abstract interface to .tacacsrc credentials file.

Designed to interoperate with the legacy DeviceV2 implementation, but
provide a reasonable API on top of that.  The name and format of the
.tacacsrc file are not ideal, but compatibility matters.
"""

from collections import namedtuple
from distutils.version import LooseVersion
from time import strftime, localtime
import pwd, sys, subprocess, os, getpass
from twisted.python import log
from trigger.conf import settings
import shlex
# Exports
__all__ = ('get_device_password', 'prompt_credentials',
           'update_credentials', 'validate_credentials',
           'Credentials', 'Tacacsrc')

# Credential object stored in Tacacsrc.creds
Credentials = namedtuple('Credentials', 'username password realm')

# Exceptions
class TacacsrcError(Exception): pass
class CouldNotParse(TacacsrcError): pass
class MissingPassword(TacacsrcError): pass
class MissingRealmName(TacacsrcError): pass
class VersionMismatch(TacacsrcError): pass


# Functions
def get_device_password(device=None, tcrc=None):
    """
    Fetch the password for a device/realm or create a new entry for it.
    If device is not passed, ``settings.DEFAULT_REALM`` is used, which is default
    realm for most devices.

    :param device:
        Realm or device name to updated

    :param device:
        Optional `~trigger.tacacsrc.Tacacsrc` instance
    """
    
    if tcrc is None:
        tcrc = Tacacsrc()

    # If device isn't passed, assume we are initializing the .tacacsrc.
    try:
        creds = tcrc.creds[device]
    except KeyError:
        print('\nCredentials not found for device/realm %r, prompting...' % device)
        creds = prompt_credentials(device)
        tcrc.creds[device] = creds
        tcrc.write()

    return creds


def prompt_credentials(device, user=None):
    """
    Prompt for username, password and return them as Credentials namedtuple.

    :param device: Device or realm name to store
    :param user: (Optional) If set, use as default username
    """
    
    if not device:
        raise MissingRealmName('You must specify a device/realm name.')

    creds = ()
    print('\nUpdating credentials for device/realm %r' % device)

    user_default = ''
    if user:
        user_default = ' [%s]' % user
    
    username = getpass._raw_input('Username%s: ' % user_default) or user
    if username == '':
        print('\nYou must specify a username, try again!')
        return prompt_credentials(device, user=user)

    passwd = getpass.getpass('Password: ')
    if not passwd:
        print('\nPassword cannot be blank, try again!')
        return prompt_credentials(device, user=username)

    creds = Credentials(username, passwd, device)

    return creds

def update_credentials(device, username=None):
    """
    Update the credentials for a given device/realm. Assumes the same username
    that is already cached unless it is passed.

    This may seem redundant at first compared to Tacacsrc.update_creds() but we
    need this factored out so that we don't end up with a race condition when
    credentials are messed up.

    Returns True if it actually updated something or None if it didn't.

    :param device: Device or realm name to update
    :param username: Username for credentials
    """

    tcrc = Tacacsrc()
    if tcrc.creds_updated:
        return None

    mycreds = tcrc.creds.get(device, tcrc.creds[settings.DEFAULT_REALM])
    if username is None:
        username = mycreds.username

    tcrc.update_creds(tcrc.creds, mycreds.realm, username)
    tcrc.write()

    return True


def validate_credentials(creds=None):
    """
    Given a set of credentials, try to return a `~trigger.tacacsrc.Credentials`
    object.

    If ``creds`` is unset it will fetch from ``.tacacsrc``.

    Expects either a 2-tuple of (username, password) or a 3-tuple of (username,
    password, realm). If only (username, password) are provided, realm will be populated from
    :setting:`DEFAULT_REALM`.

    :param creds:
        A tuple of credentials.

    """

    realm = settings.DEFAULT_REALM

    # If it isn't set or it's a string, or less than 1 or more than 3 items,
    # get from .tacacsrc
    if (not creds) or (type(creds) == str) or (len(creds) not in (2, 3)):
        log.msg('Creds not valid, fetching from .tacacsrc...')
        tcrc = Tacacsrc()
        return tcrc.creds.get(realm, get_device_password(realm, tcrc))

    # If it's a dict, get the values
    if hasattr(creds, 'values'):
        log.msg('Creds is a dict, converting to values...')
        creds = list(creds.values())

    # If it's missing realm, add it.
    if len(creds) == 2:
        log.msg('Creds is a 2-tuple, making into namedtuple...')
        username, password = creds
        return Credentials(username, password, realm)

    # Or just make it go...
    elif len(creds) == 3:
        log.msg('Creds is a 3-tuple, making into namedtuple...')
        return Credentials(*creds)

    raise RuntimeError('THIS SHOULD NOT HAVE HAPPENED!!')


def _gpg_pipe(file_name, gpguser, gpgkey, data=None):
    """
    Pipe things through gpg.
    
    For safety, we give the passphrase to gpg via a file descriptor.
    The argument list is modified to include the relevant options for that.
    The data is fed to gpg via a temporary file, readable only by
    the owner, to avoid congested pipes.
    """

    if data != None: #encrypt_here
        cmd = 'gpg2 --batch --yes --quiet -e -r '+gpguser+' -o '
        cmd += file_name
        p = subprocess.Popen(shlex.split(cmd), stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             close_fds=False)
        out, err = p.communicate(bytes('\n'.join(data), 'utf-8'))
    else: # decrypt_here
        cmd = 'gpg2 --pinentry-mode=loopback --batch --passphrase-fd --yes --quiet -r '
        cmd += gpguser+' -d '+file_name
        # print(cmd)
        passphraseecho = subprocess.Popen(['echo', gpgkey],
                                          stdout=subprocess.PIPE,
                                          stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        p = subprocess.Popen(shlex.split(cmd), stdin=passphraseecho.stdout,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()

    if not p.returncode == 0:
        raise RuntimeError("Error %s" % (err))
    
    return out

# Classes
class Tacacsrc(object):
    """
    Encrypts, decrypts and returns credentials for use by network devices and
    other tools.

    Pass use_gpg=True to force GPG, otherwise it relies on
    settings.USE_GPG_AUTH

    `*_old` functions should be removed after everyone is moved to the new
    system.
    """

    def __init__(self, tacacsrc_file='.tacacsrc.gpg', generate_new=False):
        """
        Open .tacacsrc (tacacsrc_file or $TACACSRC or ~/.tacacsrc), or create
        a new file if one cannot be found on disk.

        """

        self.file_name = tacacsrc_file
        self.generate_new = generate_new
        self.userinfo = pwd.getpwuid(os.getuid())
        self.gpguser = settings.TACACSRC_GPG_USER
        self.gpgkey = settings.TACACSRC_PASSPHRASE
        self.username = self.userinfo.pw_name
        self.user_home = self.userinfo.pw_dir
        self.data = []
        self.creds = {}
        self.creds_updated = False
        self.version = LooseVersion('2.0')
        self.file_abs_path = os.path.join(self.user_home, self.file_name)
        log.msg("Got username: %r" % self.username, debug=True)

        # Check if the file exists
        if not os.path.exists(self.file_abs_path):
            print('%s not found, generating a new one!' % os.path.join(self.user_home, self.file_name))
            self.generate_new = True

        if not self.generate_new:
            self.rawdata = self._decrypt_and_read()
            self.creds = self._parse()
        else:
            self.creds[settings.DEFAULT_REALM] = prompt_credentials(device='tacacsrc')
            self.write()


    def update_creds(self, creds, realm, user=None):
        """
        Update username/password for a realm/device and set self.creds_updated
        bit to trigger .write().

        :param creds: Dictionary of credentials keyed by realm
        :param realm: The realm to update within the creds dict
        :param user: (Optional) Username passed to prompt_credentials()
        """

        creds[realm] = prompt_credentials(realm, user)
        log.msg('setting self.creds_updated flag', debug=True)
        self.creds_updated = True
        new_user = creds[realm].username
        print('\nCredentials updated for user: %r, device/realm: %r.' % \
              (new_user, realm))

        
    def _encrypt_and_write(self):
        '''Encrypt data with symmetric encryption.'''
        
        _gpg_pipe(self.file_abs_path, self.gpguser, self.gpgkey, self.rawdata)

        
    def _decrypt_and_read(self):
        '''Decrypt encrypted data with symmetric encryption.'''

        return _gpg_pipe(self.file_abs_path, self.gpguser, self.gpgkey)

        
    def write(self):
        """Replace self.rawdata with current password details."""

        out = ['# Saved by %s at %s\n\n' % \
            (self.__module__, strftime('%Y-%m-%d %H:%M:%S %Z', localtime()))]

        for realm, (uname, pwd, _) in self.creds.items():
            out.append('%s_uname_ = %s' % (realm, uname))
            out.append('%s_pwd_ = %s' % (realm, pwd))

        self.rawdata = out
        self._encrypt_and_write()
        self._update_perms()


    def _update_perms(self):
        """Enforce -rw------- on the creds file"""

        os.chmod(self.file_abs_path, 0o600)

    
    def _parse(self):
        """Parses .tacacsrc.gpg and returns dictionary of credentials."""

        data = {}
        creds = {}

        for line in self.rawdata.decode('utf-8').splitlines():
            if line.find('#') != -1:
                line = line[:line.find('#')]
            line = line.strip()
            if len(line):
                k, v = line.split(' = ')
                if k == 'version':
                    if v != self.version:
                        raise VersionMismatch('Bad .tacacsrc version (%s)' % v)
                else:
                    realm, s, junk = k.split('_')
                    #assert(junk == '')
                    assert((realm, s) not in data)
                    data[(realm, s)] = v#self._decrypt(v)

        for (realm, k), v in data.items():
            if k == 'uname':
                #creds[realm] = (v, data[(realm, 'pwd')])
                #creds[realm] = Credentials(v, data[(realm, 'pwd')])
                creds[realm] = Credentials(v, data[(realm, 'pwd')], realm)
            elif k == 'pwd':
                pass
            else:
                raise CouldNotParse('Unknown .tacacsrc entry (%s_%s)' % (realm, v))

        return creds

    def user_has_gpg(self):
        """Checks if user has .gnupg directory and .tacacsrc.gpg file."""
        
        gpg_dir = os.path.join(self.user_home, '.gnupg')
        tacacsrc_gpg = os.path.join(self.user_home, '.tacacsrc.gpg')

        # If not generating new .tacacsrc.gpg, we want both to be True
        if os.path.isdir(gpg_dir) and os.path.isfile(tacacsrc_gpg):
            return True

        return False
