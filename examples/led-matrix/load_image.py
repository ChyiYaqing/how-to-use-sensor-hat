from sense_hat import SenseHat
from PIL import Image

# Initialize SenseHAT
sense = SenseHat()

# Load the image
img = Image.open("../images/apple.png")

# Ensure the image is 8x8 pixels in RGB format
img = img.resize((8, 8)).convert("RGB")

# Get pixel data
pixels = list(img.getdata())

# Display the image on the LED matrix
sense.set_pixels(pixels)
#sense.load_image("../images/apple.png")
