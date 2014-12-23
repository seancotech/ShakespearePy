# Libraries
from os import path, getcwd
from sys import argv

# Local modules
from Newspeech import *
from Quotes import *
from Utils import *
from TTSpeaker import *

# Filepaths
SCRIPT_DIR = path.dirname(path.realpath(__file__))
NEW_SPEECH = path.join(SCRIPT_DIR, "Assets", "newspeech.xml")

# Command-line switches
SPEAK_LONG_SWITCH = "--speak"
SPEAK_SHORT_SWITCH = "-s"
QUIET_LONG_SWITCH = "--quiet"
QUIET_SHORT_SWITCH = "-q"

def main():
    quiet = False
    readQuote = False
    quote = ""
    speak = TTSpeaker()

    # Assumed everything after the script call is part of the quote
    # Search for the quote provided
    argv.remove(argv[0])

    if SPEAK_LONG_SWITCH in argv or SPEAK_SHORT_SWITCH in argv:
        readQuote = True
        if SPEAK_LONG_SWITCH in argv: argv.remove(SPEAK_LONG_SWITCH)
        if SPEAK_SHORT_SWITCH in argv: argv.remove(SPEAK_SHORT_SWITCH)
    
    if QUIET_LONG_SWITCH in argv or QUIET_SHORT_SWITCH in argv:
	quiet = True
	if QUIET_LONG_SWITCH in argv: argv.remove(QUIET_LONG_SWITCH)
	if QUIET_SHORT_SWITCH in argv: argv.remove(QUIET_SHORT_SWITCH)

 
    # Load XML into object from file
    if not quiet: print("Reading file...")
    xml = loadFile(NEW_SPEECH)
    newspeech = Newspeech(xml)
    if not quiet: print("Done reading!")
    if not quiet: print "" # Blank line   

    # Now, only thing left should be the quote
    if len(argv) >= 1:
        quote = ' '.join(argv)
    else:
        # No arguments given, so pick a random quote and search for it
        if not quiet: print("Run with no arguments given! Picking a random quote...")
        quote = getRandomQuote()

    if not quiet: print("Search string: " + quote)
    if not quiet: print "" # Blank line
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
