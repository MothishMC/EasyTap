import os

from kaki.app import App
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.factory import Factory

Screen

class Live(App, MDApp):
    KV_FILES = [
        os.path.join(os.getcwd(), "Screens", "ManagerScreens", "manager_screens.kv"),
        os.path.join(os.getcwd(), "Screens", "LoginScreen", "login_screen.kv"),
        os.path.join(os.getcwd(), "Screens", "HomeScreen", "home_screen.kv"),
        os.path.join(os.getcwd(), "Screens", "HomeScreen", "Components", "cards.kv"),
        os.path.join(os.getcwd(), "Screens", "CameraScreen", "camera_screen.kv"),
        os.path.join(os.getcwd(), "Screens", "ToolScreen", "tool_screen.kv"),
    ]

    CLASSES = {
        'ManagerScreens': "Screens.ManagerScreens.manager_screens",
        'LoginScreen': "Screens.LoginScreen.login_screen",
        'HomeScreen': "Screens.HomeScreen.home_screen",
        'Cards': "Screens.HomeScreen.Components.cards",
        'CameraScreen': "Screens.CameraScreen.camera_screen",
        'ToolScreen': "Screens.ToolScreen.tool_screen",
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):
        self.theme_cls.primary_palette = "Brown"
        return Factory.ManagerScreens()


Live().run()
