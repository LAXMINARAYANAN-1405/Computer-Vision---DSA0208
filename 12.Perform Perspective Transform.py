import cv2
import numpy as np

# Step 1: Read the image
img = cv2.imread('picture1.png')

# Step 2: Check if image is loaded
if img is None:
    print("❌ Error: Image not found!")
else:
    # Step 3: Define 4 points from input image (source)
    pts1 = np.float32([[100, 100], [400, 100], [100, 400], [400, 400]])

    # Step 4: Define 4 points for the output image (destination)
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

    # Step 5: Get the perspective transform matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Step 6: Apply the perspective warp
    output = cv2.warpPerspective(img, matrix, (300, 300))

    # Step 7: Show both images
    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformed Image", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
