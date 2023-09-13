import cv2
import matplotlib
import pytesseract as tess
import pytesseract.pytesseract

tess.pytesseract.tesseract_cmd= 'c:\\users\\chand\\anaconda3\\lib\\site-packages'
image= cv2.imread("pic1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# t_img = cv2.Canny(image, 30, 200)
# image= cv2.imread("mg.jpg",0)
# ret,t_img= cv2.threshold(gray,150,200,cv2.THRESH_BINARY)
# ret, thresh = cv2.threshold(gray, 127, 255, 0)
# thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# t_img = cv2.dilate(thresh, kernel)

# t_img = cv2.GaussianBlur(thresh, (5, 5), 0)

# contours, hierarchy = cv2.findContours(gray,
#     cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# # filtered contours
# filtered_contours = []
# for contour in contours:
#     area = cv2.contourArea(contour)
#     if area > 100:
#         filtered_contours.append(contour)

# cv2.drawContours(image, filtered_contours, -1, (0, 255, 0), 3)
cv2.imshow("image", thresh)
# cv2.getStructuringElement(1,200,1)
text = tess.image_to_string(thresh)
print(text)
cv2.waitKey(0)