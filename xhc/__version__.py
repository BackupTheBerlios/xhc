import glob
import os.path

def uniques(list): # requires that elements of list be hashable!
    d = {}
    for x in list: d[x] = None
    return d.keys()

# Version of the application
version     = "1.11"
# Name of the application
name		= 'X-Host Chooser'
# Short name of the application
short_name  = 'xhc'
# Description of the program
description	= 'Launch pad for XWin.exe from Cygwin'
# Additional data files - used by py2exe
data_files	= [('.', ((glob.glob('*.gif') + glob.glob('*.ico')) + glob.glob('*.jpg') + glob.glob('*.xpm') + glob.glob('*.xpm'))),
                   ('locale/de/LC_MESSAGES', glob.glob('locale/de/LC_MESSAGES/*.po'))]

# Author of the program
author		= 'Alexander Skwar'
# Author's email
author_email= 'ASkwar@email-server.info'

# Scripts of the program - used by py2exe
scripts		= ['xhc.py']

# Files which should be in the source distribution
files = glob.glob('*.py') + glob.glob('setup.*') + glob.glob('*.lnk') +         \
        glob.glob('*.ico') + glob.glob('*.jpg') + glob.glob('*.xpm') +          \
        glob.glob('*.png') +                                                    \
        glob.glob(os.path.join('locale', '*', 'LC_MESSAGES', '*.po'))

files = uniques(files)

# Should the source distribution files be uploaded?
# If this is not None, then they'll be uploaded
# upload = None
upload = {
    'host': 'ftp.berlios.de',
    'user': None, # ie. anonymous
    'pass': None, # ie. default password
    'acct': None, # ie. anonymous
    'dir': '/incoming',
    'pasv': True
}
