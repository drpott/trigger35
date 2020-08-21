# trigger35 using Python 3.x
* network automation based on trigger
* converted trigger to run on python 3.x
* deleted some functions from original project (don't use ACLs, change mgmt etc..)

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
   $ pip install twisted crochet IPy pyasn1 SimpleParse pytz cryptography bcrypt textfsm
   $ gpg2 --gen-key (make sure user is 5 chars long and change in settings.py to reflect user/pass)
```

## Setup environment
Following must be done to run this thing in your environment:
* create following directories in your conda env:
     ```
     cd $CONDA_PREFIX
     mkdir -p ./etc/conda/activate.d
     mkdir -p ./etc/conda/deactivate.d
     touch ./etc/conda/activate.d/env_vars.sh
     touch ./etc/conda/deactivate.d/env_vars.sh
     ```
     
* edit files (set/unset env variables) in your conda env, eg:
      ```
      vi ./etc/conda/activate.d/env_vars.sh

      set TRIGGER_SETTINGS='<path to>/trigger35/configs/settings.py'
      set TRIGGER_PREFIX='<path to>python35/trigger35/configs'
      set TRIGGER_PATH='<path to>/trigger35'

      vi ./etc/conda/deactivate.d/env_vars.sh

      unset TRIGGER_SETTINGS
      unset TRIGGER_PREFIX
      unset TRIGGER_PATH
     ```

* update system ```/etc/hosts``` file if you need

* in your bin/*.py file you must add the path to trigger35, first liner:
     ```
     import sys
     sys.path.append(r'<path to>/python35/trigger35') or
     sys.path.append(os.getenv(TRIGGER_PATH)) #untested
     ````

## IDE
Take emacs init.el from my environ dir, based on:
* https://realpython.com/emacs-the-best-python-editor/
* whilst in emacs:
```
    M-x venv-work on py37
    M-x elpy-config
```