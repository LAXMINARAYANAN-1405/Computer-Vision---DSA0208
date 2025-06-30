import cv2

# Step 1: Read the image
img = cv2.imread('picture3.png')

# Step 2: Check if image is loaded
if img is None:
    print("❌ Error: Image not found!")
else:
    # Step 3: Rotate clockwise (90 degrees)
    clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Step 4: Rotate counterclockwise (90 degrees)
    counter_clockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Step 5: Show all images
    cv2.imshow('Original Image', img)
    cv2.imshow('Rotated Clockwise', clockwise)
    cv2.imshow('Rotated Counter-Clockwise', counter_clockwise)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
