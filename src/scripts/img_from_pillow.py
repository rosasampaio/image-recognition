from PIL import ImageGrab
from PIL import features

print(features.check_feature(feature="xcb"))
print(features.get_supported_features())
print(features.check_feature(feature="xcb"))

# Capture the entire screen
# bbox = (100, 100, 500, 500)  
# bbox = (hight, since that, wight, hight)  
# box = (300, 300, 600, 600) 
# box = (100, 270, 300, 300)  # commands.txt

box = (100, 270, 300, 300) 
screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")
screenshot = ImageGrab.grab(bbox=box)

# Save the screenshot to a file
screenshot.save("commands.png")

# Close the screenshot
screenshot.close()