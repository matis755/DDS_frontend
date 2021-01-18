from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.app import App


def valid(ids):
    if ids.sine_checkbox.state == 'normal' and ids.triangle_checkbox.state == 'normal' \
            and ids.square_checkbox.state == 'normal':
        return False
    return True


def show_alert_dialog(app):
    app.dialog = MDDialog(title='Error!',
                          text='Please select the shape of the waveform!',
                          buttons=[MDFlatButton(text='Dismiss', on_release=close_dialog)])
    app.dialog.open()


def close_dialog(*args, **kwargs):
    app = App.get_running_app()
    app.dialog.dismiss()
