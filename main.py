import PyPDF2
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Optional: change voice or speed
engine.setProperty('rate', 160)   # Speed of speech

# Open PDF file
pdf_file = open('positivethoughts.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

print(f"Total Pages: {len(pdf_reader.pages)}")

# Read each page
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()

    if text:
        engine.say(text)
        engine.runAndWait()

pdf_file.close()
