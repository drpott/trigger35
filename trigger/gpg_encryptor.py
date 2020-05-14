import os, subprocess
  

def _gpg_pipe(args, data=None):
    '''Pipe things through gpg.

    With the right args, this can be either an encryption or a decryption
    operation.

    For safety, we give the passphrase to gpg via a file descriptor.
    The argument list is modified to include the relevant options for that.

    The data is fed to gpg via a temporary file, readable only by
    the owner, to avoid congested pipes.

    '''
    
    # Actually run gpg.
    cmd = ['gpg2', '--passphrase', 'abc123', '--yes', '--quiet', '-r', 'daniel'] + args
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    if data == None:
        out, err = p.communicate()
    else:
        out, err = p.communicate(bytes(data, 'utf-8'))

    # Return output data, or deal with errors.
    if p.returncode: # pragma: no cover
        raise obnamlib.Error(err)

    return out

def encrypt_symmetric(cleartext):
    '''Encrypt data with symmetric encryption.'''
    return _gpg_pipe(['-r', 'daniel', '-e', '-o', 'test_file'], cleartext)

def decrypt_symmetric():
    '''Decrypt encrypted data with symmetric encryption.'''
    return _gpg_pipe(['-d', 'test_file'])
