import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the webpage
url = "https://authenticationtest.com/"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the element by its ID
element = soup.find("a", {"class": "btn btn-primary"})

# Extract the element and its contents
print(element.text)