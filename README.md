# Live-Emotion-Detection-for-Smart-Song-Suggestion

# 🎵 Live Emotion Detection for Smart Song Suggestion

This project is a smart song recommender system that uses **live face emotion detection** to suggest personalized songs via **YouTube**, based on the user's mood, preferred **language**, and **singer**.

---

## 🧠 How It Works

1. The user opens the web app.
2. They enter:
   - Preferred **language** (e.g., Hindi, English)
   - Favorite **singer** (e.g., Arijit Singh)
3. The system opens a **Streamlit interface** that:
   - Captures **live video from webcam**
   - Detects user's facial and hand landmarks using **MediaPipe**
   - Predicts the **emotion** using a trained **Keras model**
4. On clicking **"Recommend me songs"**, it:
   - Creates a **YouTube search query** like:  
     `language + emotion + song + singer`
   - Opens YouTube in the browser with relevant results.

---

## 🚀 Tech Stack

- **Python**
- **MediaPipe** – For real-time face & hand tracking
- **Keras / TensorFlow** – For training & loading the emotion detection model
- **OpenCV** – For video processing
- **Flask** – Web routing
- **Streamlit** – Real-time face emotion detection interface
- **YouTube** – Used for song suggestions via query

---

## 📁 Project Structure

liveEmoji-main/
├── app.py # Flask backend
├── music.py # Streamlit emotion detection logic
├── data_collection.py # Data collection via webcam
├── data_training.py # Model training script
├── inference.py # Run standalone emotion detection
├── model.h5 # Trained Keras model
├── labels.npy # Label names for predictions
├── templates/
│ └── index.html # Web UI
├── static/
│ ├── style.css # Styling
│ └── script.js # JS for animation
├── .gitignore
└── README.md