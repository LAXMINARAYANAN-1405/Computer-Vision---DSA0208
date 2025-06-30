import cv2
import numpy as np

# Step 1: Read the image
img = cv2.imread('picture3.png')

if img is None:
    print("❌ Error: Image not found!")
else:
    # Step 2: Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 3: Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Step 4: Apply Sobel operator in X direction
    sobel_x = cv2.Sobel(blurred, cv2.CV_64F, dx=1, dy=0, ksize=3)
    abs_sobel_x = cv2.convertScaleAbs(sobel_x)

    # Step 5: Display images
    cv2.imshow('Original Image', img)
    cv2.imshow('Sobel X - Vertical Edges', abs_sobel_x)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
