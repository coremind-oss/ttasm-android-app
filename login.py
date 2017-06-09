from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
 
class Form(GridLayout):
    def __init__(self, **kwargs):
        super(Form,self).__init__(**kwargs)
        self.cols = 2
         
        self.add_widget(Label(text='username'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
         
        self.add_widget(Label(text='password'))
        self.password = TextInput(multiline=False,password=True) 
        self.add_widget(self.password)
         
         
        self.add_widget(Label(text='additional text'))  
        self.additional_text = TextInput(multiline=True)    
        self.add_widget(self.additional_text)
 
 
class simpleApp(App):
    def build(self):
        return Form()
     
     
if __name__== '__main__':
    simpleApp().run() 

