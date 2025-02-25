# Real-Time Human Detection and Pose Estimation

## Overview
This project implements real-time human detection and pose estimation using OpenCV and MediaPipe. It captures video from the webcam, detects human presence, facial landmarks, and tracks body poses in real-time.

## Features
- Detects and draws 33 key body landmarks using MediaPipe Pose.
- Detects human presence and draws bounding boxes around faces using MediaPipe Face Detection.
- Displays the processed video with real-time annotations.
- Flips the image horizontally and converts it to grayscale for an additional output window.
- Prints a message indicating whether a human is detected in the frame.

## Requirements
Ensure you have Python installed along with the following dependencies:

```bash
pip install opencv-python mediapipe
```

## Usage
Run the script using:

```bash
python pose_human_detection.py
```

The script will:
1. Capture video from the webcam.
2. Detect human presence, faces, and draw bounding boxes.
3. Detect human poses and overlay landmark connections.
4. Display two video windows:
   - One with real-time human detection and pose estimation.
   - Another with a flipped grayscale version.
5. Print a message indicating whether a human is detected.
6. Exit when the user closes the video window.

## Code Explanation
- **OpenCV (`cv2`)** is used for video capture and image processing.
- **MediaPipe (`mp.solutions.pose & mp.solutions.face_detection`)** is used for full-body detection and face detection.
- The script continuously reads frames from the webcam, processes them, and displays the results in real time.

## Key Functions
- `cv2.VideoCapture(0)`: Captures video from the default webcam.
- `mp.solutions.pose.Pose()`: Initializes full-body pose detection.
- `mp.solutions.face_detection.FaceDetection()`: Initializes face detection.
- `mp.solutions.drawing_utils.draw_landmarks()`: Draws pose landmarks.
- `mp_drawing.draw_detection(img, detection)`: Draws bounding boxes around detected faces.
- `cv2.imshow()`: Displays video output.
- `cv2.flip()`: Flips the image horizontally.
- `cv2.cvtColor()`: Converts images to different color spaces (e.g., grayscale).

## Closing the Application
To stop the program, close the video window manually.

## Future Improvements
- Add hand gesture recognition using MediaPipe Hands.
- Add sign language translation using MediaPipe Hands.
- Improve detection speed and accuracy with optimizations.

## License
This project is open-source and free to use under the MIT License.

