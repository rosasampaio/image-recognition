import cv2
image = cv2.imread('image_path/image_name.jpg')
x, y, w, h = 100, 100, 300, 300
cropped_image = image[y:y+h, x:x+w]

cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('cropped_image.jpg', cropped_image)