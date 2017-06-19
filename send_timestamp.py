from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from datetime import datetime

 


class Structure(BoxLayout):
    def __init__(self,**kwargs):
        super(Structure,self).__init__(orientation='vertical')

         
        self.lbl = Label(text='Welcome to your personal time management application',font_size=25)
        self.add_widget(self.lbl)
        self.img = Image(source='TTASM.png',size=(250,250))
        self.add_widget(self.img)
        btn = Button(text='START',color=[0,1,1,1],font_size=40)
        btn.bind(on_press=self.action)     
        self.add_widget(btn)
         
         
    def action(self,obj):
        print('Sending timestamp...',datetime.now())

         
class Application(App):
    def build(self):
        return Structure()
     
if __name__ == '__main__':
    Application().run()  
        
        
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.image import Image
# from kivy.uix.button import Button
# from builtins import str
# 
# 
# class Structure(BoxLayout):
#     layout=BoxLayout(orientation='vertical',spacing=10)
#     
#     lbl = Label(text="Welcome to TTASM")
#     img = Image(source = 'TTASM.png',size=(250,250))
#     btn = Button(text="Start",font_size="35",color=[0,0,1,0.8])
#     layout.add_widget(lbl)
#     layout.add_widget(img)
#     layout.add_widget(btn)
#     
# class Application(App):
#     def build(self):
#         str = Structure()
#         return str
#  
# if __name__== '__main__':
#     Application().run()    

    
