from PIL import Image
import pytesseract

# Open an image file
img = Image.open('pic1.jpg')

# Perform OCR
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)
