from kivy.app import App
from kivy.uix.widget import Widget

class Widgets(Widget):
    pass

class create_widget(App):
    def build(self):
        return Widgets()
    
if __name__ == "__main__":
    create_widget().run()