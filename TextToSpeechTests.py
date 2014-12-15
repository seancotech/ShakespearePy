import pyttsx
import random
from Quotes import getRandomQuote

numQuotes = 20
speechEngine = pyttsx.init()
speechEngine.setProperty("rate", 100)
voices = speechEngine.getProperty("voices")
for count in range(0, numQuotes):
    # Pick a random voice from those available
    speechEngine.setProperty("voice", random.choice(voices))
    speechEngine.say(getRandomQuote())

# Speak!
speechEngine.runAndWait()