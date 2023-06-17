import os
import whisper
from contracts.listener import Listener
from config.config import Config

class Whisper(Listener):
    def __init__(self,  debug: str = False) -> None:
        self.config = Config()
        self.debug = debug
        model_size = self.config.get("whisper.model_size")
        if self.debug: print(f"Model size detected: {model_size}")
        self.model = whisper.load_model(model_size)

    def set(self, audio: os.path = None) -> None:
        if not os.path.exists(audio):
            raise FileNotFoundError()
        self.set_audio(audio)
        self.log_mel()
        if self.debug: self.detect_language() 

    def set_audio(self, audio) -> None:
        self.audio = whisper.load_audio(audio)
        self.audio = whisper.pad_or_trim(self.audio)

    def log_mel(self) -> None:
        self.mel = whisper.log_mel_spectrogram(self.audio).to(self.model.device)

    def detect_language(self) -> None:
        _, probs = self.model.detect_language(self.mel)
        print(f"{str(max(probs, key=probs.get)).upper()} is the language detected")

    def decode_audio(self):
        options = whisper.DecodingOptions(fp16 = False) #fp32=True
        return whisper.decode(self.model, self.mel, options)
    
    def decode(self) -> None:
        self.decoded_result = self.decode_audio()

    def get(self):
        return self.decoded_result.text
