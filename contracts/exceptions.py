

class NoSpeakerException(Exception):
    def __init__(self, message = "No Speaker available") -> None:
        self.message = message
        super().__init__(self.message)

    # def __str__(self) -> str:
    #     return super().__str__(self.filename)

class MicrophoneNotFoundError(Exception):
    def __init__(self, message = "No Microphone available") -> None:
        self.message = message
        super().__init__(self.message)
