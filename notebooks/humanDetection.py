import cv2 #Importing opencv
import mediapipe as mp #Importing mediapipe

cap = cv2.VideoCapture(0) #Video capturing, 0=Default camera(built-in webcam, 1=second camera, 2= third camera ad so on. You can also pass a file path)
pose_obj = mp.solutions.pose.Pose() # Create a Pose estimation object for 33 key body landmarks
mp_face_detection = mp.solutions.face_detection # Load Face Detection module
mp_drawing = mp.solutions.drawing_utils # Utility for drawing landmarks


while True:
    key, img = cap.read() # Read a frame from the camera
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert the frame from BGR to RGB (MediaPipe uses RGB format)
    face_obj = mp_face_detection.FaceDetection()  # Initialize the face detection object
    result_face = face_obj.process(imgRGB) # Process the image to detect faces
    
    # If faces are detected, draw bounding boxes around them
    if result_face.detections: 
        for detection in result_face.detections:
            mp_drawing.draw_detection(img, detection)

    # Draw the detected pose landmarks on the original image
    result = pose_obj.process(imgRGB)
    mp.solutions.drawing_utils.draw_landmarks(img, result.pose_landmarks,
                                                    mp.solutions.pose.POSE_CONNECTIONS)
    
    # Check if any pose landmarks are detected
    if result.pose_landmarks:
        print("human dectected") # Print message if a human is detected
    else:
        print("No human") # Print message if no human is detected
    
    img_flip = cv2.flip(img, 1) # Flip the image horizontally (mirror effect)
    img_gray = cv2.cvtColor(img_flip, cv2.COLOR_BGR2GRAY) # Convert the flipped image to grayscale
    cv2.imshow("video", img) # Display the original image with detected landmarks
    cv2.imshow("video_flip", img_gray) # Display the flipped grayscale image
    cv2.waitKey(1) # Wait for a key press for 1 millisecond, allowing video to be displayed
    
    # Check if the user closes the video window
    if cv2.getWindowProperty("video", cv2.WND_PROP_VISIBLE) < 1:
        break # Exit the loop if the window is closed
   