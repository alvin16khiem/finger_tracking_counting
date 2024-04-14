Purpose:
The script aims to track fingers in real-time using OpenCV and a webcam.

Image Loading:
Images of hands are loaded from a specified folder.

Hand Detection:
Using the handDetector class, hands and landmarks are detected in each frame of the webcam feed.

Finger Status Detection:
By analyzing the positions of landmarks, the script determines the status of each finger (open or closed).

Finger Counting:
The script counts the number of open fingers based on their detected status.

Display and Performance:
The count of open fingers and the frames per second (FPS) are displayed on the video feed to provide real-time feedback on finger tracking performance.
