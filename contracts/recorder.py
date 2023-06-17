from abc import ABC, abstractmethod

class Recorder(ABC):
    @abstractmethod
    def open(self):
        raise NotImplementedError("this is an abstract class")

    @abstractmethod
    def record(self):
        raise NotImplementedError("this is an abstract class")

    @abstractmethod
    def shutdown(self):
        raise NotImplementedError("this is an abstract class")

class RecorderManager(Recorder):
    def __init__(self, recorder: Recorder, debug: bool = False) -> None:
        self.debug = debug
        self.recorder = recorder(debug=debug)
        if self.debug: print(f"This is the Recorder instance: {self.recorder}")

    def open(self):
        self.recorder.open()
    
    def record(self):
        if self.debug: print(f"method-This is the Recorder instance: {self.recorder}")
        return self.recorder.record()        
    
    def shutdown(self):
        self.recorder.shutdown()
    
