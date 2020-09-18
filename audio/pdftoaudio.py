
import pyttsx3
import PyPDF2

book_name = open('sample.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book_name)
pages = pdf_reader.numPages

play = pyttsx3.init()
play.setProperty('volume', 0.9)
play.setProperty('rate', 120)
print('playing')

for num in range(0, pages):
    page = pdf_reader.getPage(num)
    text = page.extractText()
    play.say(text)
    play.runAndWait()


1


# import pyttsx3
# import PyPDF2

# book_name = open('sample.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(book_name)
# pages = pdf_reader.numPages

# play = pyttsx3.init()
# play.setProperty('volume', 0.9)
# play.setProperty('rate', 120)
# print('playing....')

# for num in range(0, pages):
#     page = pdf_reader.getPage(num)
#     text = page.extractText()
#     play.say(text)
#     play.runAndWait()


# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Omkar is my boss he is so great i have no words to describe it")
# engine.setProperty('rate', 120)  # 120 words per minute
# engine.setProperty('volume', 0.9)
# engine.runAndWait()
