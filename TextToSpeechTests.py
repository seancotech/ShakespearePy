import pyttsx
import random

phrases = ["To be or not to be", 
    "Hello, world", 
    "My kingdom for a horse"]

speechEngine = pyttsx.init()
speechEngine.setProperty("rate", 100)
voices = speechEngine.getProperty("voices")
for phrase in phrases:
    # Pick a random voice from those available
    speechEngine.setProperty("voice", random.choice(voices))
    speechEngine.say(phrase)

# Speak!
speechEngine.runAndWait()