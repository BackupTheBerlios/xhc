#!/usr/bin/env python
#Boa:App:BoaApp

#------------------------------------------------------------------------------
# Name:        xhc.py                                                          
# Purpose:     Launch pad for starting XWin.exe from Cygwin/XFree86 comfortably
#                                                                              
# Author:      Alexander Skwar <ASkwar@email-server.info>                      
#                                                                              
# Created:     2003/17/03                                                      
# RCS-ID:      $Id: xhc.py,v 1.6 2003/03/17 12:56:25 askwar Exp $                                                   
# Copyright:   (c) 2003                                                        
# Licence:     GPL                                                             
#------------------------------------------------------------------------------

from wxPython.wx import *
from XHCFrames import *

modules ={'MakeDist': [0, 'Script for distributing the program', 'Utils/MakeDist.py'],
 '__init__': [0,
              'Initialization code for the XHCFrames package',
              'XHCFrames/__init__.py'],
 '__version__': [0, 'Version Information', 'Utils/__version__.py'],
 'fHaupt': [1, 'Hauptfenster des Programmes', 'XHCFrames/fHaupt.py'],
 'messages': [0, 'Generic message catalog for gettext', 'messages.pot'],
 'setup': [0, 'Setup information', 'Utils/setup.py']}

class BoaApp(wxApp):
    """Application class created by Boa."""
    
    def OnInit(self):
        """Handler called when the application initializes."""
        
        wxInitAllImageHandlers()
        self.main = fHaupt.create(None)
        #workaround for running in wxProcess
        self.main.Show();self.main.Hide();self.main.Show()
        self.SetTopWindow(self.main)
        return true

def main():
    """Method run when the script is started."""
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()

