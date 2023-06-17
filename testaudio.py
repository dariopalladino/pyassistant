import pyaudio
from contracts.recorder import Recorder
from contracts.listener import ListenerManager
from contracts.whisper import Whisper
from contracts.speaker import SpeakerManager
from contracts.tssx3 import TTSX3
from contracts.chatgpt import chatGPT
        
import os
import time

def run():
    w = ListenerManager(Whisper, True)
    speaker = SpeakerManager(TTSX3, True)
    counter = 0
    try: 
        counter += 4
        filename = "temp_audio_"+str(counter)+".wav"
        while os.path.isfile(filename):
            print(filename)
            
            w.set(os.path.join(os.getcwd(), filename))
            w.decode()
            # speaker.speak(w.get())
            GPT = chatGPT(w.get(), debug=True)
            speaker.speak(GPT.getResponse())


            counter += 1
            filename = "temp_audio_"+str(counter)+".wav"

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    run()

