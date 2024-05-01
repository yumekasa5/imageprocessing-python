import cv2

def estimate_dimensions(image_path, pixel_size):
    # Load the image
    image = cv2.imread(image_path, 0)  # Read the image as grayscale

    # Apply edge detection
    edges = cv2.Canny(image, 100, 200)  # Adjust the threshold values as needed

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the longest contour (assuming it represents the vertical line)
    longest_contour = max(contours, key=cv2.contourArea)

    # Calculate the length of the contour in pixels
    contour_length = cv2.arcLength(longest_contour, True)

    # Calculate the estimated length in the real world based on the pixel size
    estimated_length = contour_length * pixel_size

    return estimated_length

# import numpy as np
# import cv2

# # Create an empty 16-bit grayscale image of size 100x100
# image = np.zeros((100, 100), dtype=np.uint16)

# # Define the line width and intensity
# line_width = 21.05128
# line_intensity = 30000

# # Calculate the start and end of the line in the image
# start = (100 - line_width) / 2
# end = start + line_width

# # Draw the line on the image
# for i in range(100):
#     for j in range(100):
#         if start <= j < end:
#             # Calculate the brightness value based on a 3rd degree polynomial function
#             x = (j - start) / line_width  # Normalize x to the range [0, 1]
#             brightness = line_intensity * (1 - (2 * abs(x - 0.5)) ** 3)  # 3rd degree polynomial function
#             image[i, j] = brightness

# # Save the image
# cv2.imwrite(r"C:\work\Pyhton\image\100x100_vertical_line.png", image)

import numpy as np

# Define the coefficients of the polynomial
# For example, for the polynomial x^3 + 2x^2 - 3x + 1, the coefficients would be [1, 2, -3, 1]
coefficients = [1, 2, -3, 1]

# Use numpy.roots to find the roots
roots = np.roots(coefficients)

print(roots)