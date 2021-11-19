from kivy.properties import StringProperty
from kivymd.uix.card import MDCard


class Cards(MDCard):
    source = StringProperty()
    text = StringProperty()