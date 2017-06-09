# from kivy.app import App
# from kivy.uix.label import Label
# 
# class Hello_app(App):
#     def build(self):
#         return Label(text="Hello World")
#     
# if __name__== "__main__":
#     Hello_app().run()




from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()