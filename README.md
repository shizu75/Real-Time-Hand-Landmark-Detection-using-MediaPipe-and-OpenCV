# Real-Time Hand Landmark Detection using MediaPipe and OpenCV

## Project Overview
This project implements **real-time hand landmark detection** using **MediaPipe Hands** integrated with **OpenCV** for video capture and visualization. The system detects up to multiple hands from a live webcam feed and overlays detailed hand landmarks and connections on each detected hand.

The project demonstrates efficient, real-time computer vision using a lightweight and highly optimized framework.

---

## Objectives
- Detect human hands in real time using a webcam
- Identify and visualize 21 hand landmarks per hand
- Draw skeletal hand connections dynamically
- Understand MediaPipe’s hand tracking pipeline
- Integrate MediaPipe with OpenCV for live video processing

---

## Technologies Used
- Python 3
- OpenCV (cv2)
- MediaPipe
- NumPy (implicit via MediaPipe)
- Warnings (for clean execution)

---

## System Setup

### Hand Detection Configuration
- **Static Image Mode:** Enabled
- **Maximum Hands Detected:** 3
- **Minimum Detection Confidence:** 0.5
- **Minimum Tracking Confidence:** 0.5

These parameters balance accuracy and real-time performance.

---

## Methodology

### 1. Webcam Capture
- Live video stream captured using OpenCV
- Frames processed continuously until user interruption

---

### 2. Frame Preprocessing
- Frames flipped horizontally for mirror view
- Resized to a fixed resolution (500 × 500)
- Converted from BGR to RGB (required by MediaPipe)

---

### 3. Hand Landmark Detection
- MediaPipe detects hands and extracts:
  - 21 3D landmarks per hand
- Supports multiple hands in a single frame

---

### 4. Landmark Visualization
- Hand landmarks drawn using MediaPipe drawing utilities
- Connections between landmarks rendered to show hand skeleton

---

### 5. Real-Time Display
- Annotated video feed displayed in a window
- Execution stops when the **'p'** key is pressed

---

## Key Concepts Demonstrated
- Real-time video processing
- Hand landmark detection
- Multi-hand tracking
- RGB/BGR color space conversion
- Integration of MediaPipe with OpenCV

---

## Output
- Live webcam feed with:
  - Detected hand landmarks
  - Connected skeletal structure for each hand
- Smooth real-time performance

---

## How to Run the Project

### Prerequisites
Install required libraries:
- opencv-python
- mediapipe

---

### Steps
1. Ensure a webcam is connected
2. Run the Python script
3. Show your hands to the camera
4. Observe:
   - Real-time landmark detection
   - Hand skeleton visualization
5. Press **'p'** to exit

---

## Learning Outcomes
- Understanding of MediaPipe Hands API
- Experience with real-time computer vision systems
- Ability to visualize pose and landmark data
- Practical integration of OpenCV and MediaPipe

---

## Limitations
- Works best under good lighting conditions
- Performance depends on camera quality
- Static image mode may increase computational cost

---

## Future Improvements
- Switch to dynamic tracking mode for efficiency
- Add gesture recognition logic
- Track hand orientation and motion
- Integrate with sign language recognition
- Export landmark data for ML applications

---

## Use Case
This project is suitable for:
- Gesture recognition research
- Human-computer interaction (HCI)
- Computer vision learning projects
- AI-powered interactive applications

---

## Author
Developed as an educational computer vision project demonstrating real-time hand landmark detection using MediaPipe and OpenCV.
