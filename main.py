import pyttsx3
import PyPDF2
speech = pyttsx3.init()
book = open('Read.pdf','rb')
pdfRead = PyPDF2.PdfFileReader(book)
numofpage = pdfRead.getNumPages()
speech.say("Total Number of Page is")
speech.say(numofpage)
speech.say("Enter the page number")
readatpage = int(input("Enter the page number: "))
for num in range(readatpage, numofpage):
    page = pdfRead.getPage(readatpage)
    text = page.extractText()
    speech.say(text)
    speech.runAndWait()
