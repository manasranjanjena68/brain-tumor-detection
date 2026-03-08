# 🧠 Brain Tumor Detection Using Deep Learning

A web-based application that detects **brain tumors from MRI images** using **Deep Learning and Django**.
Users can upload MRI scans and the system predicts whether a **tumor is present or not**.

---

## 🚀 Features

* 👤 User authentication (Signup / Login / Logout)
* 🧠 Brain tumor detection using a trained Deep Learning model
* 📤 Upload MRI scan images
* 📊 View prediction results instantly
* 📁 Prediction history for users
* 🤖 Chatbot for basic assistance
* 🎨 Clean and responsive web interface

---

## 🛠 Tech Stack

**Frontend**

* HTML
* CSS
* JavaScript

**Backend**

* Django (Python)

**Machine Learning**

* TensorFlow
* Keras
* CNN Model

**Database**

* SQLite

---

## 📂 Project Structure

brain-tumor-detection
│
├── accounts/          # User authentication system
├── chatbot/           # Chatbot functionality
├── core/              # Main prediction logic
├── model/             # ML model and prediction script
├── static/            # CSS, images, and static files
├── templates/         # HTML templates
├── manage.py          # Django management script
└── requirements.txt   # Project dependencies

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

git clone https://github.com/manasranjanjena68/brain-tumor-detection.git

### 2️⃣ Navigate to project folder

cd brain-tumor-detection

### 3️⃣ Create virtual environment

python -m venv .venv

### 4️⃣ Activate virtual environment

Windows:
.venv\Scripts\activate

### 5️⃣ Install dependencies

pip install -r requirements.txt

### 6️⃣ Run migrations

python manage.py migrate

### 7️⃣ Start the server

python manage.py runserver

Open in browser:

http://127.0.0.1:8000/

---

## 📥 Download Model File

The trained model file is not included in the repository because of GitHub size limits.

Download the model from the link below and place it inside:

brain_tumor_detection/model/

File name:

Brain_Tumor.h5

---

## 📸 Screenshots



Example:

* Home Page
* Upload MRI Scan
* Prediction Result
* User Dashboard

---

## 👨‍💻 Author

**Manas Ranjan Jena (Biku)**
📍 Bhadrak, Odisha, India

LinkedIn:
https://www.linkedin.com/in/manas-ranjan-jena/

---

## ⭐ Future Improvements

* Deploy the application online
* Improve model accuracy
* Add Grad-CAM visualization for tumor regions
* Improve chatbot with AI

---

## 📜 License

This project is for **educational and research purposes**.
