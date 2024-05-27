#  import kivy 
import kivy

#  import App from kivy
from kivy.app import App

# import boxlayout
from kivy.uix.boxlayout import BoxLayout

# import label to use as header
from kivy.uix.label import Label

# import textinput for the inputs
from kivy.uix.textinput import TextInput

# import Button
from kivy.uix.button import Button

#  import popup
from kivy.uix.popup import Popup



# Create class that we pass the App
class RegistrationApp(App):
    def build(self):
        # window name
        self.title = "Registration Form"

        # define orientation, padding and spacing of the items in the form
        layout = BoxLayout(orientation='vertical', padding= 30, spacing= 10)

        #  add header and properties
        head_label = Label(text="Python User Registration App", font_size=26, bold=True, height=40)

        # labels for the inputs
        name_label = Label(text="User Name", font_size=18)
        self.name_input = TextInput(multiline =False, font_size=18)

        email_label = Label(text="User Email", font_size=18)
        self.email_input = TextInput(multiline =False, font_size=18)

        # use password=True to indicate that this text area holds special characters
        password_label = Label(text="User Password", font_size=18)
        self.password_input = TextInput(multiline =False, font_size=18, password=True)

        confirm_password_label = Label(text="Confirm User Password", font_size=18)
        self.confirm_password_input = TextInput(multiline =False, font_size=18, password=True)

        # Create the registration button
        submit_button = Button(text="Register", font_size=18, on_press=self.register)



        # wrap our properties in a layout function so that they are visible
        layout.add_widget(head_label)

        layout.add_widget(name_label)
        layout.add_widget(self.name_input)

        layout.add_widget(email_label)
        layout.add_widget(self.email_input)

        layout.add_widget(password_label)
        layout.add_widget(self.password_input)

        layout.add_widget(confirm_password_label)
        layout.add_widget(self.confirm_password_input)

        layout.add_widget(submit_button)

        return layout
    
  



# call our class and run it 
if __name__ == "__main__":
    RegistrationApp().run()
