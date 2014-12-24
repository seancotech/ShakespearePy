from threading import Thread
from xml.dom import minidom
from xml.etree import cElementTree
from hashlib import md5
import pickle

from Queue import Queue


def loadFile(filename):
    """Loads the input file into a string."""

    file = open(filename, 'r')
    output = file.read()
    file.close()

    return output

def saveCache(filename, inputDict):
    """Saves a lookup-cache (as a dict) to a file."""

    with open(filename, "wb") as file:
        pickle.dump(inputDict, file, pickle.HIGHEST_PROTOCOL)

def loadCache(filename):
    """Loads a lookup-cache as a dict object."""
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except EOFError:
        # Cache is corrupted or empty, caller should handle
        return {};

def hashFile(filename):
    """Returns an MD5 hash of file contents."""

    return md5(open(filename).read()).hexdigest()

def checkHash(filename, hash):
    """Returns True if the MD5 hash of the file matches the provided MD5 hash."""

    return hashFile(filename) == hash