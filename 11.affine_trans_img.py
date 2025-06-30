import cv2
import numpy as np

# Step 1: Read the image
img = cv2.imread('picture2.png')

# Step 2: Check if image is loaded
if img is None:
    print("❌ Error: Image not found!")
else:
    # Step 3: Define 3 points from the original image
    rows, cols, ch = img.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

    # Step 4: Define where those points should map to
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    # Step 5: Get the Affine Transform matrix
    M = cv2.getAffineTransform(pts1, pts2)

    # Step 6: Apply the transformation
    result = cv2.warpAffine(img, M, (cols, rows))

    # Step 7: Show both images
    cv2.imshow('Original Image', img)
    cv2.imshow('Affine Transformed Image', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
