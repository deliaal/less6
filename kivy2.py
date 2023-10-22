from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

class Main_App(App):
    def build(self):
        img = Image(source='C:/Users/Impact/Downloads/yamaha.jpg',
                      size_hint=(0.7, 0.7),
                      pos_hint={'center_y': 0.7, 'center_x': 0.7})
        return img

Main_App().run()