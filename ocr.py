
from PIL import Image
import pytesseract
from printer import pr

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'



def getText(filePath):
    rawText =  pytesseract.image_to_string(Image.open(filePath))
    text = rawText.replace("\n", " ")
    return text

if __name__ == '__main__':

    print(getText('./rawDocuments/passport.jpg'))