#!/usr/bin/env python
"""Setup wrapper for creating Windows executable."""

#-----------------------------------------------------------------------------
# Name:        setup.py                                                       
# Purpose:     Setup wrapper for creating Windows executable                  
#                                                                             
# Author:      Alexander Skwar <ASkwar@email-server.info>                     
#                                                                             
# Created:     2003/12/03                                                     
# RCS-ID:      $Id: setup.py,v 1.3 2003/07/08 20:53:20 askwar Exp $           
# Copyright:   (c) 2003                                                       
# Licence:     GPL                                                            
#-----------------------------------------------------------------------------

from distutils.core import setup
from glob import glob
import py2exe
import os
import os.path
opj = os.path.join
from __version__ import *
from shutil import copyfile

def main():
    
    old_cwd = os.getcwd()
    try:
        # setup() requires that setup.cfg is in the same directory as setup()
        # is in, when it's called.
        # IOW: We're changing directories to .., so we need to copy setup.cfg
        # to this directory as well, and also remove it, when we're done
        copyfile('setup.cfg', opj('..', 'setup.cfg'))
        
        os.chdir('..')
        
        new_data_files = []
        for data_file in data_files:
            file_entries = []
            for file in data_file[1]:
                file_entries += glob(file)
            new_data_files += ((data_file[0], file_entries), )
    
        # Let py2exe build the executable
        setup(
        	name		= name,
        	version		= version, 
        	scripts		= scripts, 
        	description	= description, 
        	author		= author, 
        	author_email	= author_email, 
        	data_files	= new_data_files,
        )
        
        os.remove('setup.cfg')

    finally:
        os.chdir(old_cwd)
        
if __name__ == '__main__':
    if not os.name in ('nt', 'dos'):
        print "Error: setup.py can only be run in Windows or DOS!\n"
        sys.exit(1)

    main()

