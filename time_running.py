import cv2
import datetime

# Open the default webcam (0 = first camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Get current time as a string
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Overlay the time on the frame
    cv2.putText(
        frame,
        current_time,
        (10, 30),                     # position (x, y)
        cv2.FONT_HERSHEY_SIMPLEX,     # font
        1,                             # font scale
        (0, 255, 0),                   # color (BGR) - green
        2,                              # thickness
        cv2.LINE_AA
    )

    cv2.imshow("Webcam with Live Clock", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()