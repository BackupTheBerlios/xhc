#!/usr/bin/env python
#Boa:App:BoaApp

from wxPython.wx import *
##import XHCFrames
from XHCFrames import *

modules ={'MakeDist': [0, 'Script for distributing the program', 'Utils/MakeDist.py'],
 '__init__': [0, '', 'XHCFrames/__init__.py'],
 '__version__': [0, 'Version Information', 'Utils/__version__.py'],
 'fHaupt': [1, 'Hauptfenster des Programmes', 'XHCFrames/fHaupt.py'],
 'messages': [0, 'Generic message catalog for gettext', 'messages.pot'],
 'setup': [0, 'Setup information', 'Utils/setup.py']}

class BoaApp(wxApp):
    def OnInit(self):
        wxInitAllImageHandlers()
        self.main = fHaupt.create(None)
##        self.main = XHCFrames.fHaupt.create(None)
        #workaround for running in wxProcess
        self.main.Show();self.main.Hide();self.main.Show()
        self.SetTopWindow(self.main)
        return true

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
