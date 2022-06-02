from tkinter import Button

from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

class filetospeech(GridLayout):
    lt = StringProperty("the text entered will also appear here")
    gt = StringProperty("the text entered will also appear here")
    ft = StringProperty("the text entered will also appear here")
    def filepassing(self,widget):
        self.lt=widget.text
    def genderpassing(self,widget):
        self.gt=widget.text
    def laungpassing(self,widget):
        self.ft=widget.text
    def filetosound3(self,text, gender, language):
        import pyttsx3
        engine = pyttsx3.init(driverName='sapi5')
        voice = engine.getProperty('voices')
        if (gender == "female"):
            engine.setProperty('voice', voice[1].id)
            if (language == "English (United States)"):
                voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                engine.setProperty('voice', voice_id)
                infile = text
                f = open(infile, 'r')
                theText = f.read()
                f.close()
                engine.say(theText)
                engine.runAndWait()
            if (language == "French"):
                voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
                engine.setProperty('voice', voice_id)
                infile = text
                f = open(infile, 'r')
                theText = f.read()
                f.close()
                engine.say(theText)
                engine.runAndWait()

        if (gender == "male"):
            engine.setProperty('voice', voice[0].id)
            if (language == "English (United States)"):
                voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                engine.setProperty('voice', voice_id)
                infile = text
                f = open(infile, 'r')
                theText = f.read()
                f.close()
                engine.say(theText)
                engine.runAndWait()
            if (language == "French"):
                voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
                engine.setProperty('voice', voice_id)
                infile = text
                f = open(infile, 'r')
                theText = f.read()
                f.close()
                engine.say(theText)
                engine.runAndWait()
class BasedApp(App):
    pass
BasedApp().run()