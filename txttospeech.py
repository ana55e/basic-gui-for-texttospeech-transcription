from tkinter import Button

from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
class txttospeech(GridLayout):
    ltx = StringProperty("the text entered will also appear here")
    gtx = StringProperty("the text entered will also appear here")
    ftx = StringProperty("the text entered will also appear here")
    def xfilepassing(self,widget):
        self.ltx=widget.text
    def xgenderpassing(self,widget):
        self.gtx=widget.text
    def xlaungpassing(self,widget):
        self.ftx=widget.text
    def texttosound3(self , text, gender, language):
        import pyttsx3
        engine = pyttsx3.init(driverName='sapi5')
        voice = engine.getProperty('voices')
        if (gender == "female"):
            engine.setProperty('voice', voice[1].id)
            if (language == "English (United States)"):
                voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                engine.setProperty('voice', voice_id)
                engine.say(text)
                engine.runAndWait()
            if (language == "French"):
                voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
                engine.setProperty('voice', voice_id)
                engine.say(text)
                engine.runAndWait()


        if (gender == "male"):
            engine.setProperty('voice', voice[0].id)
            if (language == "English (United States)"):
                voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                engine.setProperty('voice', voice_id)
                engine.say(text)
                engine.runAndWait()
            if (language == "French"):
                voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
                engine.setProperty('voice', voice_id)
                engine.say(text)
                engine.runAndWait()

class BasedApp(App):
    pass
BasedApp().run()