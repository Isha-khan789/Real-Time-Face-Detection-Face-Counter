# Real-Time Face Detection & Face Counter

A real-time computer vision application built with **Python and OpenCV** that detects human faces through a webcam, counts detected faces, displays FPS, captures screenshots, and logs face-count changes with timestamps.

## Features

*  Real-time webcam video
*  Face detection using Haar Cascade
*  Bounding boxes around detected faces
*  Real-time face counter
*  Maximum number of faces detected during a session
*  Real-time FPS display
*  Screenshot capture
*  Face detection event logging
*  CSV-based detection log
*  Timestamped face-count changes
* Keyboard controls for screenshots and exiting

##  Technologies Used

* **Python**
* **OpenCV**
* **NumPy**
* **Haar Cascade Classifier**
* **CSV**
* **Webcam / Real-Time Video Processing**

##  Project Structure

```text
Real-Time Face Detection & Face Counter/
│
├── editor.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── screenshots/
│   └── Generated screenshots
│
├── face_log.csv
│   └── Generated face detection logs
│
└── venv/
    └── Python virtual environment
```

> `venv/`, `screenshots/`, and generated CSV files are excluded from GitHub using `.gitignore`.

##  How It Works

The application follows this computer vision pipeline:

```text
Webcam
   ↓
Capture Frame
   ↓
Convert to Grayscale
   ↓
Haar Cascade Face Detection
   ↓
Detect Face Coordinates
   ↓
Draw Bounding Boxes
   ↓
Count Faces
   ↓
Calculate FPS
   ↓
Display Results
   ↓
Log Face Count Changes
```

##  Face Detection

The project uses OpenCV's **Haar Cascade Classifier** for face detection.

The classifier is loaded using OpenCV's built-in Haar Cascade path:

```python
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)
```

The detector then searches the grayscale webcam frame:

```python
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=7
)
```

### Parameters

**`scaleFactor`**

Controls how much the image is reduced during the multi-scale detection process.

**`minNeighbors`**

Controls how strict the detector is when deciding whether a region is a face.

Higher values generally reduce false positives but can also cause some faces to be missed.

##  Face Counter

The number of detected faces is calculated using:

```python
face_count = len(faces)
```

The application displays the current count directly on the webcam feed.

Example:

```text
Faces detected: 2
```

The program also keeps track of the maximum number of faces detected during the current session.

##  FPS Counter

The application calculates the approximate processing speed in **Frames Per Second (FPS)**.

Example:

```text
FPS: 29.84
```

This helps measure how smoothly the real-time computer vision application is running.

##  Screenshot Capture

Press:

```text
S
```

to save the current webcam frame.

Screenshots are saved with timestamp-based filenames:

```text
screenshots/screenshot_1234567890.jpg
```

The captured image includes the detected face bounding boxes and displayed information.

##  CSV Logging

The application records face-count changes with timestamps.

Example:

```csv
Time,Faces
10:15:21,0
10:15:27,1
10:15:35,2
10:15:42,1
10:15:50,0
```

The program only logs when the detected face count changes rather than writing a new row for every video frame.

##  Keyboard Controls

| Key | Action               |
| --- | -------------------- |
| `Q` | Quit the application |
| `S` | Capture screenshot   |

Make sure the OpenCV window is focused when pressing the keys.

##  Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Enter the project directory

```bash
cd "Real-Time Face Detection & Face Counter"
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

##  Run the Application

Start the application with:

```bash
python editor.py
```

Your webcam should open automatically.

You can then:

* Move in front of the camera to test face detection
* Press `S` to capture a screenshot
* Press `Q` to close the application

##  Requirements

The project currently uses:

```text
Python
opencv-python
numpy
```

Dependencies are listed in:

```text
requirements.txt
```

Install them using:

```bash
python -m pip install -r requirements.txt
```

##  Limitations

This project uses a traditional **Haar Cascade** detector, so it can sometimes produce false positives or miss faces.

Performance can also vary depending on:

* Lighting conditions
* Camera quality
* Face angle
* Distance from the camera
* Background complexity

Haar Cascade is useful for learning traditional computer vision, but modern deep-learning detectors such as **YOLO** are generally more robust for real-world object detection.

##  What I Learned

Through this project, I practiced:

* OpenCV fundamentals
* Reading webcam frames
* Image preprocessing
* Grayscale conversion
* Haar Cascade face detection
* Bounding boxes
* Real-time video processing
* FPS calculation
* Keyboard event handling
* Image saving
* CSV file handling
* Timestamp logging
* Python virtual environments
* Git and GitHub project management

## Future Improvements

Possible future improvements include:

* Face recognition
* Multiple-face tracking
* Better detection accuracy
* Confidence scores
* Automatic attendance system
* Database integration
* Web-based dashboard
* Real-time analytics
* Deep-learning-based face detection
* YOLO-based object detection

##  Author

**Isha**

Computer Science Student | AI/ML & Computer Vision Learner

---

 If you found this project useful, feel free to explore the repository and follow my learning journey in AI/ML and Computer Vision.
