import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [2, 3, 2, 0]
green = [0, 2, 0, 2]
blue = [0, 5, 2, 2]
purple = [2, 4, 2, 2]

class Main_App(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text="Button #%s" % (i+1),
                        background_color=random.choice(colors),
                         color=random.choice(colors))
            layout.add_widget(btn)
        return layout

Main_App().run()
