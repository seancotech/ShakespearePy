class ShakespeareSpeech(object):
    """A ShakespeareSpeech object holds information about all relevant metadata regarding a given speech."""

    def __init__(self, play, act, scene, speaker, speech):
        self.play = play
        self.act = act
        self.scene = scene
        self.speaker = speaker
        self.speech = speech

    def getPlay(self):
        return self.play

    def getAct(self):
        return self.act

    def getScene(self):
        return self.scene

    def getSpeaker(self):
        return self.speaker

    def getSpeech(self):
        return self.speech


