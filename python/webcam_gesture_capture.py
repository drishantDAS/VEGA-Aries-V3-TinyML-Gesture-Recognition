import cv2
import mediapipe as mp
import serial
import time

SERIAL_PORT = "COM5"
BAUD_RATE = 115200

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

def extract_features(hand_landmarks):
    features = []
    for landmark in hand_landmarks.landmark:
        features.append(landmark.x)
        features.append(landmark.y)
    return features

def format_features(features):
    return ",".join(f"{v:.6f}" for v in features) + "\n"

def main():
    print("VEGA TinyML webcam feature sender")
    print(f"Opening {SERIAL_PORT} at {BAUD_RATE} baud...")

    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open laptop webcam")

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    ) as hands:
        try:
            while True:
                ok, frame = cap.read()
                if not ok:
                    break

                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result = hands.process(rgb)

                if result.multi_hand_landmarks:
                    hand = result.multi_hand_landmarks[0]
                    features = extract_features(hand)

                    if len(features) == 42:
                        ser.write(format_features(features).encode("utf-8"))
                        print("42 features sent")

                    mp_draw.draw_landmarks(
                        frame, hand, mp_hands.HAND_CONNECTIONS
                    )

                cv2.imshow("VEGA TinyML Gesture Capture", frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        finally:
            cap.release()
            ser.close()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
