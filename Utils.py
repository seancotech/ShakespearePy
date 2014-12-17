from threading import Thread
from xml.dom import minidom
from xml.etree import cElementTree
from Queue import Queue

def loadFile(filename):
    """Loads the input file into a string."""

    file = open(filename, 'r')
    output = file.read()
    file.close()

    return output

