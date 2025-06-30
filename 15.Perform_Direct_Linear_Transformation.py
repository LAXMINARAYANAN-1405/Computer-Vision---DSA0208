import cv2
import numpy as np

# Step 1: Load image
img = cv2.imread('picture4.png')

if img is None:
    print("❌ Error: Image not found!")
    exit()

# Step 2: Define 4 corresponding points (source → destination)
src_pts = np.array([[100, 100], [400, 100], [100, 400], [400, 400]], dtype=np.float32)
dst_pts = np.array([[0, 0], [300, 0], [0, 300], [300, 300]], dtype=np.float32)

# Step 3: Build matrix A using DLT
A = []
for i in range(4):
    x, y = src_pts[i][0], src_pts[i][1]
    u, v = dst_pts[i][0], dst_pts[i][1]
    A.append([-x, -y, -1, 0, 0, 0, x*u, y*u, u])
    A.append([0, 0, 0, -x, -y, -1, x*v, y*v, v])

A = np.asarray(A)

# Step 4: Perform SVD to find H
U, S, Vt = np.linalg.svd(A)
H = Vt[-1].reshape(3, 3)  # Last row of V (corresponds to smallest singular value)

# Step 5: Normalize and apply homography
H = H / H[2, 2]
warped = cv2.warpPerspective(img, H, (300, 300))

# Step 6: Show results
cv2.imshow("Original Image", img)
cv2.imshow("DLT Homography Output", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
