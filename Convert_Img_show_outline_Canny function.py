import cv2

# Step 1: Read the image
img = cv2.imread('picture3.png')

# Step 2: Check if image is loaded
if img is None:
    print("❌ Error: Image not found!")
else:
    # Step 3: Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 4: Apply Canny Edge Detection
    edges = cv2.Canny(gray, threshold1=100, threshold2=200)

    # Step 5: Display the result
    cv2.imshow('Original Image', img)
    cv2.imshow('Canny Edge Detection', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
