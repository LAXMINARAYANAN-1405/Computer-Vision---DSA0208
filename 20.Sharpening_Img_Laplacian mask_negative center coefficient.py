import cv2
import numpy as np

# Step 1: Read the image
img = cv2.imread('picture6.png')

if img is None:
    print("❌ Error: Image not found!")
else:
    # Step 2: Convert to grayscale (optional for sharpening)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 3: Define Laplacian kernel with negative center coefficient
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    # Step 4: Apply the sharpening kernel
    sharpened = cv2.filter2D(gray, -1, kernel)

    # Step 5: Display the result
    cv2.imshow("Original (Gray)", gray)
    cv2.imshow("Sharpened Image", sharpened)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
