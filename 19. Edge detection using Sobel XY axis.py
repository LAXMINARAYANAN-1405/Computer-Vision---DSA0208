import cv2
import numpy as np

# Step 1: Load the image
img = cv2.imread('picture4.png')

if img is None:
    print("❌ Error: Image not found!")
else:
    # Step 2: Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 3: Apply Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Step 4: Apply Sobel in X and Y
    sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)

    # Step 5: Convert to absolute values
    abs_x = cv2.convertScaleAbs(sobelx)
    abs_y = cv2.convertScaleAbs(sobely)

    # Step 6: Combine both gradients
    sobel_xy = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)

    # Step 7: Display all images
    cv2.imshow("Original", img)
    cv2.imshow("Sobel X", abs_x)
    cv2.imshow("Sobel Y", abs_y)
    cv2.imshow("Sobel XY (Combined)", sobel_xy)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
