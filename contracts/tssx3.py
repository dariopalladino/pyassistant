import pyttsx3
from contracts.speaker import Speaker
from config.config import Config

class TTSX3(Speaker):
    def __init__(self, debug: str = False) -> None:
        self.debug = debug
        self.config = Config()
        self.ttsx3 = pyttsx3.init(driverName=self.config.get('ttsx3.driverName'),debug=True)
        self.setProperties()
    
    def speak(self, message) -> None:
        if self.debug: print(f"TT-this is the message: {message}")        
        self.ttsx3.say(message)
        self.ttsx3.runAndWait()

    def setProperties(self) -> None:
        # rate = self.ttsx3.getProperty('rate')
        self.ttsx3.setProperty('rate', 125)
        # volume = self.ttsx3.getProperty('volume')
        self.ttsx3.setProperty('volume', 0.8)
        # self.ttsx3.setProperty('voice', 0)
        # rate = self.ttsx3.getProperty('rate')
        # volume = self.ttsx3.getProperty('volume')
        # voice = self.ttsx3.getProperty('voice')
        if self.debug: print(f"TT-rate: {self.ttsx3.getProperty('rate')}")
        if self.debug: print(f"TT-volume: {self.ttsx3.getProperty('volume')}")
        # if self.debug: print(f"TT-voice: {voice[1].id}")

    def shutup(self) -> None:
        return self.ttsx3.stop()
