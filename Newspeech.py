# Used to encode search returns
from ShakespeareSpeech import ShakespeareSpeech

class Newspeech(object):
    """Stores an XML play or speech file."""

    def __init__(self, body):
        self.body = body

    def getSpeech(searchString):
        """Returns a ShakespeareSpeech object with the relevant speech 
        corresponding to the given search string."""


    def backtrack(index, tag):
        """Backtracks from the provided index until the given tag is encountered.
        Returns the text at that tag."""

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


