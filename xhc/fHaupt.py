#Boa:Frame:wxfHaupt

from wxPython.wx import *
from wxPython.lib.anchors import LayoutAnchors
import gettext
import time
import string
import os
import socket

# _ will be set by wxfHaupt.__init__()

def create(parent):
    return wxfHaupt(parent)

[wxID_WXFHAUPT, wxID_WXFHAUPTBTNBROWSEXWINBINARY, wxID_WXFHAUPTBTNENDE, 
 wxID_WXFHAUPTBTNRUN, wxID_WXFHAUPTBTNSAVECONFIG, 
 wxID_WXFHAUPTBTNSUCHEXWINBINARY, wxID_WXFHAUPTCHBAUFLOESUNG, 
 wxID_WXFHAUPTCHBEIGENEIP, wxID_WXFHAUPTCHBEMULATE3BUTTONS, 
 wxID_WXFHAUPTCHBFONT, wxID_WXFHAUPTCHBNOUNIXKILL, wxID_WXFHAUPTCHBNOWINKILL, 
 wxID_WXFHAUPTCHBONCE, wxID_WXFHAUPTCHBROOTLESS, wxID_WXFHAUPTCHLANGUAGE, 
 wxID_WXFHAUPTCOBAUFLOESUNG, wxID_WXFHAUPTCOBXWINBINARY, 
 wxID_WXFHAUPTCOBZIELHOST, wxID_WXFHAUPTNBHAUPT, wxID_WXFHAUPTRBBROADCAST, 
 wxID_WXFHAUPTRBZIELHOST, wxID_WXFHAUPTSTATICLINE1, wxID_WXFHAUPTSTBEFEHL, 
 wxID_WXFHAUPTSTEMULATE3BUTTONSTIMEOUT, wxID_WXFHAUPTSTLANGUAGE, 
 wxID_WXFHAUPTSTXWINBINARY, wxID_WXFHAUPTTCBEFEHL, wxID_WXFHAUPTTCEIGENEIP, 
 wxID_WXFHAUPTTCEMULATE3BUTTONSTIMEOUT, wxID_WXFHAUPTWINSETUP, 
 wxID_WXFHAUPTWINSTART, 
] = map(lambda _init_ctrls: wxNewId(), range(31))

