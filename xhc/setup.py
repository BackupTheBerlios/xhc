#!/usr/bin/env python
"""Setup wrapper for creating Windows executable."""

#-----------------------------------------------------------------------------
# Name:        setup.py                                                       
# Purpose:     Setup wrapper for creating Windows executable                  
#                                                                             
# Author:      Alexander Skwar <ASkwar@email-server.info>                     
#                                                                             
# Created:     2003/12/03                                                     
# RCS-ID:      $Id: setup.py,v 1.3 2003/03/15 09:49:13 askwar Exp $                                                
# Copyright:   (c) 2003                                                       
# Licence:     GPL                                                            
#-----------------------------------------------------------------------------

from distutils.core import setup
import glob
import py2exe
import os
from __version__ import *

def main():
    
    # Let py2exe build the executable
    setup(
    	name		= name,
    	version		= version, 
    	scripts		= scripts, 
    	description	= description, 
    	author		= author, 
    	author_email= author_email, 
    	data_files	= data_files
    )
    
if __name__ == '__main__':
    if not os.name in ('nt', 'dos'):
        print "Error: setup.py can only be run in Windows or DOS!\n"
        sys.exit(1)

    main()

