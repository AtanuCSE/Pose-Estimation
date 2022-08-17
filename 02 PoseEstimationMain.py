import cv2
import mediapipe as mp

# Load Video
cap = cv2.VideoCapture("PoseVideo/1.mp4")

FrameCount = 0

# Define Object
mpPose = mp.solutions.pose
pose = mpPose.Pose() 
# Define Drawing Utilities
mpDraw = mp.solutions.drawing_utils

while True:

    ## Capture frames and convert BGR to RGB
    ## ! Mediapipe pose detection can't work without RGB
    
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)    # Results contains the estimations
    # print(results.pose_landmarks)   # Printing the landmarks
    
    # ! Drawing dots in the frames
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    FrameCount+=1
    cv2.putText(img, str(int(FrameCount)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.imshow("Frames", img)
    cv2.waitKey(1)
    
    if FrameCount==200:
        break