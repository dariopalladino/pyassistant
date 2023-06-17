import time
from contracts.listener import ListenerManager
from contracts.speaker import SpeakerManager
from contracts.recorder import RecorderManager
from contracts.tssx3 import TTSX3
from contracts.gtts import gTTSX
from contracts.whisper import Whisper
from contracts.pyaudio import PyAudio
from contracts.gspeechrecognition import SRRecorder, SRListener
from contracts.chatgpt import chatGPT

DEBUG = True

def run(what: str):
    if what.lower() == "GOOGLE":
        speaker = SpeakerManager(gTTSX, DEBUG) # this doesn't work yet
        w = ListenerManager(SRListener, debug=DEBUG)
        audio = RecorderManager(SRRecorder, DEBUG)
    else:
        speaker = SpeakerManager(TTSX3, DEBUG)
        w = ListenerManager(Whisper, debug=DEBUG) # SRListener can be used
        audio = RecorderManager(PyAudio, debug=DEBUG) # if SRListener is used, SRRecorder is mandatory here and viceversa

    try:
        GPT = chatGPT(debug=True)
        while True:
            w.set(audio.record())
            w.decode()
            # speaker.speak(w.get())
            # call chatGPT to get an answer
            GPT.ask(w.get())
            speaker.speak(GPT.getResponse())

    except KeyboardInterrupt:
        audio.shutdown()
        speaker.shutup()


if __name__ == "__main__":
    run("TTSX")







