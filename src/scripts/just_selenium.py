from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import io

# Set up the webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
driver = webdriver.Chrome(options=options)

# Enter the webpage
url = 'https://authenticationtest.com'
driver.get(url)

# Click on the element
element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Simple Form Auth")]'))
)
print("ELEMENT: ", element.location)
location = element.location
size = element.size
# element.click()
element.send_keys("")
# Get the screenshot of the element
location = element.location
size = element.size
print('TYPE IS. ', element.tag_name)
driver.save_screenshot('screenshot_just_sel.png')

# Crop the screenshot to get the graphic representation
x = location['x']
y = location['y']
w = size['width']
h = size['height']
image = Image.open('screenshot_just_sel.png')
image = image.crop((x, y, x + w, y + h))
image.save('graphic_representation.png')

# Close the webdriver
driver.quit()