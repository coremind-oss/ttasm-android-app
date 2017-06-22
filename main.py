from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


# Create screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        spacing: 10
        orientation: 'vertical'
        padding:[40,40,40,40]
        Label:
            text:'TTASM APP'
            font_size: 60
            color: [0,1,0,1]
        Label:
            text:'If you have account, continue to Log In. Otherwise go to Sign Up page'
        Button:
            text: 'Sign Up'
            font_size: 40
            on_press: root.manager.current = 'signup'
        Button:
            text: 'Log In'
            font_size: 40
            on_press: root.manager.current = 'login' 
        Button:
            text: 'Quit'
            font_size: 40
            on_press: root.close_app()

<SignupScreen>:
    BoxLayout:
        spacing: 10
        orientation: 'vertical'
        padding:[40,40,40,40]
        Label:
            text: '< Sign Up >'
            font_size: 60
            color: [0,1,0,1]

        Label:
            text: 'Username:'
            font_size: 40
        TextInput:
            id: 'username'
            multiline: False
            font_size: 40           
        Label:
            text: 'Password:'
            font_size: 40
        TextInput:
            id: 'password'
            multiline: False
            password: True
            font_size: 40        
        Button:
            text:'Create account'
            on_press:root.show_message()
            font_size: 30                                                     
        Button:
            text: 'Back to start page'
            on_press: root.manager.current = 'menu'
            font_size: 30
            
<LoginScreen>:
    BoxLayout:
        spacing: 10
        orientation: 'vertical'
        padding:[40,40,40,40]
        Label:
            text: '< Log In >'
            font_size: 60
            color: [0,1,0,1]

        Label:
            text: 'QR scanner for logging will be placed here.'
        Button:
            text: 'Back to start page'
            on_press: root.manager.current = 'menu'
            font_size: 40
""")

# Declare screens


class MenuScreen(Screen):
    
    def close_app(self):
        exit()
    pass

class SignupScreen(Screen):
    
    def show_message(self):  
        print('Here will be credentials')
        pass

class LoginScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SignupScreen(name='signup'))
sm.add_widget(LoginScreen(name='login'))

class TestApp(App):

    def build(self):
        return sm



if __name__ == '__main__':
    TestApp().run()