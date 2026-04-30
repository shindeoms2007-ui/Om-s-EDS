import numpy as np

# Example: 5x5 grayscale image matrix (values 0–255)
image = np.array([
    [120, 200, 150, 80, 60],
    [90, 255, 130, 70, 40],
    [30, 60, 90, 120, 150],
    [200, 220, 240, 250, 255],
    [10, 20, 30, 40, 50]
])

# Step 1: Increase brightness by adding 30
brightened = image + 30

# Step 2: Ensure values do not exceed 255
brightened = np.clip(brightened, 0, 255)

# Step 3: Find average brightness
average_brightness = np.mean(brightened)

# Output
print("Original Image:\n", image)
print("\nBrightened Image:\n", brightened)
print("\nAverage Brightness:", average_brightness)