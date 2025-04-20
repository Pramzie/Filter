# Filter Switcher using OpenCV & MediaPipe
---

This project uses **OpenCV**, **MediaPipe**, and **hand tracking gestures** to apply artistic real-time filters to your webcam feed. When both hands are raised and visible to the webcam for more than **2 seconds**, a **random Ghibli-style visual filter** is activated!

<p align="center">
  <img src="https://img.shields.io/badge/OpenCV-%230074C1.svg?&style=flat&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/MediaPipe-F9A825?logo=mediapipe&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white"/>
</p>

---

## 🎨 Features

- 🎥 Real-time webcam capture
- ✋ Hand tracking using MediaPipe
- 🪄 Raise both hands for 2+ seconds to activate a random filter
- 🔄 Filters include:
  - Pencil Sketch
  - Hand-Drawn Sketch
  - Oil Painting
  - Sepia Tone
- 👋 Intuitive gesture-based interface (no buttons needed)

---

## 📦 Dependencies

- Python 3.7+
- OpenCV (`opencv-python`, `opencv-contrib-python`)
- MediaPipe
- NumPy

### 🔧 Installation

```bash
pip install opencv-python opencv-contrib-python mediapipe numpy
```

---

## 🚀 Usage

Simply run the Python script:

```bash
python ghibli_filter_switcher.py
```

- Raise **both hands** to the camera and hold for **2 seconds** to apply a random filter.
- Press **`q`** to quit the application.

---

## 📁 File Structure

```
ghibli_filter_switcher/
├── ghibli_filter_switcher.py  # Main script
└── README.md                  # Project description
```

---

## 🧠 How It Works

- Uses **MediaPipe Hands** to detect hand landmarks.
- If **2 or more hands** are detected and held up for **2+ seconds**, a filter is randomly selected.
- Filters are implemented with **OpenCV transformations**.

---

## 🖼 Example Filters

| Filter | Preview |
|--------|---------|
| Pencil | ![Pencil Sketch]|
| Sketch | Similar to a grayscale hand-drawn sketch |
| Oil Paint | Stylized brush stroke effect |
| Sepia | Warm brown tone like vintage photos |

---

## 🙌 Credits

- [OpenCV](https://opencv.org/)
- [MediaPipe by Google](https://mediapipe.dev/)
- You, for waving at your webcam like a magician 🪄

---

## 📜 License

This project is licensed under the MIT License. Feel free to fork, modify, and share!

---