class wxfHaupt(wxFrame):
    def _init_coll_nbHaupt_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(bSelect=true, imageId=-1, pPage=self.winStart,
              strText='Start')
        parent.AddPage(bSelect=false, imageId=-1, pPage=self.winSetup,
              strText='Setup')

    def _init_utils(self):
        # generated method, don't edit
        pass

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxFrame.__init__(self, id=wxID_WXFHAUPT, name='wxfHaupt', parent=prnt,
              pos=wxPoint(829, 496), size=wxSize(376, 262),
              style=wxMINIMIZE_BOX | wxCAPTION | wxSYSTEM_MENU,
              title='X Host Chooser')
        self._init_utils()
        self.SetClientSize(wxSize(368, 228))
        self.Enable(true)
        self.Center(wxBOTH)
        EVT_ACTIVATE(self, self.OnWxfhauptActivate)
        EVT_CLOSE(self, self.OnWxfhauptClose)

        self.nbHaupt = wxNotebook(id=wxID_WXFHAUPTNBHAUPT, name='nbHaupt',
              parent=self, pos=wxPoint(0, 0), size=wxSize(368, 228),
              style=wxMAXIMIZE_BOX)
        self.nbHaupt.SetConstraints(LayoutAnchors(self.nbHaupt, true, true,
              true, true))
        self.nbHaupt.SetAutoLayout(true)
        EVT_NOTEBOOK_PAGE_CHANGING(self.nbHaupt, wxID_WXFHAUPTNBHAUPT,
              self.OnNbhauptNotebookPageChanging)
        EVT_PAINT(self.nbHaupt, self.OnTranslatableControlPaint)

        self.winStart = wxWindow(id=wxID_WXFHAUPTWINSTART, name='winStart',
              parent=self.nbHaupt, pos=wxPoint(0, 0), size=wxSize(360, 202),
              style=wxTAB_TRAVERSAL)

        self.winSetup = wxWindow(id=wxID_WXFHAUPTWINSETUP, name='winSetup',
              parent=self.nbHaupt, pos=wxPoint(0, 0), size=wxSize(360, 202),
              style=wxTAB_TRAVERSAL)

        self.cobZielhost = wxComboBox(choices=['tc34', 'r48', 'r73', 's07nfs',
              's08nfs', 'localhost'], id=wxID_WXFHAUPTCOBZIELHOST,
              name='cobZielhost', parent=self.winStart, pos=wxPoint(136, 24),
              size=wxSize(168, 21), style=wxTAB_TRAVERSAL,
              validator=wxDefaultValidator, value='tc34')
        self.cobZielhost.SetLabel('tc34')
        EVT_KILL_FOCUS(self.cobZielhost, self.OnCobzielhostKillFocus)

        self.btnRun = wxButton(id=wxID_WXFHAUPTBTNRUN, label='Verbinden',
              name='btnRun', parent=self.winStart, pos=wxPoint(16, 160),
              size=wxSize(75, 23), style=0)
        self.btnRun.SetHelpText('IP/Name des Zielrechners eingeben')
        EVT_BUTTON(self.btnRun, wxID_WXFHAUPTBTNRUN, self.OnBtnrunButton)
        EVT_PAINT(self.btnRun, self.OnTranslatableControlPaint)

        self.btnEnde = wxButton(id=wxID_WXFHAUPTBTNENDE, label='Beenden',
              name='btnEnde', parent=self.winStart, pos=wxPoint(264, 160),
              size=wxSize(75, 23), style=0)
        EVT_BUTTON(self.btnEnde, wxID_WXFHAUPTBTNENDE, self.OnBtnendeButton)
        EVT_PAINT(self.btnEnde, self.OnTranslatableControlPaint)

        self.cobAufloesung = wxComboBox(choices=['800 600', '1024 768',
              '1280 1024', '1600 1200'], id=wxID_WXFHAUPTCOBAUFLOESUNG,
              name='cobAufloesung', parent=self.winSetup, pos=wxPoint(96, 32),
              size=wxSize(125, 21), style=0, validator=wxDefaultValidator,
              value='1280 1024')
        self.cobAufloesung.SetLabel('1280 1024')
        self.cobAufloesung.Enable(false)
        EVT_KILL_FOCUS(self.cobAufloesung, self.OnCobaufloesungKillFocus)

        self.chbRootless = wxCheckBox(id=wxID_WXFHAUPTCHBROOTLESS,
              label='-rootless: Anzeige ohne Hintergrundbild',
              name='chbRootless', parent=self.winSetup, pos=wxPoint(8, 80),
              size=wxSize(272, 13), style=0)
        self.chbRootless.SetValue(false)
        self.chbRootless.SetHelpText('Hilfe rootless')
        EVT_CHECKBOX(self.chbRootless, wxID_WXFHAUPTCHBROOTLESS,
              self.OnChbrootlessCheckbox)
        EVT_PAINT(self.chbRootless, self.OnTranslatableControlPaint)

        self.chbOnce = wxCheckBox(id=wxID_WXFHAUPTCHBONCE,
              label='-once: Nach Beendigung der Session beenden',
              name='chbOnce', parent=self.winSetup, pos=wxPoint(8, 94),
              size=wxSize(280, 16), style=0)
        self.chbOnce.SetValue(true)
        self.chbOnce.SetHelpText('Hiolfe once')
        EVT_CHECKBOX(self.chbOnce, wxID_WXFHAUPTCHBONCE, self.OnChbonceCheckbox)
        EVT_PAINT(self.chbOnce, self.OnTranslatableControlPaint)

        self.chbNoWinKill = wxCheckBox(id=wxID_WXFHAUPTCHBNOWINKILL,
              label='-nowinkill: Abbruch durch Windows unterbinden',
              name='chbNoWinKill', parent=self.winSetup, pos=wxPoint(8, 112),
              size=wxSize(296, 13), style=0)
        self.chbNoWinKill.SetValue(false)
        EVT_CHECKBOX(self.chbNoWinKill, wxID_WXFHAUPTCHBNOWINKILL,
              self.OnChbnowinkillCheckbox)
        EVT_PAINT(self.chbNoWinKill, self.OnTranslatableControlPaint)

        self.chbNoUnixKill = wxCheckBox(id=wxID_WXFHAUPTCHBNOUNIXKILL,
              label='-nounixkill: Abbruch durch Unix mit Ctrl+Alt+Backspace unterbinden',
              name='chbNoUnixKill', parent=self.winSetup, pos=wxPoint(8, 128),
              size=wxSize(344, 13), style=0)
        self.chbNoUnixKill.SetValue(false)
        EVT_CHECKBOX(self.chbNoUnixKill, wxID_WXFHAUPTCHBNOUNIXKILL,
              self.OnChbnounixkillCheckbox)
        EVT_PAINT(self.chbNoUnixKill, self.OnTranslatableControlPaint)

        self.chbEmulate3Buttons = wxCheckBox(id=wxID_WXFHAUPTCHBEMULATE3BUTTONS,
              label='-emulate3buttons', name='chbEmulate3Buttons',
              parent=self.winSetup, pos=wxPoint(8, 144), size=wxSize(104, 13),
              style=0)
        self.chbEmulate3Buttons.SetValue(true)
        EVT_CHECKBOX(self.chbEmulate3Buttons, wxID_WXFHAUPTCHBEMULATE3BUTTONS,
              self.OnChbemulate3buttonsCheckbox)
        EVT_PAINT(self.chbEmulate3Buttons, self.OnTranslatableControlPaint)

        self.tcEmulate3ButtonsTimeout = wxTextCtrl(id=wxID_WXFHAUPTTCEMULATE3BUTTONSTIMEOUT,
              name='tcEmulate3ButtonsTimeout', parent=self.winSetup,
              pos=wxPoint(128, 140), size=wxSize(32, 21), style=0, value='50')
        self.tcEmulate3ButtonsTimeout.Enable(true)
        EVT_TEXT(self.tcEmulate3ButtonsTimeout,
              wxID_WXFHAUPTTCEMULATE3BUTTONSTIMEOUT,
              self.OnTcemulate3buttonstimeoutText)

        self.stEmulate3ButtonsTimeout = wxStaticText(id=wxID_WXFHAUPTSTEMULATE3BUTTONSTIMEOUT,
              label='timeout (ms)', name='stEmulate3ButtonsTimeout',
              parent=self.winSetup, pos=wxPoint(168, 144), size=wxSize(104, 13),
              style=0)
        EVT_PAINT(self.stEmulate3ButtonsTimeout,
              self.OnTranslatableControlPaint)

        self.stXWinBinary = wxStaticText(id=wxID_WXFHAUPTSTXWINBINARY,
              label='XFree86 Binary:', name='stXWinBinary',
              parent=self.winSetup, pos=wxPoint(8, 56), size=wxSize(80, 13),
              style=0)
        EVT_PAINT(self.stXWinBinary, self.OnTranslatableControlPaint)

        self.cobXWinBinary = wxComboBox(choices=[r'C:\cygwin\usr\X11R6\bin\XWin.exe',
              r'D:\cygwin\usr\X11R6\bin\XWin.exe',
              r'E:\cygwin\usr\X11R6\bin\XWin.exe'],
              id=wxID_WXFHAUPTCOBXWINBINARY, name='cobXWinBinary',
              parent=self.winSetup, pos=wxPoint(96, 56), size=wxSize(125, 21),
              style=0, validator=wxDefaultValidator,
              value=r'C:\cygwin\usr\X11R6\bin\XWin.exe')
        self.cobXWinBinary.SetLabel(r"C:\cygwin\usr\X11R6\bin\XWin.exe")
        EVT_KILL_FOCUS(self.cobXWinBinary, self.OnCobxwinbinaryKillFocus)

        self.btnBrowseXWinBinary = wxButton(id=wxID_WXFHAUPTBTNBROWSEXWINBINARY,
              label='...', name='btnBrowseXWinBinary', parent=self.winSetup,
              pos=wxPoint(232, 56), size=wxSize(32, 23), style=0)
        EVT_BUTTON(self.btnBrowseXWinBinary, wxID_WXFHAUPTBTNBROWSEXWINBINARY,
              self.OnBtnbrowsexwinbinaryButton)

        self.btnSucheXWinBinary = wxButton(id=wxID_WXFHAUPTBTNSUCHEXWINBINARY,
              label='Suche...', name='btnSucheXWinBinary', parent=self.winSetup,
              pos=wxPoint(272, 56), size=wxSize(64, 23), style=0)
        EVT_BUTTON(self.btnSucheXWinBinary, wxID_WXFHAUPTBTNSUCHEXWINBINARY,
              self.OnBtnsuchexwinbinaryButton)
        EVT_PAINT(self.btnSucheXWinBinary, self.OnTranslatableControlPaint)

        self.stBefehl = wxStaticText(id=wxID_WXFHAUPTSTBEFEHL,
              label='Auszuf\xfchrender Befehl:', name='stBefehl',
              parent=self.winSetup, pos=wxPoint(8, 160), size=wxSize(216, 13),
              style=0)
        EVT_PAINT(self.stBefehl, self.OnTranslatableControlPaint)

        self.tcBefehl = wxTextCtrl(id=wxID_WXFHAUPTTCBEFEHL, name='tcBefehl',
              parent=self.winSetup, pos=wxPoint(8, 176), size=wxSize(320, 21),
              style=0, value='tcBefehl')

        self.chbAufloesung = wxCheckBox(id=wxID_WXFHAUPTCHBAUFLOESUNG,
              label='Aufl\xf6sung:', name='chbAufloesung', parent=self.winSetup,
              pos=wxPoint(8, 36), size=wxSize(80, 13), style=0)
        self.chbAufloesung.SetValue(false)
        EVT_CHECKBOX(self.chbAufloesung, wxID_WXFHAUPTCHBAUFLOESUNG,
              self.OnChbaufloesungCheckbox)
        EVT_PAINT(self.chbAufloesung, self.OnTranslatableControlPaint)

        self.rbZielhost = wxRadioButton(id=wxID_WXFHAUPTRBZIELHOST,
              label='Zielhost:', name='rbZielhost', parent=self.winStart,
              pos=wxPoint(24, 24), size=wxSize(79, 13), style=wxTAB_TRAVERSAL)
        self.rbZielhost.SetValue(true)
        EVT_RADIOBUTTON(self.rbZielhost, wxID_WXFHAUPTRBZIELHOST,
              self.OnRbzielhostRadiobutton)
        EVT_PAINT(self.rbZielhost, self.OnTranslatableControlPaint)

        self.rbBroadcast = wxRadioButton(id=wxID_WXFHAUPTRBBROADCAST,
              label='Broadcast (Connect zu "zuf\xe4lligem" Rechner)',
              name='rbBroadcast', parent=self.winStart, pos=wxPoint(24, 80),
              size=wxSize(288, 13), style=wxTAB_TRAVERSAL)
        self.rbBroadcast.SetValue(false)
        EVT_RADIOBUTTON(self.rbBroadcast, wxID_WXFHAUPTRBBROADCAST,
              self.OnRbbroadcastRadiobutton)
        EVT_PAINT(self.rbBroadcast, self.OnTranslatableControlPaint)

        self.chbFont = wxCheckBox(id=wxID_WXFHAUPTCHBFONT,
              label="-fp (fontpath) angeben (f\xfcr Sun's)?", name='chbFont',
              parent=self.winStart, pos=wxPoint(40, 48), size=wxSize(272, 13),
              style=0)
        self.chbFont.SetValue(false)
        EVT_CHECKBOX(self.chbFont, wxID_WXFHAUPTCHBFONT, self.OnChbfontCheckbox)
        EVT_PAINT(self.chbFont, self.OnTranslatableControlPaint)

        self.chbEigeneIP = wxCheckBox(id=wxID_WXFHAUPTCHBEIGENEIP,
              label='Eigene IP:', name='chbEigeneIP', parent=self.winStart,
              pos=wxPoint(24, 124), size=wxSize(96, 13), style=0)
        self.chbEigeneIP.SetValue(true)
        EVT_CHECKBOX(self.chbEigeneIP, wxID_WXFHAUPTCHBEIGENEIP,
              self.OnChbeigeneipCheckbox)
        EVT_PAINT(self.chbEigeneIP, self.OnTranslatableControlPaint)

        self.staticLine1 = wxStaticLine(id=wxID_WXFHAUPTSTATICLINE1,
              name='staticLine1', parent=self.winStart, pos=wxPoint(32, 104),
              size=wxSize(264, 2), style=0)

        self.btnSaveConfig = wxButton(id=wxID_WXFHAUPTBTNSAVECONFIG,
              label='Speichere', name='btnSaveConfig', parent=self.winStart,
              pos=wxPoint(144, 160), size=wxSize(75, 23), style=0)
        EVT_BUTTON(self.btnSaveConfig, wxID_WXFHAUPTBTNSAVECONFIG,
              self.OnBtnsaveconfigButton)
        EVT_PAINT(self.btnSaveConfig, self.OnTranslatableControlPaint)

        self.tcEigeneIP = wxTextCtrl(id=wxID_WXFHAUPTTCEIGENEIP,
              name='tcEigeneIP', parent=self.winStart, pos=wxPoint(136, 120),
              size=wxSize(168, 21), style=0, value='')
        EVT_TEXT(self.tcEigeneIP, wxID_WXFHAUPTTCEIGENEIP,
              self.OnTceigeneipText)

        self.stLanguage = wxStaticText(id=wxID_WXFHAUPTSTLANGUAGE,
              label='Sprache:', name='stLanguage', parent=self.winSetup,
              pos=wxPoint(8, 10), size=wxSize(64, 13), style=0)
        EVT_PAINT(self.stLanguage, self.OnTranslatableControlPaint)

        self.chLanguage = wxChoice(choices=['English', 'Deutsch'],
              id=wxID_WXFHAUPTCHLANGUAGE, name='chLanguage',
              parent=self.winSetup, pos=wxPoint(96, 8), size=wxSize(125, 21),
              style=0, validator=wxDefaultValidator)
        self.chLanguage.SetSelection(1)
        EVT_CHOICE(self.chLanguage, wxID_WXFHAUPTCHLANGUAGE,
              self.OnChlanguageChoice)

        self._init_coll_nbHaupt_Pages(self.nbHaupt)

    def __init__(self, parent):
        
        self.config = {}

        # Dictionary containing all the translatable texts.
        # Set by self.SetTexts()
        self.__labels = {}
        
        self.cfg_app_name = 'X Host Chooser'
        self.cfg_vendor_name = 'Delphi Deutschland GmbH'
        self._init_ctrls(parent)
        
        #icon_file = 'X_Transparent.xpm'
        #icon_type = wxBITMAP_TYPE_XPM
        
        icon_file = "X_swoosh_logo_32x32x16.ico"
        icon_type = wxBITMAP_TYPE_ICO
        
        self.icon = wxIcon(icon_file, icon_type)
        self.SetIcon(self.icon)
        
        ip = socket.gethostbyname(socket.gethostname())
        self.UpdateEigeneIP(wert = ip)

        self.SetTexts(self.chLanguage.GetSelection())

