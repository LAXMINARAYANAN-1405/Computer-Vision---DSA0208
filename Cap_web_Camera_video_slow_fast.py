import cv2

# Step 1: Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Step 2: Check if webcam opened
if not cap.isOpened():
    print("❌ Error: Cannot access webcam.")
else:
    # Step 3: Ask user for playback mode
    print("Choose playback speed:")
    print("1. Normal Motion")
    print("2. Slow Motion")
    print("3. Fast Motion")
    choice = int(input("Enter choice (1/2/3): "))

    # Step 4: Set delay based on choice
    if choice == 1:
        delay = 30
    elif choice == 2:
        delay = 100
    elif choice == 3:
        delay = 10
    else:
        print("Invalid choice. Defaulting to normal.")
        delay = 30

    print("📷 Press 'q' to quit webcam feed.")

    # Step 5: Loop to read frames from webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Webcam Video', frame)

        # WaitKey controls speed
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
