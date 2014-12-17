from ShakespeareSpeech import ShakespeareSpeech
from threading import Thread
from xml.dom import minidom
from xml.etree import cElementTree
from Queue import Queue

def readXMLAsync(filepath):
    """Given a path to an XML file, reads the contents asyncronously to a cElementTree object."""

    # Thread-safe queue to get result
    asyncResult = Queue()
    readThread = Thread(target = readXMLFromFile, args = (filepath, asyncResult), kwargs = {})
    readThread.start()
    readThread.join()

    # Done!
    return asyncResult.get()

def processXMLToSpeechList(root):
    """Processes a cElementTree object and returns a list of ShakespeareSpeech objects."""
    output = []
    # Given that the structure will be...
    # <PLAY>PLAY_NAME
    # <ACT>
    # <SCENE>
    # <SPEECH>
    # <SPEAKER>SPEAKER_NAME</SPEAKER>
    # SPEECH_BODY</SPEECH>

    # So, let's do a pre-order traversal over the XML parse tree to populate the list
    for play in root:
        currentPlay = play.text
        currentAct = 0
        for act in play:
            currentAct += 1
            currentScene = 0
            for scene in act:
                currentScene += 1
                for speech in scene:
                    speakers = speech[0].text
                    speechText = speech[1].text
                    output.append(ShakespeareSpeech(currentPlay, currentAct, currentScene, speakers, speechText))
    return output

def readXMLFromFile(filepath, resultQueue):
    inputString = ""
    with open(filepath, "r") as inputFile:
        inputString = inputFile.read()

    # Return by putting the result in the queue
    resultQueue.put(cElementTree.fromstring(inputString))