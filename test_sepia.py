from PIL import Image
from sepia import sepia

# Open your photograph
photo = Image.open("C:/Users/jones/Downloads/Domestic-cat-35.jpg.jpg")

# Apply the sepia effect
photo = sepia(photo)

# Save the finished photograph
photo.save("sepia_photo.jpg")

print("Your sepia photograph is finished!")
