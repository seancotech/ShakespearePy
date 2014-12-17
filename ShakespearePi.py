# Libraries
from os import path, getcwd

# Local modules
from Quotes import *
from Utils import *

# Filepaths
NEW_SPEECH = path.join(getcwd(), "Assets", "newspeech.xml")

def main():
    # 1. Load XML into object from file
    print "Reading XML into file..."
    xml = readXMLAsync(NEW_SPEECH)
    print "Done reading XML!"
    # 2. Parse the XML tree into ShakespeareSpeech objects
    print "Parsing XML..."
    speechList = processXMLToSpeechList(xml)
    print "Done parsing XML!"

# Run on startup
main()