from flask import Flask, render_template, request
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import joblib

nltk.download('stopwords')

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Preprocessing function (same as Jupyter)
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def preprocess(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [ps.stem(word) for word in text if word not in stop_words]
    return ' '.join(text)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_text = request.form['news']
        processed = preprocess(input_text)
        vectorized = vectorizer.transform([processed])
        prediction = model.predict(vectorized)

        result = "🟢 Real News" if prediction[0] == 1 else "🔴 Fake News"
        return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
