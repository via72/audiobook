import pyttsx3
import PyPDF2
book = open('oop.pdf', 'rb')  # storing as a binary book
pdfReader = PyPDF2.PdfFileReader(book)  # reading the book
pages = pdfReader.numPages  # counting the total number of pages in the book
print(pages)
speaker = pyttsx3.init()  # object creation
speaker.say("A very good afternoon Sir . Welcome to our audio book project")  # greetings
for num in range(7, pages):
    page = pdfReader.getPage(num)  # getting a particular page
    text = page.extractText()  # extracting text from that particular page

    """RATE"""
    rate = speaker.getProperty('rate')  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    speaker.setProperty('rate', 125)  # setting up new voice rate

    """VOLUME"""
    volume = speaker.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    print(volume)  # printing current volume level
    speaker.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

    """VOICE"""
    voices = speaker.getProperty('voices')  # getting details of the current voice
    print(voices)
    speaker.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

    speaker.say(text)
    speaker.runAndWait()