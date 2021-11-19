from kivy.properties import BooleanProperty
from kivymd.uix.screen import MDScreen


class HomeScreen(MDScreen):
    data = {
        "Gallery": "folder-multiple-image",
        "Camera": "camera"
    }

    def callback(self, instance):
        if instance.icon == "camera":
            print("You pressed camera icon")
        elif instance.icon == "folder-multiple-image":
            print("You pressed gallery icon")
        else:
            print("")



