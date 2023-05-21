import dxcam
import win32gui
from PIL import Image

# Create a dxcam instance
camera = dxcam.create()

# Get the handle of the target game window
game_title = "Honkai: Star Rail"
game_window = win32gui.FindWindow(None, game_title)

# Get the dimensions of the game window
left, top, right, bottom = win32gui.GetClientRect(game_window)
width = right - left
height = bottom - top

# Adjust the region to match the desired dimensions
region_width = 1920
region_height = 1080
region_left = (width - region_width) // 2
region_top = (height - region_height) // 2
region_right = region_left + region_width
region_bottom = region_top + region_height

# Set the region for capturing the screenshot
region = (region_left, region_top, region_right, region_bottom)

# Start capturing frames
camera.start(region=region)

# Capture a frame (screenshot)
frame = camera.grab()

# Stop capturing frames
camera.stop()

# Convert the frame to a PIL Image
image = Image.fromarray(frame)

# Save the image to a file
image.save("screenshot.png")
