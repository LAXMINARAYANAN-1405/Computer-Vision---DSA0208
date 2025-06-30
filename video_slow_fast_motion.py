import cv2

# Step 1: Read the video file
cap = cv2.VideoCapture('video1.mp4')  # Replace with your video file name

# Step 2: Check if video opened successfully
if not cap.isOpened():
    print("❌ Error: Cannot open video file.")
else:
    # Step 3: Choose playback mode
    print("Choose playback speed:")
    print("1. Normal Motion")
    print("2. Slow Motion")
    print("3. Fast Motion")
    choice = int(input("Enter choice (1/2/3): "))

    # Step 4: Set delay based on choice
    if choice == 1:
        delay = 30  # ~30 fps (Normal)
    elif choice == 2:
        delay = 100  # Slower playback
    elif choice == 3:
        delay = 10   # Faster playback
    else:
        print("Invalid choice. Defaulting to normal.")
        delay = 30

    # Step 5: Read and display frames
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video Playback', frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
