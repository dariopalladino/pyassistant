from abc import ABC, abstractmethod
import os

class Listener(ABC):

    @abstractmethod    
    def set(self, audio) -> None:
        raise NotImplementedError("this is an abstract class")

    @abstractmethod
    def decode(self) -> None:
        raise NotImplementedError("this is an abstract class")

    @abstractmethod
    def get(self) -> str:
        raise NotImplementedError("this is an abstract class")


class ListenerManager(Listener):
    def __init__(self, listener: Listener, debug: str = False) -> None:
        self.debug = debug
        self.listener = listener()
        if self.debug: print(f"This is the Listener instance: {self.listener}")

    def set(self, audio: str):
        if self.debug: print(f"This is the stream: {audio}")
        # assert audio is str, "Audio must be a file path. None given!"        
        self.listener.set(audio)

    # @dispatchmethod
    # def set(self, audio: sr.AudioData):
    #     import speech_recognition as sr
    #     if self.debug: print(f"This is the stream: {audio}")
    #     assert audio is sr.AudioData, "Audio must be a stream of AudioData (SR). None given!"
    #     self.listener.set(audio)

    def get(self):
        return self.listener.get()
    
    def decode(self):
        self.listener.decode()

