import pyaudio
import wave
import os
from contracts.recorder import Recorder

class PyAudio(Recorder):
    SECONDS = 10
    FRAMES = []
    FORMAT = pyaudio.paInt32
    def __init__(self, config: dict = {"format":FORMAT,
                                       "channels":1, 
                                       "rate":44100, 
                                       "input":True, 
                                       "frames_per_buffer":1024},
                        debug: bool = False
                ) -> None:        
        self.recorder = pyaudio.PyAudio() 
        self.debug = debug       
        self.counter = 0
        self.config = config
        self.open()

    def open(self) -> None:
        self.stream = self.recorder.open(
            format=self.config["format"], 
            channels=self.config["channels"], 
            rate=self.config["rate"], 
            input=self.config["input"], 
            frames_per_buffer=self.config["frames_per_buffer"]
        )

    def record(self) -> str:
        self.FRAMES.clear()
        self.counter += 1
        for i in range(0, int(self.config["rate"]/self.config["frames_per_buffer"] * self.SECONDS)):
            audio = self.stream.read(self.config["frames_per_buffer"])
            self.FRAMES.append(audio)
        
        filename = "temp_audio_"+str(self.counter)+".wav"
        while os.path.isfile(filename):
            self.counter += 1
            filename = "temp_audio_"+str(self.counter)+".wav"

        wav = wave.open(filename, "wb")
        wav.setnchannels(1)
        wav.setsampwidth(pyaudio.get_sample_size(self.FORMAT))
        wav.setframerate(44100)
        wav.writeframes(b''.join(self.FRAMES))
        wav.close
        if self.debug: print(f"This is the file path: {filename}")
        return filename
    
    def shutdown(self):
        self.stream.stop_stream()
        self.stream.close()
        self.recorder.terminate()
        