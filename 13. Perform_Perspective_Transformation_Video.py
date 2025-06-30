import cv2
import numpy as np

# Step 1: Open video file or webcam (0 = default webcam)
cap = cv2.VideoCapture('video1.mp4')  # or use 0 for live camera

# Step 2: Check if video is opened
if not cap.isOpened():
    print("❌ Error: Cannot open video.")
    exit()

# Step 3: Define source and destination points for transformation
# These should be inside the frame resolution (adjust as needed)
src_points = np.float32([[100, 100], [500, 100], [100, 400], [500, 400]])
dst_points = np.float32([[0, 0], [400, 0], [0, 300], [400, 300]])

# Step 4: Get the perspective transform matrix
M = cv2.getPerspectiveTransform(src_points, dst_points)

# Step 5: Read and transform each frame
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply perspective transformation
    warped_frame = cv2.warpPerspective(frame, M, (400, 300))

    # Display the original and transformed frames
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Perspective Transformed Frame", warped_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 6: Release and close
cap.release()
cv2.destroyAllWindows()
