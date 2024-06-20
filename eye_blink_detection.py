import cv2
import mediapipe as mp
import numpy as np
import time

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

def eye_aspect_ratio(landmarks, eye_indices):
    A = np.linalg.norm(np.array([landmarks[eye_indices[1]].x, landmarks[eye_indices[1]].y]) - np.array([landmarks[eye_indices[5]].x, landmarks[eye_indices[5]].y]))
    B = np.linalg.norm(np.array([landmarks[eye_indices[2]].x, landmarks[eye_indices[2]].y]) - np.array([landmarks[eye_indices[4]].x, landmarks[eye_indices[4]].y]))
    C = np.linalg.norm(np.array([landmarks[eye_indices[0]].x, landmarks[eye_indices[0]].y]) - np.array([landmarks[eye_indices[3]].x, landmarks[eye_indices[3]].y]))
    ear = (A + B) / (2.0 * C)
    return ear

EYE_AR_THRESH = 0.3

cap = cv2.VideoCapture(0)
lastTime = 'Bilinmiyor'

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            left_eye_indices = [33, 160, 158, 133, 153, 144]
            right_eye_indices = [362, 385, 387, 263, 373, 380]

            left_ear = eye_aspect_ratio(face_landmarks.landmark, left_eye_indices)
            right_ear = eye_aspect_ratio(face_landmarks.landmark, right_eye_indices)

            ear = (left_ear + right_ear) / 2.0
            cv2.putText(frame, f"Son Goz Kirpma Saati: {lastTime}", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            if ear < EYE_AR_THRESH:
                cv2.putText(frame, "Gozler Kapali", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                lastTime = time.strftime('%H:%M:%S')
            else:
                cv2.putText(frame, "Gozler Acik", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Goz Kirpma Tespiti', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
