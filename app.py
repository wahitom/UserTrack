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

#  import validate_email
from validate_email import validate_email

# import zxcvbn for password validation
from zxcvbn import zxcvbn

# import os 
import os

# Create class that we pass the App
class RegistrationApp(App):
    def build(self):
        # window name
        self.title = "Registration Form"

        # define orientation, padding and spacing of the items in the form
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)

        #  add header and properties
        head_label = Label(text="Python User Registration App", font_size=26, bold=True, height=40)

        # labels for the inputs
        name_label = Label(text="User Name", font_size=18)
        self.name_input = TextInput(multiline=False, font_size=18)

        email_label = Label(text="User Email", font_size=18)
        self.email_input = TextInput(multiline=False, font_size=18)

        # use password=True to indicate that this text area holds special characters
        password_label = Label(text="User Password", font_size=18)
        self.password_input = TextInput(multiline=False, font_size=18, password=True)

        confirm_password_label = Label(text="Confirm User Password", font_size=18)
        self.confirm_password_input = TextInput(multiline=False, font_size=18, password=True)

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

    # validate password function
    def validate_password(self, password):
        result = zxcvbn(password)
        if result["score"] < 3:
            return False
        return True

    # check if email already exists
    def email_exists(self, email):
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                for line in file:
                    if "Email:" in line and email in line:
                        return True
        return False

    # define a function to register the user
    def register(self, instance):
        # Get the values form the input
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text
        confirm_password = self.confirm_password_input.text

        # validate email using validate_email function
        is_valid = validate_email(email)

        # some validations 
        # 1. if inputs are empty
        if name.strip() == '' or email.strip() == '' or password.strip() == '' or confirm_password.strip() == '':
            message = "Please fill all the fields"

        # 2. check if the password and confirm password are the same
        elif password != confirm_password:
            message = "Passwords do not match"

        # 3. check if email is valid
        elif not is_valid:
            message = "Please enter a valid email"

        # 4. check if password is valid
        elif not self.validate_password(password):
            message = "Password must be stronger.\nTry adding more characters or symbols."

        # 5. check if email already exists
        elif self.email_exists(email):
            message = "This email is already registered.\nPlease use a different email."

        # save user data inside a text file
        else:
            with open("users.txt", "a") as file:
                file.write('Name:{}\n'.format(name))
                file.write('Email:{}\n'.format(email))
                file.write('Password:{}\n'.format(password))
                file.write('---\n')  # Add a separator between users

            message = "Registration Successful\nName: {}\nEmail: {}".format(name, email)

        # create popup for message 
        popup = Popup(title="Registration Status", content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

# call our class and run it 
if __name__ == "__main__":
    RegistrationApp().run()
