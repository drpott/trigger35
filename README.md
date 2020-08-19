# trigger35 using Python 3.x
network automation using trigger for me

## work done so far:
 - fixed tacacsrc and to use only GPG encryption
 - fixed twister.py
 - fixed gong script (telnet and ssh works now)
 - fixed netdevices
 - fixed commands with commando
 - made netdevices leaner (got rid of Prodonly, ACLs - who uses ACLs nowadays)
 - fixed cli pty

## work to do
 - other shit most likely

## requirements

 - Environment:
   - Linux
   - python 3.x
   - gpg2 (gpg2 --gen-key)
   - gnupg-agent

 - Install Procedure
     dnf install conda emacs
     conda create -n py37 python=3.7
     git clone https://github.com/drpott/trigger35.git
     cd trigger35
     conda activate py37
     pip install twisted crochet IPy pyasn1 SimpleParse pytz cryptography bcrypt
     gpg2 --gen-key (make sure user is 5 chars long and change in settings.py to reflect user/pass)

update /etc/hosts file and py scripts location in bin/*.py, trigger/config/settings.py and trigger/conf/__init__.py


  - for emacs:
    - https://realpython.com/emacs-the-best-python-editor/
    ln -s .conda/envs .virtualenvs
    venv-work on py37
    elpy-config