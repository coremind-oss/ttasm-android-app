from kivy.app import App
from kivy.uix.label import Label



class test_func(App):
    def build(self):
        return Label()
    

if __name__=='__main__':
    test_func().run()