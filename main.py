# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from sender import Sender
import validator


class MainApp(MDApp):
    title = 'Programmable DDS signal generator'

    def __init__(self):
        super(MainApp, self).__init__()

    def generate_btn_callback(self):
        if validator.valid(self.root.ids):
            sender.send_to_fpga(self.root.ids)
        else:
            validator.show_alert_dialog(self)


if __name__ == '__main__':
    sender = Sender()
    MainApp().run()
