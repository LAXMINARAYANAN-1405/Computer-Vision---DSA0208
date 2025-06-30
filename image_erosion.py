import cv2
import numpy as np

# Step 1: Read the image
img = cv2.imread('picture6.png')

# Step 2: Check if image is loaded
if img is None:
    print("❌ Error: Image not found!")
else:
    # Step 3: Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 4: Apply binary thresholding
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Step 5: Define kernel
    kernel = np.ones((5, 5), np.uint8)

    # Step 6: Apply erosion
    eroded = cv2.erode(thresh, kernel, iterations=1)

    # Step 7: Display the images
    cv2.imshow('Original Image', img)
    cv2.imshow('Binary Image', thresh)
    cv2.imshow('Eroded Image', eroded)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
