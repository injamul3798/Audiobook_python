#import the library
import pyttsx3
"""pyttsx3 is a text-to-speech conversion
 library in Python. """
#Now open the text file to read
file = open(r"test.txt")

#read line
book_text=file.readlines()
# init function to get an engine instance
# for the speech synthesis
engine = pyttsx3.init()

for i in book_text:
    engine.say(i)
    engine.runAndWait()
 