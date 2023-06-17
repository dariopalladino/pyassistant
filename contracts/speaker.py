from abc import ABC, abstractmethod
from config.config import Config

class Speaker(ABC):
    
    @abstractmethod
    def speak(self, message) -> None:
        raise NotImplementedError("this is an abstract class")


    @abstractmethod
    def shutup(self) -> None:
        raise NotImplementedError("this is an abstract class")


class SpeakerManager(Speaker):
    def __init__(self, speaker: Speaker, debug: str = False) -> None:
        self.speaker = speaker(debug)
        self.debug = debug
        self.config = Config()
        if not self.debug: self.greet()

    def speak(self, message):
        if self.debug: print(f"SM-this is the message: {message}")
        self.speaker.speak(message)

    def shutup(self) -> None:
        self.speaker.shutup()
    
    def greet(self):
        gender = self.config.get('assistant.gender')
        print(f"Gender {gender}")
        name = self.config.get("assistant."+str(gender)+".name")
        self.speak(f"Hi, My name is {name} and I am here to assist you in any queries.")