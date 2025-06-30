import cv2
import numpy as np

# Step 1: Read the image
img = cv2.imread('picture3.png')

# Step 2: Check if image is loaded
if img is None:
    print("❌ Error: Image not found!")
else:
    # Step 3: Define translation values (tx = right, ty = down)
    tx = 100  # move 100 pixels right
    ty = 50   # move 50 pixels down

    # Step 4: Create translation matrix
    M = np.float32([[1, 0, tx], [0, 1, ty]])

    # Step 5: Apply affine transformation
    moved = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

    # Step 6: Display images
    cv2.imshow('Original Image', img)
    cv2.imshow('Moved Image', moved)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
