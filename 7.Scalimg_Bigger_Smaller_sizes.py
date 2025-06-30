import cv2

# Step 1: Read the image
img = cv2.imread('picture6.png')

# Step 2: Check if image is loaded
if img is None:
    print("❌ Error: Image not found!")
else:
    # Step 3: Resize to smaller size (e.g., 50% of original)
    small = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Step 4: Resize to bigger size (e.g., 200% of original)
    big = cv2.resize(img, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

    # Step 5: Display all images
    cv2.imshow('Original Image', img)
    cv2.imshow('Smaller Image', small)
    cv2.imshow('Bigger Image', big)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
