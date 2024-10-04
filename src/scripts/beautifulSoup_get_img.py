import requests
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import cv2

url = 'https://authenticationtest.com/'
response = requests.get(url)
soup = BeautifulSoup(
    UnicodeDammit(
        response.content
    ).unicode_markup,
    "html.parser")

image_url = soup.find('img')['src']

image_response = requests.get(image_url)
with open('favicon.png', 'wb') as file:
    file.write(image_response.content)

image = cv2.imread('favicon.png')
x, y, w, h = 100, 100, 300, 300
cropped_image = image[y:y+h, x:x+w]
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('cropped_image.jpg', cropped_image)
