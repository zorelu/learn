#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.app import App
from kivy.uix.button import Button

from jnius import autoclass
MediaPlayer = autoclass('android.media.MediaPlayer')
player=MediaPlayer()
media="/sdcard/1.pm3"

def reset_player():
    if (player.isPlaying()):
        player.stop()
    player.reset()

def restart_player(_):
    reset_player()
    try:
        player.setDataSource(media)
        player.prepare()
        player.start()
    except:
        player.reset()

class App(App):
    def build(self):
        return Button(text='Hello world!',on_release=restart_player)

if __name__=="__main__":
    App().run()