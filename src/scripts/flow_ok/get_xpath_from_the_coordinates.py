from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")

# Create a new instance of the ActionChains class
actions = ActionChains(driver)

# Move to the element at the specified coordinates
actions.move_by_offset(100, 100).perform()

# Get the element at the current mouse position
element = driver.switch_to.active_element

# Get the XPath of the element
xpath = element.get_attribute("xpath")

print(xpath)


# xpath = f"//*[@x='{location.x}' and @y='{location.y}']"

# print(xpath)