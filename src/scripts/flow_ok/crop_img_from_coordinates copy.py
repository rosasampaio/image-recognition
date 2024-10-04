import requests
from bs4 import BeautifulSoup
import cv2

url = 'https://www.example.com/image.jpg'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
image_url = soup.find('img')['src']

image_response = requests.get(image_url)
with open('image.jpg', 'wb') as file:
    file.write(image_response.content)

image = cv2.imread('image.jpg')
x, y, w, h = 100, 100, 300, 300
cropped_image = image[y:y+h, x:x+w]
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('cropped_image.jpg', cropped_image)