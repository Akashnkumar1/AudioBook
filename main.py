import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename
book = askopenfilename(initialdir='.')
speech = pyttsx3.init()
pdfRead = PyPDF2.PdfFileReader(book)
total_page = pdfRead.getNumPages()
speech.say("Total Number of Page is")
speech.say(total_page)
speech.say("Enter the page number")
read_page = int(input("Enter the page number: "))
for num in range(read_page, total_page):
    page = pdfRead.getPage(read_page)
    text = page.extractText()
    speech.say(text)
    speech.runAndWait()