######################################################## Frame

    def OnWxfhauptActivate(self, event):
        """Update Config für alle möglichen Wert, wenn das Form aktiviert wird"""
        
        # Nur dann updaten, wenn das Fenster auch aktiviert wird
        # dh. nicht updaten, wenn es deaktiviert wird
        if (event.GetActive()):
            self.LoadConfig()
            
            self.UpdateZielhostBroadcast()
            self.UpdateEigeneIP()
            self.UpdateAufloesungCheckbox()
            self.UpdateChbEmulate3Buttons()
            self.UpdateOnce()
            self.UpdateRootless()
            self.UpdateNoUnixKill()
            self.UpdateNoWinKill()
            self.UpdateXWinBinary()
            self.UpdateFont()
            self.UpdateLanguage()
            
        event.Skip()

    def OnWxfhauptClose(self, event):
        """Der User möchte das Programm beenden"""
        
        # Konfiguration abspeichern
        self.SaveConfig()
        
        event.Skip()

    def OnNbhauptNotebookPageChanging(self, event):
        """Der User wechselt die Notebook Seite"""
        
        # Konfiguration abspeichern
        self.SaveConfig()
        
        event.Skip()
            
######################################################## Comboboxen

    def OnCobaufloesungKillFocus(self, event):
        """Der User hatte den Focus auf die Combobox Auflösung gelegt, und verlässt das Feld nun"""
        
        # Update die Combobox mit den aktuellen Werten
        self.UpdateCombobox(self.cobAufloesung, 'auflösung')
        event.Skip()

    def OnCobxwinbinaryKillFocus(self, event):
        """Übertrage den ausgewählten/eingegebenen Wert für das XWin Binary in die Combobox-Werte"""
        
        # Update die Combobox mit den aktuellen Werten
        self.UpdateCombobox(self.cobXWinBinary, 'XWinBinary')
        event.Skip()

    def OnCobzielhostKillFocus(self, event):
        """Der User hatte den Focus auf dem Feld Zielhost IP und verlässt es nun"""
        
        # Update die Combobox mit den aktuellen Werten
        self.UpdateCombobox(self.cobZielhost, 'query')
        event.Skip()

    def OnCobeigeneipKillFocus(self, event):

        event.Skip()

