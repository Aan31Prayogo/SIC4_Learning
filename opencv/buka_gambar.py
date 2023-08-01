#import library
import cv2

#muat file dan ekxtensi file
image_name = "python_logo.png"

#membaca image atau gambar
image = cv2.imread(image_name)
print(image)
print(type(image))

#menampilkan image
cv2.imshow("python tes", image)
cv2.waitKey(0)

cv2.destroyAllWindows()