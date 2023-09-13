import cv2
import matplotlib
import pytesseract as tess
tess.pytesseract.tesseract_cmd= 'C:\Program Files\Tesseract-OCR\Tesseract.exe'
image= cv2.imread("pic1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
text= tess.image_to_string(image)
print(text)
cv2.imshow("image",gray)
cv2.waitKey(0)