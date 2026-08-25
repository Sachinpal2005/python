import cv2

def rotate_frame(frame, angle):
    """Rotate frame by given angle (degrees) without cropping."""
    h, w = frame.shape[:2]
    center = (w // 2, h // 2)

    # Get rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Compute new bounding dimensions so the image isn't cropped
    cos = abs(M[0, 0])
    sin = abs(M[0, 1])
    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))

    # Adjust the rotation matrix to account for translation
    M[0, 2] += (new_w / 2) - center[0]
    M[1, 2] += (new_h / 2) - center[1]

    rotated = cv2.warpAffine(frame, M, (new_w, new_h))
    return rotated


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    angle = 0        # current rotation angle
    step = 5         # degrees per key press
    flipped = False  # horizontal mirror flip

    print("Controls:")
    print("  a -> rotate counter-clockwise")
    print("  d -> rotate clockwise")
    print("  f -> flip horizontally")
    print("  n -> reset to normal (no rotation, no flip)")
    print("  q -> quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        if flipped:
            frame = cv2.flip(frame, 1)

        if angle != 0:
            frame = rotate_frame(frame, angle)

        # Show current angle on screen
        display = frame.copy()
        cv2.putText(display, f"Angle: {angle % 360}  Flipped: {flipped}",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Webcam", display)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('a'):
            angle = (angle - step) % 360
        elif key == ord('d'):
            angle = (angle + step) % 360
        elif key == ord('f'):
            flipped = not flipped
        elif key == ord('n'):
            angle = 0
            flipped = False
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()