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

 - Python 3.x modules:
   - gtextfsm (manual installation, broken via pip install)
   - twisted 20.3
   - crochet
   - IPy
   - pyasn1
   - SimpleParse
   - zope.interface

original project:
https://github.com/trigger/trigger

Thanks to the author, it's a great tool