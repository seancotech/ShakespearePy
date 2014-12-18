# External libraries
from random import choice
import pyttsx

class TTSpeaker(object):
    """A TTSpeaker utilizes the TTS libraries and APIs available on the local machine to read a given string."""

    def __init__(self):
        """Constructs a new TTSpeaker by randomly selecting an available voice and setting the rate to 150."""
        self.speechEngine = pyttsx.init()
        self.speechEngine.setProperty("voice", choice(self.speechEngine.getProperty("voices")))
        self.speechEngine.setProperty("rate", 150)

    def getSpeakers(self):
        """Returns a list of local speakers available for use."""

        return self.speechEngine.getProperty("voices")

    def setSpeaker(self, speaker):
        """Sets the speaker to use for reading."""

        self.speechEngine.setProperty("voice", speaker)
    
    def setRate(self, rate):
        """Sets the speech rate."""

        self.speechEngine.setProperty("rate", rate)

    def readString(self, string):
        """Reads the provided string with the currently configured speech options."""

        self.speechEngine.say(string)
        self.speechEngine.runAndWait()
