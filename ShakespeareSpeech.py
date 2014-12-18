class ShakespeareSpeech(object):
    """A ShakespeareSpeech object holds information about all relevant metadata regarding a given speech."""

    def __init__(self, play, speaker, speech):
        self.play = play
        self.speaker = speaker
        self.speech = speech

    def getPlay(self):
        return self.play

    def getSpeaker(self):
        return self.speaker

    def getSpeech(self):
        return self.speech
