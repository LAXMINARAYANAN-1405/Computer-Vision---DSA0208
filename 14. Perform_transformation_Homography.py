import cv2
import numpy as np

# Step 1: Read the image
img = cv2.imread('picture6.png')

# Step 2: Check if image is loaded
if img is None:
    print("❌ Error: Image not found!")
    exit()

# Step 3: Define points on original image (e.g., corners of a sheet)
src_pts = np.float32([[100, 100], [400, 100], [100, 400], [400, 400]])

# Step 4: Define destination points (where you want the source points mapped)
dst_pts = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# Step 5: Compute the Homography matrix
H, status = cv2.findHomography(src_pts, dst_pts)

# Step 6: Warp the image using the Homography matrix
warped_img = cv2.warpPerspective(img, H, (300, 300))

# Step 7: Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformed Image", warped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
