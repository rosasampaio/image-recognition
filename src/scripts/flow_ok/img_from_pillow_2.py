from PIL import Image, ImageFilter

# Load the image
img = Image.open('image.jpg')

# Resize the image to a suitable size
img = img.resize((640, 480), Image.ANTIALIAS)

# Apply a filter to enhance the element
img = img.filter(ImageFilter.EDGE_ENHANCE)

# Convert the image to a numpy array
img_array = np.array(img)

# Extract the element using numpy indexing
element = img_array[100:200, 100:200]  # adjust the indices as needed
print("Extracted element:", element.shape)