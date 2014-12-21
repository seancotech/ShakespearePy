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

    if (len(argv) < 2 or len(argv) is 3 and (argv[1] is SPEAK_LONG_SWITCH or argv[1] is SPEAK_SHORT_SWITCH)):
        # No arguments given, so pick a random quote and search for it
        print("Run with no arguments given! Picking a random quote...")
        quote = getRandomQuote()

    else:
        # Assumed everything after the script call is part of the quote
        # Search for the quote provided
        for word in argv:
            if argv.index(word) != 0:
                if word is SPEAK_LONG_SWITCH or word is SPEAK_SHORT_SWITCH:
                    # We should read the quote!
                    readQuote = True
                else:
                    quote += word + " "

    quote = quote[0:len(quote) - 2] # Trim last space
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