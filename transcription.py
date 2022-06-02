



from tkinter import Button

from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

class transcription(GridLayout):
        et = StringProperty("the text entered will also appear here")
        s = StringProperty("default")
        def damn(self, widget):
                self.et = widget.text
        def transcripteur(self,f):
                import speech_recognition as sr
                r = sr.Recognizer()
                #n = input("donner ou trouve le fichier wav ou flac")
                anas = sr.AudioFile(f)
                with anas as source:
                        audio = r.record(source)

                text = r.recognize_google(audio, show_all=True)

                print("in the try block")
                self.s = str(text)

                print(self.s)







class transcriptionApp(App):
        pass

transcriptionApp().run()