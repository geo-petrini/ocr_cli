import pytesseract
pytesseract.pytesseract.tesseract_cmd = './Tesseract-OCR/tesseract.exe'

print(pytesseract.get_languages(config=''))