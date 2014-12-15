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

def readXMLFromFile(filepath, resultQueue):
    inputString = ""
    with open(filepath, "r") as inputFile:
        inputString = inputFile.read()

    # Return by putting the result in the queue
    resultQueue.put(cElementTree.fromstring(inputString))