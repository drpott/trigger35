# trigger35 using Python 3.x
network automation using trigger and python 3.x for me

## Technologies and requirements
Project is created with:
* Linux
* emacs IDE
* python 3.x (any version > 3 should work)
* gpg2 (for tacacsrc module using gpg encryption)
* gnupg-agent

## Setup
To run this project:
```
   $ dnf install conda emacs
   $ conda create -n py37 python=3.7
   $ ln -s .conda/envs .virtualenvs (this more for emacs venv)
   $ git clone https://github.com/drpott/trigger35.git
   $ cd trigger35
   $ conda activate py37
   $ pip install twisted crochet IPy pyasn1 SimpleParse pytz cryptography bcrypt
   $ gpg2 --gen-key (make sure user is 5 chars long and change in settings.py to reflect user/pass)
```

## Configuration
Following must be done to run this thing:
     * update hosts file if you need
     * change path trigger location in following py scripts: (work in progress, until better method)
     ```
        trigger/bin/*.py,
        trigger/config/settings.py and
        trigger/conf/__init__.py
     ```

## IDE
Take emacs init.el from my environ dir, based on:
* https://realpython.com/emacs-the-best-python-editor/
* whilst in emacs:
```
    M-x venv-work on py37
    M-x elpy-config
```