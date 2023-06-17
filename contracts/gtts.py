from gtts import gTTS
from io import BytesIO
from contracts.speaker import Speaker
from playsound import playsound
from tempfile import NamedTemporaryFile

class gTTSX(Speaker):
    def __init__(self, debug: str = False) -> None:
        self.debug = debug
        self.mp3fp = BytesIO()
        
    
    def speak(self, message ) -> None:
        lang: str = 'com'
        # with BytesIO() as f:
        with self.mp3fp as f:
            self.gtts = gTTS(message, lang)
            self.gtts.write_to_fp(f)
            f.seek(0)
    
    def shutup(self) -> None:
        pass
        
    