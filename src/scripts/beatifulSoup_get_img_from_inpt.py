import requests
from bs4 import BeautifulSoup

url = 'https://authenticationtest.com/simpleFormAuth/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the input element with the image
input_element = soup.find('input', {'class': 'form-control'})

# Get the image URL from the input element
image_url = input_element['src']

# Download the image
image_response = requests.get(image_url)

# Save the image to a file
with open('image.jpg', 'wb') as file:
    file.write(image_response.content)