######################################################## Radiobuttons

    def OnRbzielhostRadiobutton(self, event):
        """Update Auswahl des Zielhosts"""
        
        self.Layout()
        
        # Zielhost bzw. -broadcast Radiobuttons updaten
        self.UpdateZielhostBroadcast()
        event.Skip()
    
    def OnRbbroadcastRadiobutton(self, event):
        """Update Auswahl auf Broadcast"""
        
        # Zielhost bzw. -broadcast Radiobuttons updaten
        self.UpdateZielhostBroadcast()
        event.Skip()

######################################################## Checkboxen

    def OnChbemulate3buttonsCheckbox(self, event):
        """Der User hat die Checkbox chbEmulate3Buttons angeklickt"""
        
        # Verstecke oder zeige das Textfeld tcEmulate3ButtonsTimeout und update Config
        self.UpdateChbEmulate3Buttons()
        event.Skip()

    def OnChbeigeneipCheckbox(self, event):
        """Update die Eigene IP, da der User auf die Checkbox chbEigeneIP geklickt hat"""
        
        # Verstecke oder zeige das Textfeld tcEigeneIP und update Config
        self.UpdateEigeneIP()
        event.Skip()

    def OnChbaufloesungCheckbox(self, event):
        """Update die gewünschte Auflösung, da auf Checkbox chbAufloesung geklickt wurde"""
        
        # Verstecke/zeige Combobox cobAufloesung und update Config entsprechend
        self.UpdateAufloesungCheckbox()
        event.Skip()

    def OnChbrootlessCheckbox(self, event):
        """Der User hat die Checkbox 'rootless' angeklickt"""
        
        # Update Config entsprechend Auswahl der Checkbox
        self.UpdateRootless()
        event.Skip()

    def OnChbonceCheckbox(self, event):
        """Der User hat die Checkbox 'once' angeklickt"""
        
        # Update Config entsprechend Auswahl der Checkbox
        self.UpdateOnce()
        event.Skip()
        
    def OnChbnowinkillCheckbox(self, event):
        """Der User hat die Checkbox 'NoWinKill' angeklickt"""
        
        # Update Config entsprechend Auswahl der Checkbox
        self.UpdateNoWinKill()
        event.Skip()

    def OnChbnounixkillCheckbox(self, event):
        """Der User hat die Checkbox 'NoUnixKill' angeklickt"""
        
        # Update Config entsprechend Auswahl der Checkbox
        self.UpdateNoUnixKill()
        event.Skip()

    def OnChbfontCheckbox(self, event):
        """Checkbox 'Font' wurde gedrückt"""
        
        # Update Config entsprechend Auswahl der Checkbox
        self.UpdateFont()
        event.Skip()

