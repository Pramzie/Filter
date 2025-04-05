import cv2
import mediapipe as mp
import numpy as np
import time
import random

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)

# Store time when both hands are detected
hand_raised_time = None
filter_active = False
filters = ['pencil', 'sketch', 'oil_paint', 'sepia']
current_filter = None

# Apply Filters

def apply_pencil_sketch(frame):
    gray, sketch = cv2.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
    return sketch

def apply_sketch(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    inverted_blur = cv2.bitwise_not(blurred)
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)
    return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

def apply_oil_paint(frame):
    return cv2.xphoto.oilPainting(frame, 7, 1)

def apply_sepia(frame):
    sepia_matrix = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia_frame = cv2.transform(frame, sepia_matrix)
    return np.clip(sepia_frame, 0, 255).astype(np.uint8)

# Filter selection
filter_functions = {
    'pencil': apply_pencil_sketch,
    'sketch': apply_sketch,
    'oil_paint': apply_oil_paint,
    'sepia': apply_sepia
}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip for a mirror effect
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    hand_count = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            hand_count += 1
    
    # Check if both hands are detected
    if hand_count >= 2:
        if hand_raised_time is None:
            hand_raised_time = time.time()
        elif time.time() - hand_raised_time > 2:  # 3 seconds threshold
            filter_active = True
            current_filter = random.choice(filters)  # Random filter
            hand_raised_time = None  # Reset timer to prevent instant switching
    else:
        hand_raised_time = None  # Reset if hands are lowered
    
    # Apply the selected filter
    if filter_active and current_filter:
        frame = filter_functions[current_filter](frame)
    
    
    cv2.imshow("Ghibli-Style Filter Switcher", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()