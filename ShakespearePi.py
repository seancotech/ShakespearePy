# Libraries
from os import path, getcwd

# Local modules
from Quotes import *
from Utils import *

# Filepaths
NEW_SPEECH = path.join(getcwd(), "Assets", "newspeech.xml")

def main():
    print "Reading XML into file..."
    xml = readXMLAsync(NEW_SPEECH)
    print "Done reading XML!"

# Run on startup
main()