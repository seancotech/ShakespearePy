# Libraries
from os import path, getcwd

# Local modules
from Quotes import *
from Utils import *

# Filepaths
NEW_SPEECH = path.join(getcwd(), "Assets", "newspeech.xml")

def main():
    # 1. Load XML into object from file
    print "Reading file..."
    xml = loadFile(NEW_SPEECH)
    print "Done reading!"

# Run on startup
main()