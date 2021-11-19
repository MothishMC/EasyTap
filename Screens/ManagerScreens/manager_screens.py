from kivy.uix.screenmanager import ScreenManager
from Screens.CameraScreen.camera_screen import CameraScreen
from Screens.HomeScreen.home_screen import HomeScreen
from Screens.LoginScreen.login_screen import LoginScreen
from Screens.ToolScreen.tool_screen import ToolScreen


class ManagerScreens(ScreenManager):
    sm = ScreenManager()
    sm.add_widget(LoginScreen(name='log'))
    sm.add_widget(HomeScreen(name='home'))
    sm.add_widget(CameraScreen(name='cam'))
    sm.add_widget(ToolScreen(name='tool'))
