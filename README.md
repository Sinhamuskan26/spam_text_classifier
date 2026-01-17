# 📧 Spam Email / Message Detector

A production‑ready **Spam Detection application** built using **Machine Learning (NLP)** and deployed with a simple user interface. The system classifies a given message as **Spam** or **Not Spam** using a trained text‑classification model.

---

## 🚀 Project Overview

Spam messages are a common problem in emails and SMS. This project uses **Natural Language Processing (NLP)** techniques and **Machine Learning** to automatically detect spam messages based on their text content.

The project follows **industry‑standard practices** such as:

* Proper train–test split
* Feature extraction using vectorizers
* Model persistence
* Clean inference pipeline
* UI for real‑time prediction

---

## 🧠 Model Details

* **Algorithm:** Multinomial Naive Bayes / Logistic Regression (text‑based classifier)
* **Feature Extraction:** CountVectorizer / TF‑IDF Vectorizer
* **Pipeline:** Vectorizer + Model combined into a single pipeline
* **Output:** Binary classification

  * `0` → Not Spam
  * `1` → Spam

---

## 🗂️ Project Structure

```
spam_email_predictor/
│
├── app.py                  # Streamlit application (UI)
├── spam_pipeline.pkl       # Saved ML pipeline (model + vectorizer)
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── spam.csv                # Dataset (optional)
```

---

## 🖥️ User Interface

The application provides a simple interface where:

1. The user enters a message
2. Clicks the **Check Spam** button
3. Instantly sees whether the message is **Spam** or **Not Spam**

The UI is built using **Streamlit** for fast and interactive deployment.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <repository-url>
cd spam_email_predictor
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python -m streamlit run app.py
```

The app will open automatically in your browser.

---

## 🧪 Example Input

```
Congratulations! You have won 200k. Click the link to claim now.
```

### Output

```
🚨 SPAM
```

---

## 📦 Model Persistence

The trained model and vectorizer are saved together using **joblib** as a pipeline:

```python
joblib.dump(pipeline, "spam_pipeline.pkl")
```

This ensures consistent preprocessing and prediction during deployment.

---

## 🧠 Key Learnings

* Importance of proper text preprocessing
* Avoiding data leakage during training
* Handling class imbalance in classification problems
* Difference between demo and production‑level ML systems

---

## 🔮 Future Improvements

* Add probability/confidence score
* Use character n‑grams for better spam detection
* Deploy using FastAPI + Docker
* Add logging and monitoring
* Support email file uploads

---

## 🧑‍💻 Author

Developed as a learning and production‑ready NLP project.

---

## 📜 License

This project is for educational purposes and open for extension and improvement.
