#!/usr/bin/env python
"""Small wrapper script to create Windows executable and SFX"""

#Boa:PyApp:main

#-----------------------------------------------------------------------------
# Name:        MakeDist.py                                                     
# Purpose:     Small wrapper script to create Windows executable and SFX      
#              archive for distribution                                       
#                                                                             
# Author:      Alexander Skwar <ASkwar@email-server.info>                     
#                                                                             
# Created:     2003/12/03                                                     
# RCS-ID:      $Id: MakeDist.py,v 1.3 2003/03/15 09:49:13 askwar Exp $                                              
# Copyright:   (c) 2003                                                       
# Licence:     GPL                                                            
#-----------------------------------------------------------------------------

# Define path and options for rk archiver
rk = {
    # Complete path to the folder containing the rk archiver
    'path':         r'C:\Tools\rk',
    # Name of the rk archiver executable in 'path'
    'executable':   'rk.exe',
    # Parameters used for calling rk.exe
    'params':       r'-r -mx -SFX -S%(path)s\win32.sfx'
}

# ------------------> Nothing user-configurable below here! <------------------ 
#-------------------------------------------------------------------------------

modules ={'setup': [0,
           'setup module for creating the Windows executable with py2exe',
           'setup.py']}

import setup
import os
import sys
from __version__ import *

# Insert path into params, so that the SFX stub can be found
rk['params'] = rk['params'] % rk

def main():
    """Create Windows executable and SFX with rk."""

    # Read the setup.cfg file and replace the version for
    # version-productversion and version-fileversion by the version imported
    # from setup.
    version_strings = [
        'version-productversion',
        'version-fileversion'
    ]

    description_strings = [
    	'version-filedescription'
    ]
    
    setupcfg = file('setup.cfg')
    lines = setupcfg.readlines()
    setupcfg.close()
    
    new_lines = []
    vstr_gefunden = 0
    for line in lines:
        vstr_gefunden = 0
        for vstr in version_strings:
            if vstr == line[:len(vstr)]:
                new_lines.append("%s = %s\n" % (vstr, version))
                vstr_gefunden = 1
	
	desc_gefunden = 0
	for desc in description_strings:
	    if desc == line[:len(desc)]:
                new_lines.append("%s = %s\n" % (desc, description))
                desc_gefunden = 1
	
	if not desc_gefunden and not vstr_gefunden:
	    new_lines.append(line)
	
    # version has been replaced in setup.cfg
    # Write it back
    setupcfg = file('setup.cfg', 'w')
    setupcfg.writelines(new_lines)
    setupcfg.close()
    
    # All of the following should work below the directory where this script
    # is located.
    old_cwd = os.getcwd()
    try:
        script_dir = os.path.dirname(sys.argv[0])
        if script_dir.strip() != '':
            os.chdir(script_dir)
        
        # Create Windows executable
        cmd = "%s setup.py py2exe" % (sys.executable)
        print "Running: " + cmd + "\n"
        os.system(cmd)
        
        # This should have created a subdirectory with the name of the 
        # first script under the "dist" directory.
        # Change to this directory before calling rk
        os.chdir(os.path.join('dist', os.path.splitext(scripts[0])[0]))
        
        # Call rk
        cmd = '%s %s "..\%s-%s.exe" *' % (os.path.join(rk['path'], rk['executable']), rk['params'], name.replace(' ', "_"), version)
        print "Running: " + cmd + "\n"
        os.system(cmd)
        
    finally:
        # Change back to the old working directory
        os.chdir(old_cwd)
        
if __name__ == '__main__':
    if not os.name in ('nt', 'dos'):
        print "Error: MakeDist can only be run in Windows or DOS!\n"
        sys.exit(1)
        
    main()


