from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import pandas as pd
import pymongo

db_conn = pymongo.MongoClient("mongodb://localhost:27017/rishi")
db = db_conn['kivy-login']


# class SignupPage(Screen):
#     name = ObjectProperty(None)
#     email = ObjectProperty(None)   
#     username = ObjectProperty(None)
#     pwd = ObjectProperty(None)

#     global users
    
#     def signUpBtn(self):
#         # creating a DataFrame of the info
#         user = {"Name":self.name.text,
#                 "Email":self.email.text,
#                 "Username":self.username.text,
#                 "Password": self.pwd.text                
#         }
        
#         db.insert_one(user)              


class LoginPage(Screen):
    # _email = ObjectProperty(None)
    # _pwd = ObjectProperty(None)
    # def verify_credentials(self):
    #     if self._email.text == users and self._pwd.text == "password":
    #         self.manager.current = "user"
    
    main_screen = BoxLayout(orientation = 'vertical')
    
    def loginTask(self, instance):        
        
        self.emailLabel = Label(text='Email',
                        size_hint=(.3, .3),
                        pos_hint={'center_x': .5, 'center_y': .5})
        self._email = TextInput(hint_text = 'Email',multiline = False, readonly = False, size_hint = (.4, .3), pos_hint={'center_x': .5, 'center_y': .5} ,halign = 'center', font_size = 30)
        
        
        self.passLabel = Label(text='Password',
                        size_hint=(.3, .3),
                        pos_hint={'center_x': .5, 'center_y': .5})
        self._pwd = TextInput(hint_text = 'Password',multiline = False, readonly = False, size_hint = (.4, .3), pos_hint={'center_x': .5, 'center_y': .5} ,halign = 'center', font_size = 30)

        

        
# class UserPage(Screen):
#     pass


# #reading csv file for email, pass and name

# kv_file = Builder.load_file('login.kv')

class LoginApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(SignupPage())
        self.sm.add_widget(LoginPage())
        self.sm.add_widget(UserPage())
        return self.sm

if __name__ == '__main__':
    LoginApp().run()