import os,sys

if sys.platform in ('win32', 'win64'):
    os.system('python -m pip install python-telegram-bot')
    os.system('python -m pip install python-twitter')
elif sys.platform == 'linux':
    os.system('python3 -m pip install python-telegram-bot')
    os.system('python3 -m pip install python-twitter')
else:
    os.system('python -m pip install python-telegram-bot')
    os.system('python -m pip install python-twitter')
