import speech_recognition as sr
from random import choice
from contracts.listener import Listener
from contracts.recorder import Recorder
from config.config import Config
from contracts.exceptions import MicrophoneNotFoundError

class SRRecorder(Recorder):
    def __init__(self, debug: bool = False) -> None:
        self.debug = debug
        self.open()

    def open(self):
        self.sr = sr.Recognizer()

    def record(self):
        try:
            with sr.Microphone() as source:
                if self.debug: print('Listening...')
                self.sr.pause_threshold = 1
                audio = self.sr.listen(source)
                if self.debug: print(f"This is the audio: {audio}")
                return audio
        except:
            raise MicrophoneNotFoundError()

    def shutdown(self):
        pass


class SRListener(Listener):
    def __init__(self,  debug: str = False) -> None:
        self.config = Config()
        self.debug = debug
        self.sr = sr.Recognizer()

    def set(self, audio: sr.AudioData = None):
        self.audio = audio

    def get(self):
        return self.message

    def decode(self):
        self.message = self.sr.recognize_google(self.audio)