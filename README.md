# 🧠 Fake News Detection App 🔍📰  
![fake-news-banner](https://github.com/user-attachments/assets/fake-news-banner.jpg)

📌 An NLP-powered web application that detects whether a piece of news is **real or fake**, using machine learning and Flask – deployed on Render.

---

## 📖 Project Overview

### ❓ Why This Project?
In an era of viral misinformation, fake news can spread rapidly and influence public opinion. This project aims to solve that problem using Natural Language Processing (NLP) and machine learning to **detect fake news with high accuracy**.

This is an **end-to-end machine learning project**, from data preprocessing and model building to deployment using Flask and Render.

---

## 🚀 Features

- 🧠 **Real-time news classification** using Logistic Regression
- ✂️ **Text preprocessing with NLTK** – stopword removal, stemming
- 🔎 **TF-IDF Vectorization** for feature extraction
- ✅ Web interface with Flask + HTML
- ☁️ Hosted on **Render** for live prediction

---

## 📊 Dataset

- 📁 `Fake.csv` → 23,481 fake news articles  
- 📁 `True.csv` → 21,417 real news articles  
- 🔁 Combined and labeled:
  - `0` = Fake
  - `1` = Real

These are pre-cleaned news articles from Kaggle used for training the model.

---

## ⚠️ Limitation: Works Best on Dataset News

> ℹ️ **Note:** This model performs with high accuracy on the dataset it was trained on. If you input **real-world or live news** articles (e.g., copied from current news websites), predictions may not be accurate due to style/language differences.

### ✅ Still Valuable Because:
- Demonstrates strong grasp of **NLP + ML techniques**
- Shows ability to build, train, and deploy real applications
- End-to-end implementation with deployment

---

## 📈 Model Performance

- ✅ **Accuracy**: 98.59%
- 📊 **Classification Report**:
  - Precision (Fake): 0.99
  - Precision (Real): 0.98
- 📉 **Confusion Matrix**:
  - [[4632 78]
  - [ 46 4224]]


---

## 🛠 Tech Stack

| Category     | Tools Used                             |
|--------------|----------------------------------------|
| Language     | Python                                 |
| NLP          | NLTK, TF-IDF, Scikit-learn             |
| Model        | Logistic Regression                    |
| Web Framework| Flask                                  |
| Deployment   | Render                                 |
| Frontend     | HTML + CSS (basic form)                |

---

## 📸 UI Preview

| 🔤 Input Form | ✅ Output Result |
|--------------|------------------|
| ![input-news](https://github.com/user-attachments/assets/input.png) | ![output-result](https://github.com/user-attachments/assets/output.png) |

---

## 📦 Project Structure

News_detection/ 

├── app.py # Flask App 

├── model.pkl # Trained Logistic Regression model

├── vectorizer.pkl # TF-IDF vectorizer 

├── templates/ 

  │ └── index.html # HTML frontend 
  
├── requirements.txt # Python dependencies

├── Procfile

└── README.md # Project Documentation


## 💻 How to Run Locally


git clone https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector

pip install -r requirements.txt

python app.py

Then open your browser and go to:

http://localhost:5000

## 🧪 Try It Yourself – Sample Inputs

> **Headline:** “NASA confirms presence of water molecules on sunlit moon areas.”  
🟢 **Output:** Real

> **Headline:** “Obama caught operating secret deep-state bunker in Hawaii.”  
🔴 **Output:** Fake

---

## 🧠 Future Improvements

- 🧾 **Integrate live news scraping via APIs** for real-time prediction  
- 📈 **Upgrade to transformer-based models** (e.g., BERT) for better generalization  
- 🌍 **Multi-language news detection support**  
- 🖼 **Add rich visual analytics dashboard** for admins  

---

## 🙋‍♂️ About Me

**Nishant Kumar**  
🎓 Data Scientist | Python | SQL | NLP | CV | Machine Learning  
📫 [LinkedIn](https://www.linkedin.com/in/your-link/)  
🌐 Portfolio: Coming Soon  

---

## 🌐 Live Demo

👉 Visit the app here: [🔗 Render App Link](https://your-render-link.onrender.com)

---

⭐ **Give this repo a star** if you found it helpful!  
📬 Feel free to fork, open issues, or contribute.
