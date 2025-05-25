<<<<<<< HEAD
# ai-npc-behavior-system
AI-powered dynamic NPC system using a trained ML model and Flask API to interact with Unity
=======
# 🧠 AI-Powered NPC Behavior System

This project trains a machine learning model to predict how NPCs (non-player characters) should respond to player actions like **Attack**, **Help**, **Trade**, or **Ignore**. It includes a Flask API to serve real-time responses for game integration (e.g. with Unity).

---

## 📦 Project Structure

├── model/ # Trained model and encoders
│ ├── npc_behavior_model.pkl
│ ├── encoder.pkl
│ ├── response_encoder.pkl
│ └── interaction_encoder.pkl
├── api/
│ ├── serverr.py # Flask server
│ ├── testing.py # API test script
│ └── requirements.txt
├── training/
│ ├── train_npc_ai.py
│ └── model_train.py
├── README.md
└── .gitignore


---

## 🚀 How to Run

### 1. Install dependencies
```bash
cd api
pip install -r requirements.txt


2. Start the Flask API server

python serverr.py

3. Test the API

python testing.py
>>>>>>> 398e256 (Initial commit - AI-Powered NPC Behavior System)
