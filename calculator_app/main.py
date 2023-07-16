import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from pymongo import MongoClient 

class CalcApp(App):
    welcome_text = 'Welcome to Calculator App'
    def build(self):
        
        #creating end label
        self.label2 = Label(text='Thank you!',
                      size_hint=(.3, .3),
                      pos_hint={'center_x': .5, 'center_y': .5})
        
        #defining arithmetic operators
        self.operators = ['+','-','*','/']
        self.last_operator = None
        
        #this is the entire screen
        main_screen = BoxLayout(orientation = 'vertical')
        
        '''
        these 5 lines makes a text input and a submit button 
        when submit is clicked, the function 'submit' is executed
        '''
        self.username = TextInput(hint_text = '',multiline = False, readonly = False, size_hint = (.4, .3), pos_hint={'center_x': .5, 'center_y': .5} ,halign = 'center', font_size = 30)
        self.user_submit = Button(text = 'Last Calculated Value', size_hint = (.4, .3),pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.user_submit.bind(on_press = self.lastValue)
        main_screen.add_widget(self.username)
        main_screen.add_widget(self.user_submit)
       
       #this is the initial label
        self.label1 = Label(text= self.welcome_text,
                      size_hint=(.3, .3),
                      pos_hint={'center_x': .5, 'center_y': .5})         
        main_screen.add_widget(self.label1)
        
        '''
        creating a text input 'solution_screen' which is the top_screen
        where input buttons/numbers will be displayed
        '''
        self.solution_screen = TextInput(multiline = False, readonly = True, halign = 'right', font_size = 55 )
        main_screen.add_widget(self.solution_screen)
        
        #defining the keypad
        num_array = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in num_array:
            num_screen = BoxLayout()
            for num in row:
                btn = Button(
                    text=num,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                btn.bind(on_press = self.on_button_press)
                num_screen.add_widget(btn)
            main_screen.add_widget(num_screen)
        
        #adding = button    
        equal_btn = Button(
            text = "=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equal_btn.bind(on_press=self.on_solution)
        main_screen.add_widget(equal_btn)
        main_screen.add_widget(self.label2)
        
        return main_screen  
    
    #this function executes when buttons of the calculator keypad are pressed
    def on_button_press(self, instance):

        current_text = self.solution_screen.text
        button_text = instance.text

        if button_text == 'C':
            self.solution_screen.text = ''

        else:
            
            if current_text and (self.last_operator and button_text in self.operators): 
                return
            
            elif current_text == '' and button_text in self.operators:
                return  
    
            else:

                new_screen = current_text + button_text
                self.solution_screen.text = new_screen
        
        
        self.last_operator = button_text in self.operators
        return self.last_operator

    #this function executes the total solution when '=' is pressed
    def on_solution(self, instance):

        current_text = self.solution_screen.text
        
        if current_text:
            
            result = str(eval(current_text))

            # Connect to MongoDB and insert the result
            client = MongoClient('mongodb://localhost:27017/')
            db = client['rishi']
            collection = db['kivy-login']
            collection.insert_one({'result': result})
        
            self.solution_screen.text = str(eval(current_text))
    
    #this function concatenates the usernam with the label1        
    def lastValue(self,instance):
        
        # Connect to MongoDB and insert the result
        client = MongoClient('mongodb://localhost:27017/')
        db = client['rishi']
        collection = db['kivy-login']
            
        lastVal = collection.find_one(sort=[('_id', -1)])
        storedValue = lastVal['result']
        self.username.text = storedValue
    

                
'''
running the code
'''

if __name__ == '__main__':
    app = CalcApp()
    app.run()
    
'''
using the following code in the terminal to make macOS application using pyinstaller

> pyinstaller main.py -w --onefile

'''