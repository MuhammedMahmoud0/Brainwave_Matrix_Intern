from flask import Flask, render_template, request
import pickle
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

app = Flask(__name__)

# Load model and vectorizer
with open("../model/sentiment_analysis.pkl", "rb") as f:
    model = pickle.load(f)

with open("../model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Preprocessing function (minimal, simplified)
def preprocess(text):
    text = re.sub(r"@[\w]+", "", text)  # Remove mentions
    #text = re.sub(r"#[\w]+", "", text)  # Remove hashtags
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove punctuation/numbers
    text = text.lower()
    text = " ".join([word for word in text.split() if len(word) > 3])

    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]

    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]

    return " ".join(tokens)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        user_input = request.form["tweet"]
        cleaned = preprocess(user_input)
        vectorized = vectorizer.transform([cleaned])
        pred = model.predict(vectorized)[0]
        prediction = "Positive 😊" if pred == 1 else "Neutral 😐" if pred == 0 else "Negative 😠"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
