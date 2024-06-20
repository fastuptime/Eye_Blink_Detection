# Eye Blink Detection 👀💡

![image](https://github.com/fastuptime/Eye_Blink_Detection/assets/63351166/1377a9ff-499d-4602-b650-baabea80b0c0)


## Overview 🌟

Welcome to the **Eye Blink Detection** repository! This project utilizes OpenCV and MediaPipe to detect eye blinks in real-time using a webcam. It calculates the Eye Aspect Ratio (EAR) to determine whether the eyes are open or closed, and displays the last blink time on the screen.

## Features 🚀

- **Real-Time Eye Blink Detection**: Detects blinks in real-time using webcam input.
- **Eye Aspect Ratio Calculation**: Uses EAR to determine eye state.
- **Blink Timestamp**: Displays the last blink time on the screen.
- **Simple and Intuitive Interface**: Easy-to-understand visual cues for eye state.

## Installation and Setup 🛠️

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/fastuptime/Eye_Blink_Detection.git
   cd Eye_Blink_Detection
   ```

2. **Install Dependencies**:
   - Ensure you have Python installed.
   - Install required packages:
     ```sh
     pip install opencv-python mediapipe numpy
     ```

3. **Run the Program**:
   - Execute the Python script:
     ```sh
     python eye_blink_detection.py
     ```

## Usage 💻

1. **Launch the Program**:
   - Run the script. The webcam will start, and the program will begin detecting blinks.

2. **Eye Blink Detection**:
   - The program displays the current state of the eyes (open or closed) on the screen.
   - It also shows the last blink time.

3. **Exit the Program**:
   - Press the 'q' key to quit the program.

## Code Explanation 📝

### `eye_blink_detection.py`

- **Import Libraries**:
  ```python
  import cv2
  import mediapipe as mp
  import numpy as np
  import time
  ```

- **Initialize MediaPipe and OpenCV**:
  ```python
  mp_face_mesh = mp.solutions.face_mesh
  mp_drawing = mp.solutions.drawing_utils
  face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
  ```

- **Calculate Eye Aspect Ratio (EAR)**:
  ```python
  def eye_aspect_ratio(landmarks, eye_indices):
      # Implementation to calculate EAR
  ```

- **Threshold for Eye Aspect Ratio**:
  ```python
  EYE_AR_THRESH = 0.3
  ```

- **Capture Video from Webcam**:
  ```python
  cap = cv2.VideoCapture(0)
  lastTime = 'Bilinmiyor'
  ```

- **Main Loop for Eye Blink Detection**:
  ```python
  while cap.isOpened():
      ret, frame = cap.read()
      if not ret:
          break
      # Implementation for processing frame and detecting blinks
  ```

- **Display Results and Handle Exit**:
  ```python
  cv2.imshow('Goz Kirpma Tespiti', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()
  ```

## Contributing 🤝

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
