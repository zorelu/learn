#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.app import App
from kivy.uix.button import Button

from jnius import autoclass
MediaPlayer = autoclass('android.hardware.Camera2')
player=MediaPlayer()
media="/sdcard/1.pm3"



def restart_player(_):


        player.open()
        player.startPreview()


class App(App):
    def build(self):
        return Button(text='Hello world!',on_release=restart_player)

if __name__=="__main__":
    App().run()