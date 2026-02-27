Intrusion Detection System (AI-Based)
📌 Project Overview

This project is an AI-based Intrusion Detection System (IDS) that analyzes incoming network traffic and detects whether the request is normal or malicious (attack).
The system uses a machine learning model in the backend and provides a web-based interface for users to test and visualize results.

🎯 Features
🔍 Detects malicious vs normal traffic
🤖 AI/ML-based classification
🌐 Simple web interface (Frontend + Backend)
📊 Displays system statistics:

Total Requests
Attacks Detected
Normal Traffic

⚡ Real-time detection on button click

🏗️ Project Structure
ids_project/
│
├── backend/
│   ├── app.py              # Flask backend
│   ├── model.pkl           # Trained ML model
│   ├── scaler.pkl          # Preprocessing scaler
│
├── frontend/
│   ├── index.html          # UI page
│   ├── style.css           # Styling
│   ├── script.js           # API handling
│
└── README.md
⚙️ Technologies Used

Frontend: HTML, CSS, JavaScript
Backend: Flask (Python)
Machine Learning: Scikit-learn
Data Processing: NumPy, Pandas

🔄 How It Works (System Flow)
User enters input data (or clicks detection)
Frontend sends request to backend API

Backend:
Loads trained ML model
Applies preprocessing (scaling)
Predicts result (Attack / Normal)
Backend returns result to frontend

Frontend displays:
Prediction result
Updated statistics

🧠 Backend Logic (Simplified)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['features']
    
    scaled_data = scaler.transform([data])
    prediction = model.predict(scaled_data)

    return jsonify({
        "result": "Attack" if prediction[0] == 1 else "Normal"
    })
🎨 Frontend Behavior
When user clicks "Run Detection":
A request is sent to backend /predict
Response is received
UI updates dynamically:

Example Output:
Total Requests: 120
Attacks Detected: 34
Normal Traffic: 86

📊 Output Explanation (For Viva)
Total Requests → Total number of times detection was run
Attacks Detected → Number of malicious predictions
Normal Traffic → Safe network requests
👉 The system continuously updates these values based on predictions.
🧪 Preprocessing
Before prediction:
Input data is scaled using StandardScaler
Ensures consistent model performance
Same preprocessing used as training phase
▶️ How to Run the Project
1️⃣ Install Dependencies
pip install flask numpy pandas scikit-learn
2️⃣ Run Backend
cd backend
python app.py
3️⃣ Run Frontend

Open index.html in browser
❗ Common Errors
🔴 Error:
ModuleNotFoundError: No module named 'flask'
✅ Solution:
pip install flask
📈 Future Improvements
📂 CSV file upload support
📊 Graph visualization (charts)

🔐 User authentication
☁️ Deployment (AWS / Render / Railway)
⚡ Real-time packet capture
🎓 Viva Explanation (Short)
This project is an AI-based IDS that detects malicious traffic using a trained ML model. The frontend sends user input to a Flask backend, which preprocesses the data, predicts using the model, and returns results. The system also maintains real-time statistics of total requests, attacks, and normal traffic.

⚠️ Improvements possible (UI, CSV upload, deployment)

👉 So your project is WORKING but NOT 100% COMPLETE yet — you still have scope to upgrade.
