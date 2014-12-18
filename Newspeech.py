# Used to encode search returns
from ShakespeareSpeech import ShakespeareSpeech

# Tags to search for
PLAY_TAG = "<PLAY>"
SPEAKER_TAG = "<SPEAKER>"
SPEECH_TAG = "<SPEECH>"
OPEN_TAG = "<"
CLOSE_TAG = ">"

class Newspeech(object):
    """Stores an XML play or speech file."""

    def __init__(self, body):
        self.body = body

    def getSpeech(self, searchString):
        """Returns a ShakespeareSpeech object with the relevant speech 
        corresponding to the given search string."""

        index = -1

        try:
            index = self.getIndexIgnoreCase(searchString)
        except ValueError:
            # The string wasn't found in any play!
            return False

        play = self.backtrack(index, PLAY_TAG)
        speaker = self.backtrack(index, SPEAKER_TAG)
        speech = self.backtrackGetSpeech(index)

        # Return the speech and metadata in a new ShakespeareSpeech object for simplicity
        return ShakespeareSpeech(play, speaker, speech)

    def backtrack(self, index, tag):
        """Backtracks from the provided index until the given tag is encountered.
        Returns the text at that tag. For finding a speech body, use backtrackGetSpeech() instead."""

        # Split the body up to the index
        splitBody = self.body[0:index]

        # Find last index of open and close tags
        lastOpenTagIndex = splitBody.rfind(tag)
        # Start searching from after the ">" symbol of the tag
        startIndex = lastOpenTagIndex + len(tag)
        # Find the next tag, whatever it is - close tags can be AFTER the splitBody cutoff!
        nextOpenTagIndex = startIndex + (splitBody[startIndex:].index("<"))

        # Return contents
        return splitBody[startIndex:nextOpenTagIndex]

    def backtrackGetSpeech(self, index):
        """Backtracks from the provided speech index and returns the full speech."""

        startSpeechIndex = self.getPreviousIndex(self.body, CLOSE_TAG, index) + 1
        endSpeechIndex = self.getNextIndex(self.body, OPEN_TAG, index)

        return self.body[startSpeechIndex:endSpeechIndex]

    def getPreviousIndex(self, haystack, needle, index):
        """Returns the previous index of a substring ending at the current index in haystack."""

        return haystack.rfind(needle, 0, index)
        
    def getNextIndex(self, haystack, needle, index):
        """Returns the next index of a substring starting from the current index in haystack."""

        return haystack.find(needle, index + 1)

    def getIndexIgnoreCase(self, needle):
        """Expensive search to find the index of the needle in the body, ignoring case."""
        
        return self.body.lower().index(needle.lower())