#import library
import cv2

image_name = "python_logo.png"
image = cv2.imread(image_name)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#fungsi untuk mengubah ukuran dari gambar 
gray_image = cv2.resize(gray_image,(320,320))
image = cv2.resize(image, (320,320))

cv2.imshow("original image",image)
cv2.imshow("gray image", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()