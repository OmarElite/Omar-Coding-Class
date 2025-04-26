import cv2
import mediapipe as mp
import numpy as np
import screen_brightness_control as sbc
from math import hypot

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Webcam setup
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

# Set window size
window_width = 1280  # You can adjust this
window_height = 1000  # You can adjust this
cv2.namedWindow("Gesture Zoom & Brightness Controller", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Gesture Zoom & Brightness Controller", window_width, window_height)

zoom_factor = 1.0  # Initial zoom

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read frame from webcam.")
        break

    img = cv2.flip(img, 1)  # Mirror effect
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    h, w, _ = img.shape

    if results.multi_hand_landmarks and results.multi_handedness:
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            hand_label = results.multi_handedness[i].classification[0].label  # 'Left' or 'Right'
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Landmark positions
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            thumb_pos = (int(thumb_tip.x * w), int(thumb_tip.y * h))
            index_pos = (int(index_tip.x * w), int(index_tip.y * h))

            # Draw landmarks
            cv2.circle(img, thumb_pos, 10, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, index_pos, 10, (0, 255, 0), cv2.FILLED)
            cv2.line(img, thumb_pos, index_pos, (0, 255, 0), 3)

            distance = hypot(index_pos[0] - thumb_pos[0], index_pos[1] - thumb_pos[1])

            if hand_label == "Left":
                # Brightness control
                brightness = np.interp(distance, [30, 300], [0, 100])
                try:
                    sbc.set_brightness(brightness)
                except Exception as e:
                    print(f"Error adjusting brightness: {e}")
                brightness_bar = np.interp(distance, [30, 300], [400, 150])
                cv2.rectangle(img, (100, 150), (135, 400), (0, 255, 0), 2)
                cv2.rectangle(img, (100, int(brightness_bar)), (135, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'Brightness: {int(brightness)}%', (90, 450),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            elif hand_label == "Right":
                # Zoom control
                zoom_factor = np.interp(distance, [30, 300], [1.0, 2.0])
                zoom_bar = np.interp(distance, [30, 300], [400, 150])
                cv2.rectangle(img, (500, 150), (535, 400), (255, 0, 255), 2)
                cv2.rectangle(img, (500, int(zoom_bar)), (535, 400), (255, 0, 255), cv2.FILLED)
                cv2.putText(img, f'Zoom: {int(zoom_factor * 100)}%', (480, 450),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

    # Apply zoom effect
    if zoom_factor > 1.0:
        center_x, center_y = w // 2, h // 2
        radius_w, radius_h = int(w / (2 * zoom_factor)), int(h / (2 * zoom_factor))
        left = center_x - radius_w
        right = center_x + radius_w
        top = center_y - radius_h
        bottom = center_y + radius_h
        img = img[top:bottom, left:right]
        img = cv2.resize(img, (w, h))

    cv2.imshow("Gesture Zoom & Brightness Controller", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
