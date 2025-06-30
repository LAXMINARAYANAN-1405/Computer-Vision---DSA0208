import cv2

# Step 1: Read the image
img = cv2.imread('Picture2.png')

# Step 2: Check if image is loaded
if img is None:
    print("❌ Error: Image not found!")
else:
    # Step 3: Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    # Step 4: Show original and blurred images
    cv2.imshow('Original Image', img)
    cv2.imshow('Gaussian Blurred Image', blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
