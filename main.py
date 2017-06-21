from cgitb import text

from kivy.app import App
from kivy.lang import Builder
from kivy.lang.builder import custom_callback
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text:'TTASM APP'
            font_size: 60
            color: [0,1,0,1]
        Label:
            text:'If you have account, continue to Log In. Otherwise, create account on Sign Up page'
#         Button:
#             text: 'Begin screen'
#             on_press: root.manager.current = 'begin'
        Button:
            text: 'Sign Up'
            on_press: root.manager.current = 'signup'
        Button:
            text: 'Log In'
            on_press: root.manager.current = 'login' 
        Button:
            text: 'Quit'

# <BeginningScreen>:
#     BoxLayout:
#         orientation: 'vertical'
#         Label:
#             text: 'Welcome to start page here will be TTASM start button'
#         Button:
#             text: 'Back to start page'
#             on_press: root.manager.current = 'menu'
<SignupScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Welcome to Sign up page'
            font_size: 60
        Label:
            text: 'Username:'
        TextInput:
            id: 'username'
            multiline: False
        Label:
            text: 'Password:'
        TextInput:
            id: 'password'
            multiline: False
            password: True
        Button:
            text:'Create account'
            on_press:root.show_message()                                                     
        Button:
            text: 'Back to start page'
            on_press: root.manager.current = 'menu'
            
<LoginScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Welcome to Log In page'
            font_size: 60
        Label:
            text: 'QR scanner for logging will be placed here. After login you will be automatically redirected to page with TTASM button for sending timestamp.'
            font_size: 12
        Button:
            text: 'Back to start page'
            on_press: root.manager.current = 'menu'
""")

# Declare both screens
# class BeginningScreen(Screen):
#     pass

class MenuScreen(Screen):
    pass

class SignupScreen(Screen):
    
    def show_message(self):  
        print('Hello')
       
        
    pass

class LoginScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(MenuScreen(name='menu'))
# sm.add_widget(BeginningScreen(name='begin'))
sm.add_widget(SignupScreen(name='signup'))
sm.add_widget(LoginScreen(name='login'))

class TestApp(App):

    def build(self):
        return sm



if __name__ == '__main__':
    TestApp().run()