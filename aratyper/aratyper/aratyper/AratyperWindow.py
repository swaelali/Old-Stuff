# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk  # pylint: disable=E0611
import logging
logger = logging.getLogger('aratyper')

from aratyper_lib import Window
from aratyper.AboutAratyperDialog import AboutAratyperDialog
from aratyper.PreferencesAratyperDialog import PreferencesAratyperDialog

import thread, time
from pygsr import Pygsr
# See aratyper_lib.Window.py for more details about how this class works

class AratyperWindow(Window):
    __gtype_name__ = "AratyperWindow"
    global do_flage
    do_flage = True
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(AratyperWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutAratyperDialog
        self.PreferencesDialog = PreferencesAratyperDialog

        # Code for other initialization actions should be added here.
        
        self.start_btn = self.builder.get_object("start_btn")
        
        self.textview = self.builder.get_object("textview")
        self.textbuffer = self.builder.get_object("textbuffer")
        self.left_btn = self.builder.get_object("left_btn")
        self.center_btn = self.builder.get_object("center_btn")
        self.right_btn = self.builder.get_object("right_btn")


    def save_text(self,phrase):
        self.textbuffer.insert_at_cursor(phrase)
    
    def srprocess(self,threadname):
        speech = Pygsr()
		speech.record(3)
		try:
		    phrase, complete_response = speech.speech_to_text('ar_AE')
		except:
		    phrase = ''
		    global do_flage
		    do_flage = False
		self.save_text(phrase+' ')     
    
         
    def on_start_btn_clicked(self,widget):
        counter = 0
        global do_flage
        do_flage = True
        while do_flage:
            threadname= 'thread'+str(counter)
            thread.start_new_thread(self.srprocess,(threadname,))
 
            counter +=1
            time.sleep(3)
            
    def on_left_btn_clicked(self, widget):
        self.textview.set_justification(Gtk.Justification.LEFT)
    def on_center_btn_clicked(self, widget):
        self.textview.set_justification(Gtk.Justification.CENTER)
    def on_right_btn_clicked(self, widget):
        self.textview.set_justification(Gtk.Justification.RIGHT)
