import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

MODEL_PATH = "fake_job_model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"

def train_model():
    
    # Load dataset
    data = pd.read_csv("fake_job_postings.csv")

    # Handle missing values
    data = data.fillna("")

    # Combine important text fields
    data['text'] = data['title'] + " " + data['description'] + " " + data['requirements']

    # Features and labels
    X = data['text']
    y = data['fraudulent']

    # Convert text → numerical features
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    X_vec = vectorizer.fit_transform(X)

    # Train model
    model = MultinomialNB()
    model.fit(X_vec, y)

    # Save model and vectorizer
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

    print("✅ Model trained and saved")


# Load model once (better performance)
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
except:
    model = None
    vectorizer = None


def predict_job(text):

    if model is None or vectorizer is None:
        return "Model not trained"

    # Convert text → vector
    text_vec = vectorizer.transform([text])

    # Predict
    prediction = model.predict(text_vec)[0]

    if prediction == 1:
        return "Fake Job"
    else:
        return "Real Job"


if __name__ == "__main__":
    train_model()