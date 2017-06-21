from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


class Form(GridLayout):
    def __init__(self, **kwargs):
        super(Form,self).__init__(**kwargs)
        self.cols = 1
         
        self.add_widget(Label(text='username',font_size=60))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
         
        self.add_widget(Label(text='password',font_size=60))
        self.password = TextInput(multiline=False,password=True) 
        self.add_widget(self.password)
         
        
        btn = Button(text='Log in',font_size=60,background_color=(0,2,0,1))
        btn.bind(on_press = self.click)
        self.add_widget(btn)
    
    def click(self,obj):
        popup = Popup(content=Label(text='Succesfully logged in'),title='Data have been sent',size_hint=(None, None), size=(600, 600))
        popup.open()
        print(self.username.text,self.password.text)   
 
 
class simpleApp(App):
    def build(self):
        return Form()
     
     
if __name__== '__main__':
    simpleApp().run() 

