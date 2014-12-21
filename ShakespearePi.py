# Libraries
from os import path, getcwd
from sys import argv

# Local modules
from Newspeech import *
from Quotes import *
from Utils import *
from TTSpeaker import *

# Filepaths
NEW_SPEECH = path.join(getcwd(), "Assets", "newspeech.xml")

# Command-line switches
SPEAK_LONG_SWITCH = "--speak"
SPEAK_SHORT_SWITCH = "-s"

def main():
    readQuote = False
    quote = ""
    speak = TTSpeaker()

    # 1. Load XML into object from file
    print("Reading file...")
    xml = loadFile(NEW_SPEECH)
    newspeech = Newspeech(xml)
    print("Done reading!")
    print "" # Blank line

    # Assumed everything after the script call is part of the quote
    # Search for the quote provided
    argv.remove(argv[0])

    if SPEAK_LONG_SWITCH in argv or SPEAK_SHORT_SWITCH in argv:
        readQuote = True
        if SPEAK_LONG_SWITCH in argv: argv.remove(SPEAK_LONG_SWITCH)
        if SPEAK_LONG_SWITCH in argv: argv.remove(SPEAK_SHORT_SWITCH)

    # Now, only thing left should be the quote
    if len(argv) >= 1:
        quote = ' '.join(argv)
    else:
        # No arguments given, so pick a random quote and search for it
        print("Run with no arguments given! Picking a random quote...")
        quote = getRandomQuote()

    print("Search string: " + quote)
    print "" # Blank line
    # Search for and display quote
    prettyPrintQuote(newspeech.getSpeech(quote))

    if readQuote:
        # Read it! (TTS)
        speak.readString(newspeech.getSpeech(quote).getSpeech())

def prettyPrintQuote(quoteObject):
    """Pretty-prints a provided ShakespeareQuote object."""
    try:
        print("PLAY: " + quoteObject.getPlay())
        print("SPEAKER: " + quoteObject.getSpeaker())
        print("SPEECH: " + quoteObject.getSpeech())
    except AttributeError:
        print("Quote not found!")        

# Run on startup
main()