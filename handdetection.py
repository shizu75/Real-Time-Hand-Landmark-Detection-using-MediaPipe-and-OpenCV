import cv2
import mediapipe as mp
import warnings

warnings.filterwarnings('ignore')

mp_hand = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
det = mp_hand.Hands(static_image_mode = True, max_num_hands = 3, min_detection_confidence = 0.5, min_tracking_confidence = 0.5)

cao = cv2.VideoCapture(0)

while cao.isOpened():
    r, f = cao.read()

    if r == True:
        f = cv2.flip(f, 1)
        f = cv2.resize(f, (500, 500))
        f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
        res = det.process(f)
        f = cv2.cvtColor(f, cv2.COLOR_RGB2BGR)

        if res.multi_hand_landmarks:
            for hand_landmarks in res.multi_hand_landmarks:
                mp_draw.draw_landmarks(f, hand_landmarks, mp_hand.HAND_CONNECTIONS)

        cv2.imshow('detected', f)

        if cv2.waitKey(20) & 0xFF == ord('p'):
            break
    else:
        break

cao.release()
cv2.destroyAllWindows()
