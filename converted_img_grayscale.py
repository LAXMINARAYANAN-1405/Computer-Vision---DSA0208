

import cv2

# Step 1: Read the image (make sure 'image.jpg' is in the same folder)
img = cv2.imread("C:/Users/sedhu pathi/Downloads/Computer Vision/Picture1.png")

# Step 2: Check if image is loaded properly
if img is None:
    print("❌ Error: Image not found. Please check the filename or path.")
else:
    # Step 3: Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 4: Display both images
    cv2.imshow('Original Image', img)
    cv2.imshow('Grayscale Image', gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
