import glob

# Version of the application
version     = "1.11"
# Name of the application
name		= 'X-Host Chooser'
# Description of the program
description	= 'Launch pad for XWin.exe from Cygwin'
# Additional data files - used by py2exe
data_files	= [('.', ((glob.glob('*.gif') + glob.glob('*.ico')) + glob.glob('*.jpg') + glob.glob('*.xpm') + glob.glob('*.xpm'))),
                   ('locale/de/LC_MESSAGES', glob.glob('locale/de/LC_MESSAGES/*.po'))]

# Author of the program
author		= 'Alexander Skwar'
# Author's email
author_email	= 'ASkwar@email-server.info'

# Scripts of the program - used by py2exe
scripts		= ['xhc.py']
