# 🧠 Twitter Sentiment Analysis – Brainwave Matrix Solutions Task 2

This project is part of my internship at **Brainwave Matrix Solutions**. It is a complete end-to-end pipeline that performs sentiment analysis on tweets, classifying them into **Positive**, **Neutral**, or **Negative** sentiments.

## 🚀 Project Features

- 📌 Real-world tweet data preprocessing using NLP techniques  
- 📊 Word frequency analysis and visualization using WordClouds and Seaborn  
- 🧠 Sentiment classification using **LinearSVC**  
- 🎯 Model evaluation using F1-score and classification report  
- 💾 Model and vectorizer persistence using `pickle`  
- 🌐 Deployed using **Flask** with a simple HTML/CSS frontend  

## 🛠️ Technologies Used

- Python, Pandas, NumPy  
- NLTK, WordCloud, Seaborn, Matplotlib  
- Scikit-learn, Imbalanced-learn (SMOTE, RandomOverSampler)  
- Flask (for deployment)  
- HTML & CSS (frontend)

## 📂 Project Structure
```
├── notebooks/ # Data cleaning, EDA, and model training
├── model/
│ ├── sentiment_analysis.pkl
│ └── vectorizer.pkl
├── app/
│ ├── app.py # Flask application
│ ├── templates/
│ │ └── index.html
│ └── static/
│ └── style.css
├─ input
  └─ Twitter_Data.csv # Dataset
```
## ⚙️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/MuhammedMahmoud0/Brainwave_Matrix_Intern.git
   cd Brainwave_Matrix_Intern/Social\ Media\ Sentiment\ Analysis

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download NLTK resources (if not already):
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```
4. Run the Flask app:
    ```bash
    cd app
    python app.py
    ```
5. Open in Your Browser:
     
- 🔗 [http://127.0.0.1:5000](http://127.0.0.1:5000)
