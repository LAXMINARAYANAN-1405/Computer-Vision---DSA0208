import cv2

# Step 1: Read the image
img = cv2.imread('picture6.png')

if img is None:
    print("❌ Error: Image not found!")
else:
    # Step 2: Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 3: Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Step 4: Apply Canny Edge Detection
    edges = cv2.Canny(blurred, threshold1=100, threshold2=200)

    # Step 5: Display all images
    cv2.imshow("Original Image", img)
    cv2.imshow("Gray Image", gray)
    cv2.imshow("Canny Edge Detection", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
