# Libraries
from os import path, getcwd
from sys import argv

# Local modules
from Newspeech import *
from Quotes import *
from Utils import *

# Filepaths
SCRIPT_DIR = path.dirname(path.realpath(__file__))
NEW_SPEECH = path.join(SCRIPT_DIR, "Assets", "newspeech.xml")
CACHE_FILE = path.join(SCRIPT_DIR, "cache.pkl")

# Command-line switches
SPEAK_LONG_SWITCH = "--speak"
SPEAK_SHORT_SWITCH = "-s"
QUIET_LONG_SWITCH = "--quiet"
QUIET_SHORT_SWITCH = "-q"
NOCACHE_LONG_SWITCH = "--no-cache"
NOCACHE_SHORT_SWITCH = "-n"

def main():
    # Command-line switch bools
    readQuote, quiet, noCache = False, False, False

    quote, output, index = "", "", -1

    # Assumed everything after the script call is part of the quote
    # Search for the quote provided
    argv.remove(argv[0])

    # Handle command-line arguments
    if SPEAK_LONG_SWITCH in argv or SPEAK_SHORT_SWITCH in argv:
        readQuote = True
        if SPEAK_LONG_SWITCH in argv: argv.remove(SPEAK_LONG_SWITCH)
        if SPEAK_SHORT_SWITCH in argv: argv.remove(SPEAK_SHORT_SWITCH)
    
    if QUIET_LONG_SWITCH in argv or QUIET_SHORT_SWITCH in argv:
        quiet = True
        if QUIET_LONG_SWITCH in argv: argv.remove(QUIET_LONG_SWITCH)
        if QUIET_SHORT_SWITCH in argv: argv.remove(QUIET_SHORT_SWITCH)

    if NOCACHE_LONG_SWITCH in argv or NOCACHE_SHORT_SWITCH in argv:
        noCache = True
        if NOCACHE_LONG_SWITCH in argv: argv.remove(NOCACHE_LONG_SWITCH)
        if NOCACHE_SHORT_SWITCH in argv: argv.remove(NOCACHE_SHORT_SWITCH)
 
    # Load XML into object from file
    if not quiet: print("Reading file...")
    xml = loadFile(NEW_SPEECH)
    newspeech = Newspeech(xml)
    if not quiet: print("Done reading!")
    
    # Load cache into dictionary if exists
    cache = {}
    if not noCache:
        if path.exists(CACHE_FILE):
            if not quiet: print("Found cache! Loading cached lookups...")
            cache = loadCache(CACHE_FILE)
            if not checkHash(NEW_SPEECH, cache["hash"] if "hash" in cache else ""):
                # File hashes do not match! Invalidate cache and create new one
                if not quiet: print("Hash mismatch! Invalidating and regenerating cache.")
                cache["hash"] = hashFile(NEW_SPEECH)
            else:
                # Cache is all good!
                if not quiet: print("Cache good to go!")
        else:
            if not quiet: print("Cache doesn't exist! Creating...")
            cache["hash"] = hashFile(NEW_SPEECH)

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

    if len(quote) <= 4:
        print("Please enter a quote longer than 4 characters!")
    else:
        # Search for and display quote
        index = cache[quote] if quote in cache else -1
	output, index = newspeech.getSpeech(quote, index)
        prettyPrintQuote(output)

    if readQuote:
        # Read it! (TTS)
        from TTSpeaker import TTSpeaker
        speak = TTSpeaker()

        speak.readString(output.getSpeech())

    # Save results to cache
    if not noCache:
        if not quiet: print ""
        if not quiet: print("Writing to cache...")
        cache[quote] = index
        saveCache(CACHE_FILE, cache)

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
