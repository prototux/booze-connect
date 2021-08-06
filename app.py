import sys
import time
import socket
from device import Device

from bmap import bmap

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout

class RootWidget(BoxLayout):
    pass

class BoozeConnect(App):


    def setANR(self, widget):
        if widget.state == 'down':
            print(f'setting mode {widget.text}')
            self.bmap.settings.ANR.set(widget.text)
            self.root.ids['ANRMode'].text = widget.text

    def build(self):
        # Connect to device and load bmap classes
        self.dev = Device(sys.argv[1])
        self.bmap = bmap(self.dev.read, self.dev.write)
        self.dev.connect()

        # Load UI
        Builder.load_file('ui.kv')
        self.root = RootWidget()

        # Get ANR
        self.parsed = self.bmap.settings.ANR.get()
        self.root.ids['ANRMode'].text = self.parsed['anr_mode'].name
        for mode in self.parsed['supported_modes']:
            modebtn = ToggleButton(text=mode.name, group='ANRMode', on_press=self.setANR)
            self.root.ids['ANRModes'].add_widget(modebtn)

        return self.root

BoozeConnect().run()
