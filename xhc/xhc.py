#!/usr/bin/env python
#Boa:App:BoaApp

from wxPython.wx import *

import fHaupt

modules ={'fHaupt': [1, 'Hauptfenster des Programmes', 'fHaupt.py']}

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