######################################################## Textcontrols

    def OnTcemulate3buttonstimeoutText(self, event):
        """Der User hat Text in dem Feld für den Emulate3Buttons Timeout eingegeben"""
        
        self.UpdateConfig('emulate3buttons', self.tcEmulate3ButtonsTimeout.GetValue())
        event.Skip()

######################################################## Buttons

    def OnBtnbrowsexwinbinaryButton(self, event):
        """Aktion, wenn auf den '...' Button für XWin Binary gedrückt wurde"""
        
        dlg = wxFileDialog(self, "Datei auswählen", ".", "",
                           "alle|*|Ausführbare Dateien (*.exe)|*.exe|Alle Dateien (*.*)|*.*", wxOPEN)
        try:
            if dlg.ShowModal() == wxID_OK:
                filename = dlg.GetPath()
                # Speichere den Dateinamen
                self.cobXWinBinary.SetValue(filename)
                self.UpdateXWinBinary()
        finally:
            dlg.Destroy()
        event.Skip()

    def OnBtnendeButton(self, event):
        """Beende das Programm"""
        
        self.Close()
        event.Skip()

    def OnBtnrunButton(self, event):
        """Der User hat auf den 'Run' Button gedrückt.  Starte die Show"""
        
        # Splitte den tcBefehl String in eine Liste, damit dies an os.spawnv
        # übergeben werden kann.  Splitte an whitespaces
        args = string.split(self.tcBefehl.GetValue())
        # Rufe den Befehl auf
        os.spawnv(os.P_NOWAIT, args[0], args)
        event.Skip()

    def OnBtnsuchexwinbinaryButton(self, event):
        """Der User möchte, das nach dem XWin.exe Binary gesucht wird"""
        
        dlg = wxMessageDialog(self, 'Die Suche nach dem XWin.exe Binary ist noch nicht implementiert...',
                              'Suche...', wxICON_EXCLAMATION)
        
        dlg.ShowModal()
        
        event.Skip()
        
