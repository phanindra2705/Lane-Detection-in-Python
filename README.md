# Lane-Detection-in-Python

Lane Detection with Alerts : 
This project implements a real-time road lane detection system using Python and OpenCV. It processes live video feeds to detect road lanes and provides alerts to ensure safe lane adherence. The program can serve as a foundation for advanced driver-assistance systems (ADAS) or autonomous driving technologies.

Features : 
Real-time lane detection using OpenCV.
Alerts for lane deviation:
Visual Alerts: Displays warnings when the vehicle veers out of the detected lanes.
Audio Alerts: Plays a sound notification when the car deviates significantly from the lane center.
Configurable thresholds for lane deviation detection.
Compatible with live camera feeds or pre-recorded videos.

Technologies Used : 
Python: Core programming language.
OpenCV: For image processing and computer vision tasks.
NumPy: For numerical computations.
Audio Alert Options:
playsound (or alternatives like pygame, winsound, or system commands depending on the platform).

Requirements : 
Install the following Python libraries:

opencv-python
numpy
playsound (or alternatives like pygame or winsound)
