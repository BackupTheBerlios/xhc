#-----------------------------------------------------------------------------
# Name:        __version__.py                                                 
# Purpose:     Version information for the application                        
#                                                                             
# Author:      Alexander Skwar <ASkwar@email-server.info>                     
#                                                                             
# Created:     2003/17/03                                                     
# RCS-ID:      $Id: __version__.py,v 1.2 2003/03/17 12:56:25 askwar Exp $                                          
# Copyright:   (c) 2003                                                       
# Licence:     GPL                                                            
#-----------------------------------------------------------------------------

import os.path
opj = os.path.join

# Version of the application
version     = "1.15"
# Name of the application
name		= 'X-Host Chooser'
# Short name of the application
short_name  = 'xhc'
# Description of the program
description	= 'Launch pad for XWin.exe from Cygwin'
# Additional data files - used by py2exe
# Files are supposed to be in a directory one level up of the directory
# containing this script.
data_files  = [('Images', [opj('Images', '*.gif'), opj('Images', '*.ico'), opj('Images', '*.jpg'), opj('Images', '*.xpm')]),
                (opj('locale', 'de', 'LC_MESSAGES'), [opj('locale', 'de', 'LC_MESSAGES', '*.mo')])]

# Author of the program
author		= 'Alexander Skwar'
# Author's email
author_email= 'ASkwar@email-server.info'

# Scripts of the program - used by py2exe
scripts		= ['xhc.py']

# Files which should be in the source distribution
# Files are supposed to be in a directory one level up of the directory
# containing this script.
files = ['*.py', '*.lnk', '*.pyw',
        opj('XHCFrames', '*.py'),
        opj('Utils', '*.py'), opj('Utils', 'setup*'),
        opj('Utils', 'Tools-i18n', '*.py'),
        opj('Images', '*.ico'), opj('Images', '*.jpg'), opj('Images', '*.xpm'),
        opj('Images', '*.png'),
        opj('locale', '*', 'LC_MESSAGES', '*.po')]


# Should the source distribution files be uploaded?
# If this is not None, then they'll be uploaded
upload = {
    'host': 'ftp.berlios.de',
    'user': None, # ie. anonymous
    'pass': None, # ie. default password
    'acct': None, # ie. anonymous
    'dir': '/incoming',
    'pasv': True
}
upload = None

