#!/usr/bin/env python
#Boa:App:BoaApp

from wxPython.wx import *

import fHaupt

modules ={'MakeDist': [0, 'Script for distributing the program', 'MakeDist.py'],
 '__version__': [0, 'Version Information', '__version__.py'],
 'fHaupt': [1, 'Hauptfenster des Programmes', 'fHaupt.py'],
 'messages': [0, 'Generic message catalog for gettext', 'messages.pot'],
 'setup': [0, 'Setup information', 'setup.py']}

class BoaApp(wxApp):
    def OnInit(self):
        wxInitAllImageHandlers()
        self.main = fHaupt.create(None)
        #workaround for running in wxProcess
        self.main.Show();self.main.Hide();self.main.Show()
        self.SetTopWindow(self.main)
        return true

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