######################################################## Eigene Methoden

    def GetLabelText(self, key):
        """Liefere das Label für den angegebenen Key."""
        
        if key in self.__labels:
            return self.__labels[key]
        else:
            return 'Key %s nicht vorhanden' % key

    def BaueBefehlNeu(self):
        """Baue den im Textfeld tcBefehl gespeicherten Befehl neu auf."""
        
        # Für schnelleren Zugriff
        cfg = self.config
        tcb = self.tcBefehl
        
        tcb.SetValue('')
        
        if (cfg.has_key('XWinBinary')):
            tcb.AppendText(cfg['XWinBinary'])
        
        if (cfg.has_key('query')):
            if (cfg['query'] is None):
                tcb.AppendText(' -broadcast')
            else:
                tcb.AppendText(' -query %s' % cfg['query'])
        
        if (cfg.has_key('from')):
            if (not (cfg['from'] is None)):
                tcb.AppendText(' -from %s' % cfg['from'])
                
        if (cfg.has_key('auflösung')):
            if (not (cfg['auflösung'] is None)):
                tcb.AppendText(' -screen :0 %s' % cfg['auflösung'])
                
        if (cfg.has_key('rootless')):
            if (cfg['rootless']):
                tcb.AppendText(' -rootless')
                
        if (cfg.has_key('once')):
            if (cfg['once']):
                tcb.AppendText(' -once')
                
        if (cfg.has_key('nowinkill')):
            if (cfg['nowinkill']):
                tcb.AppendText(' -nowinkill')
            else:
                tcb.AppendText(' -winkill')
                
        if (cfg.has_key('nounixkill')):
            if (cfg['nounixkill']):
                tcb.AppendText(' -nounixkill')
            else:
                tcb.AppendText(' -unixkill')
                
        if (cfg.has_key('emulate3buttons')):
            if (not (cfg['emulate3buttons'] is None)):
                tcb.AppendText(' -emulate3buttons %s' % cfg['emulate3buttons'])
                
        if (cfg.has_key('font')):
            c = cfg['font']
            if ((not (cfg['font'] is None)) and (cfg['font'] != 0)):
                tcb.AppendText(' -fp tcp/%s:7100' % cfg['query'])
        
    def UpdateConfig(self, key, value = None):
        """Update das dict in dem die aktuelle Konfiguration abgelegt ist.
        Diese Methode baut den Befehlsstring (in tcBefehl) neu auf."""
        
        # Speichere den übergebenen Wert in der Konfiguration
        self.config[key] = value
        
        # Befehl neu aufbauen
        self.BaueBefehlNeu()
        
        pass
    
    def GetConfigKey(self, key):
        """Gebe den in der Konfiguration gespeicherte Key zurück."""

        if key in self.config:
            return self.config[key]
        else:
            return None
    
    def SaveConfig(self):
        """Methode, um die Konfiguration für einen späteren Aufruf zu speichern"""
        
        cfg = wxConfig(self.cfg_app_name, self.cfg_vendor_name)
        conf = self.config
        
        # Haben wir überhaupt etwas, was gespeichert werden kann?
        if conf == {}:
            # Nein, (noch) keine Konfiguration vorhanden
            # -> Raus hier!
            return
        
        # Speichere Werte aus den Checkboxen
        for name in ('font', 'rootless', 'once', 'nowinkill', 'nounixkill'):
            if (conf.has_key(name)):
                wert = conf[name]
                try:
                    i = int(wert)
                except:
                    i = -1
                cfg.WriteInt(name, i)
                
        if (conf.has_key('emulate3buttons')):
            if (conf['emulate3buttons'] is None):
                cfg.WriteInt('emulate3buttons', -1)
            else:
                try:
                    i = int(conf['emulate3buttons'])
                except:
                    i = -1
                    
                cfg.WriteInt('emulate3buttons', i)

        if (conf.has_key('XWinBinary')):
            cfg.Write('XWinBinary', conf['XWinBinary'])
        
        if (cfg.HasGroup('XWinBinaries')):
            cfg.DeleteGroup('XWinBinaries')
        cfg.SetPath('XWinBinaries')
        for i in range(self.cobXWinBinary.GetCount()):
            cfg.Write('Binary %d' % i, self.cobXWinBinary.GetString(i))
        cfg.SetPath('..')
        
        if (conf.has_key('auflösung')):
            if (conf['auflösung'] is None):
                cfg.Write('auflösung', '')
            else:
                cfg.Write('auflösung', conf['auflösung'])
            
        if (cfg.HasGroup('Auflösungen')):
            cfg.DeleteGroup('Auflösungen')
        cfg.SetPath('Auflösungen')
        for i in range(self.cobAufloesung.GetCount()):
            cfg.Write('Auflösung %d' % i, self.cobAufloesung.GetString(i))
        cfg.SetPath('..')

        if (conf.has_key('from')):
            if (conf['from'] is None):
                cfg.Write('from', '')
            else:
                cfg.Write('from', conf['from'])

        if (conf.has_key('query')):
            if (conf['query'] is None):
                cfg.Write('query', '')
            else:
                cfg.Write('query', conf['query'])
            
        if (cfg.HasGroup('Ziel Hosts')):
            cfg.DeleteGroup('Ziel Hosts')
        cfg.SetPath('Ziel Hosts')
        for i in range(self.cobZielhost.GetCount()):
            cfg.Write('Zielhost %d' % i, self.cobZielhost.GetString(i))
        cfg.SetPath('..')
        
    def LoadConfig(self):
        """Methode, um die Konfiguration zu laden"""
        
        # Erzeuge wxConfig Objekt
        cfg = wxConfig(self.cfg_app_name, self.cfg_vendor_name)

        # Liste mit definition von allen Config *GRUPPEN* und zugehörigen Comboboxen
        # cfgs[0][0]: Name der Group/des Paths aus der Config
        # cfgs[0][1]: Combobox das alle Werte der Group aufnimmt
        # cfgs[1][0]: Name des ausgewählten Elements aus der Config
        # cfgs[1][1]: Methode um dieses Element zu übernehmen
        cfgs = (
                (('Ziel Hosts', self.cobZielhost), ('query', self.UpdateZielhostBroadcast)),
                (('Auflösungen', self.cobAufloesung), ('auflösung', self.UpdateAufloesungCheckbox)),
                (('XWinBinaries', self.cobXWinBinary), ('XWinBinary', self.UpdateXWinBinary))
               )

        # Durchlaufe diese Liste
        for c in cfgs:
            # Gibt es in der cfg die gewünschte Gruppe?
            if (cfg.HasGroup(c[0][0])):
                # Ja, es gibt die Gruppe
                
                # Leere die Combobox; dh. entferne die Defaultwerte
                c[0][1].Clear()
                # Gehe in der cfg in die Gruppe hinein
                cfg.SetPath(c[0][0])
                # Lese das erste Element
                entry = cfg.GetFirstEntry()
                # Solange wie es Elemente gibt (also entry[0] != 0), mache was
                while (entry[0]):
                    # Es gibt noch Elemente
                    
                    # Lese das Element aus der cfg und füge es an die Combobox Choices Liste an
                    c[0][1].Append(cfg.Read(entry[1]))
                    # Hole das nächste Element
                    entry = cfg.GetNextEntry(entry[2])
                # Lösche Handle auf Element
                entry = None
                # Gehe in der Config einen Schritt hoch
                cfg.SetPath('..')
            # Gibt es in der cfg das gewünschte Element für den ausgewählten Wert?
            if (cfg.HasEntry(c[1][0])):
                # Ja, es gibt ihn
                
                # Auslesen und an Methode übergeben, die das Form entsprechend updated
                c[1][1](cfg.Read(c[1][0]))

        # Liste mit allen Config *ELEMENTEN* und den dazu gehörenden Checkboxen, bzw. Updatemethoden
        # cfgs[0]: Name des Config Elements
        # cfgs[1]: Updatemethode
        cfgs = (
                ('once', self.UpdateOnce), 
                ('rootless', self.UpdateRootless), 
                ('nounixkill', self.UpdateNoUnixKill), 
                ('nowinkill', self.UpdateNoWinKill), 
                ('emulate3buttons', self.UpdateChbEmulate3Buttons),
                ('font', self.UpdateFont),
                ('language', self.UpdateLanguage)
               )

        # Durchlaufe auch diese Liste
        for c in cfgs:
            # Sofern es einen Config Entry gibt, "bearbeite" ihn
            if (cfg.HasEntry(c[0])):
                # Es gibt einen Config Entry
                
                # Lesen und an Updatemethode verfüttern
                c[1](cfg.ReadInt(c[0]))

        # Die Sprache hat sich u.U. geändert.  Texte setzen
        self.SetTexts(self.GetConfigKey('Language'))
        
        # Fertig mit LoadConfig
        return true
    
    def UpdateXWinBinary(self, wert = None):
        """Speichere das ausgewählte Cygwin XWin Binary."""
        
        if (not (wert is None)):
            self.cobXWinBinary.SetValue(wert)
        
        self.UpdateConfig('XWinBinary', self.cobXWinBinary.GetValue())
            
    def UpdateNoWinKill(self, wert = None):
        """Update Auswahl für Checkbox 'No  WinKill' in der Config"""
        
        if (not (wert is None)):
            self.chbNoWinKill.SetValue(wert)
        
        self.UpdateConfig('nowinkill', self.chbNoWinKill.GetValue())
        
    def UpdateNoUnixKill(self, wert = None):
        """Update Auswahl für Checkbox 'NoUnixKill' in der Config"""
        
        if (not (wert is None)):
            self.chbNoUnixKill.SetValue(wert)
        
        self.UpdateConfig('nounixkill', self.chbNoUnixKill.GetValue())

    def UpdateEigeneIP(self, wert = None):
        """Update 'from', da auf Checkbox chbEigeneIP geklickt wurde"""
        
        if (not (wert is None)):
            self.chbEigeneIP.SetValue(wert != '')
            self.tcEigeneIP.SetValue(wert)
        
        # Schalte das Textfeld für die IP ein oder aus.
        self.tcEigeneIP.Enable(self.chbEigeneIP.GetValue())
        # Wurde die Checkbox an-gehakt, oder ab-gehakt?
        if (self.chbEigeneIP.GetValue()):
            # Sie wurde an-gehakt
            # Speichere die eingetragene IP in der Config
            self.UpdateConfig('from', self.tcEigeneIP.GetValue())
            
        else:
            # Sie wurde ab-gehakt
            # Lösche IP in der Config
            self.UpdateConfig('from', None)
        
    def UpdateChbEmulate3Buttons(self, wert = None):
        """Update 'Emulate3ButtonsTimeout', da auf Checkbox chbEmlutate3Buttons geklickt wurde"""
        
        if (not (wert is None)):
            self.chbEmulate3Buttons.SetValue(wert != '')
            self.tcEmulate3ButtonsTimeout.SetValue(`wert`)
        
        self.tcEmulate3ButtonsTimeout.Enable(self.chbEmulate3Buttons.GetValue())
        if (self.chbEmulate3Buttons.GetValue()):
            self.UpdateConfig('emulate3buttons', self.tcEmulate3ButtonsTimeout.GetValue())
            
        else:
            self.UpdateConfig('emulate3buttons', None)
                
    def UpdateAufloesungCheckbox(self, wert = None):
        """Update 'auflösung', da die Checkbox chbAufloesung geklickt wurde"""
        
        if (not (wert is None)):
            self.chbAufloesung.SetValue(wert != '')
            self.cobAufloesung.SetValue(wert)

        self.cobAufloesung.Enable(self.chbAufloesung.GetValue())
        if (self.chbAufloesung.GetValue()):
            self.UpdateConfig('auflösung', self.cobAufloesung.GetValue())
        
        else:
            self.UpdateConfig('auflösung', None)

    def UpdateZielhostBroadcast(self, wert = None):
        """Schalte Zielhost bzw. Broadcast ein/aus"""
        
        # Wenn auf dieses Event ausgelöst wird, wurde der Radiobutton für "Zielhost"
        # gedrückt.  Dh. Textfeld für IP des Zielhosts aktivieren und Radiobutton
        # für Broadcast deaktivieren
        
        # Wenn der Zielhost Radiobutton aktiviert wurde, mache:
        # - Setze Broadcast auf False
        # - Setze Zielhost RB auf True
        # - Textfeld für Zielhost IP aktivieren
        # andernfalls:
        # - Setze Broadcast auf True
        # - Setze Zielhost RB auf False
        # - Textfeld für Zielhost IP deaktvieren
        if (not (wert is None)):
            self.cobZielhost.SetValue(wert)
            self.rbZielhost.SetValue(wert != '')
            
        if (self.rbZielhost.GetValue()):
            # Zielhost Radiobutton wurde angeklickt
            
            # Setze Broadcast auf false
            self.rbBroadcast.SetValue(false)
            
            # Setze Zielhost RB auf true
            self.rbZielhost.SetValue(true)
        
            # Textfeld für Zielhost IP aktivieren
            self.cobZielhost.Enable(true)
        
            # Checkbox für fontpath aktivieren
            self.chbFont.Enable(true)
        
            # Zielhost IP in Config speichern
            self.UpdateConfig('query', self.cobZielhost.GetValue())
            
        else:
            # Zielhost Radiobutton wurde NICHT angeklickt
            
            # Setze Broadcast auf true
            self.rbBroadcast.SetValue(true)
            
            # Setze Zielhost RB auf false
            self.rbZielhost.SetValue(false)
        
            # Textfeld für Zielhost IP deaktivieren
            self.cobZielhost.Enable(false)
            
            # Checkbox für fontpath deaktivieren
            self.chbFont.Enable(false)
        
            # Zielhost IP in Config speichern
            self.UpdateConfig('query', None)
        
    def UpdateFont(self, wert = None):
        """Update Auswahl für Checkbox 'font' in der Config"""
        
        if (not (wert is None)):
            self.chbFont.SetValue(wert)
        
        self.UpdateConfig('font', self.chbFont.GetValue())
        
    def UpdateRootless(self, wert = None):
        """Update Auswahl für Checkbox 'rootless' in der Config"""
        
        if (not (wert is None)):
            self.chbRootless.SetValue(wert)
        
        self.UpdateConfig('rootless', self.chbRootless.GetValue())
        
    def UpdateOnce(self, wert = None):
        """Update Auswahl für Checkbox 'once' in der Config"""
        
        if (not (wert is None)):
            self.chbOnce.SetValue(wert)
        
        self.UpdateConfig('once', self.chbOnce.GetValue())
                
    def UpdateCombobox(self, combobox, cfgname):
        """Übertrage einen eingegebenen Wert aus dem Textfeld der Combobox in die Combobox Dropdown Werte"""
        
        # Falls der eingegebene Text noch nicht den Combobox-Werten vorhanden ist,
        # hänge ihn an
        # Erstmal führende und anhängende Leerzeichen entfernen
        combobox.SetValue(string.strip(combobox.GetValue()))
        # Dann Wert in der Config speichern
        self.UpdateConfig(cfgname, combobox.GetValue())
        # Wurde ein nicht-leerer String eingegeben?
        if (combobox.GetValue() != ""):
            # Gibt's den Wert schon in den Comboboxwerten?
            if (combobox.FindString(combobox.GetValue()) == -1):
                # Text noch nicht vorhanden -> Anhängen
                combobox.Append(combobox.GetValue())

    def untranslatedText(self, text):
        """Return the text without any modifications.  Used by SetTexts."""
        return text

    def SetTexts(self, lang_index):
        """Set texts of all the elements on the frame.
        Parameters:
            lang: Index to the given language, as set in the chLanguage element.
            """

        # Liste mit den unterstützten Sprachen
        langs = ['en', 'de']

        try:
            index = int(lang_index)
        except:
            index = 1
            
        lang_code = langs[index]
        
        try:
            t = gettext.translation(domain = 'xhc', localedir = 'locale', 
                                    languages = [lang_code])
            fn = t.gettext
        except IOError:
            fn = self.untranslatedText

        global _
        _ = fn

        self.__labels['btnEnde']                    = _('Exit')
        self.__labels['btnRun']                     = _('Connect')
        self.__labels['btnSaveConfig']              = _('Save')
        self.__labels['btnSucheXWinBinary']         = _('Search...')
        self.__labels['chbAufloesung']              = _('Resolution:')
        self.__labels['chbEigeneIP']                = _('Local address:')
        self.__labels['chbEmulate3Buttons']         = _('-emulate3buttons')  # Nicht übersetzen
        self.__labels['chbFont']                    = _("-fp: Set search path for fonts to remote machine (Req.d for Sun's)?")
        self.__labels['chbNoWinKill']               = _('-nowinkill: Ctrl+Alt+Backspace does not exit the X Server')
        self.__labels['chbNoUnixKill']              = _('-nounixkill: Alt+F4 does not exit the X Server')
        self.__labels['chbOnce']                    = _('-once: Quit after termination of session')
        self.__labels['chbRootless']                = _("-rootless: Don't use a root window")
        self.__labels['rbBroadcast']                = _('Broadcast (Connect to "random" server)')
        self.__labels['rbZielhost']                 = _('Target host:')
        self.__labels['stBefehl']                   = _('Auszuführender Befehl:')
        self.__labels['stEmulate3ButtonsTimeout']   = _('timeout (ms)')
        self.__labels['stLanguage']                 = _('Language:')
        self.__labels['stXWinBinary']               = _('XFree86 Binary:')

    def UpdateLanguage(self, wert = None):
        """Speichere die ausgewählte Sprache, und sofern sie sich von der
        vorherigen Unterscheidet, tausche die Texte gegen die der neuen Sprache
        aus."""
        
        if (not (wert is None)):
            self.chLanguage.SetSelection(wert)
            nbSelection = self.nbHaupt.GetSelection()
            self.SetTexts(self.chLanguage.GetSelection())
            if nbSelection != -1:
                self.nbHaupt.SetSelection(0)
                self.nbHaupt.SetSelection(1)
                self.nbHaupt.SetSelection(nbSelection)

        self.UpdateConfig('Language', self.chLanguage.GetSelection())

        
######################################################## Paint Event Handler

    def OnChlanguageChoice(self, event):
        """Auswahl im Feld der Sprachen."""
        
        self.UpdateLanguage(self.chLanguage.GetSelection())
        event.Skip()
    
######################################################## Anderes

    def OnBtnsaveconfigButton(self, event):
        """User hat auf Knopf gedrückt, um die Konfiguration abzuspeichern."""

        # Konfiguration abspeichern
        self.SaveConfig()

        event.Skip()

    def OnTceigeneipText(self, event):
        
        self.UpdateEigeneIP(wert = None)
        
        event.Skip()

    def OnTranslatableControlPaint(self, event):
        """Setze das Label des aufrufenden Objects auf den durch gettext
        übersetzten Wert."""
        
        event.GetEventObject().SetLabel(self.GetLabelText(event.GetEventObject().GetName()))
        
        event.Skip()
