#  import kivy 
import kivy

#  import App from kivy
from kivy.app import App

# import boxlayout
from kivy.uix.boxlayout import BoxLayout



# Create class that we pass the App
class RegistrationApp(App):
    def build(self):
        # window name
        self.title = "Registration Form"

        # define orientation, padding and spacing of the items in the form
        layout = BoxLayout(orientation='vertical', padding= 30, spacing= 10)

  