import cv2
import numpy as np

# Step 1: Read the image
img = cv2.imread('picture2.png')

if img is None:
    print("❌ Error: Image not found!")
else:
    # Step 2: Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 3: Apply Gaussian Blur to smoothen
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Step 4: Apply Sobel operator in Y direction
    sobel_y = cv2.Sobel(blurred, cv2.CV_64F, dx=0, dy=1, ksize=3)
    abs_sobel_y = cv2.convertScaleAbs(sobel_y)

    # Step 5: Display the output
    cv2.imshow("Original Image", img)
    cv2.imshow("Sobel Y - Horizontal Edges", abs_sobel_y)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
