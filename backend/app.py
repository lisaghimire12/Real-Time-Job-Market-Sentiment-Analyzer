from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import extract_job
from fake_job_model import predict_job
from sentiment import analyze_sentiment

app = Flask(__name__)
CORS(app)

# store last job description for sentiment
last_job_description = ""


@app.route("/analyze")
def analyze():

    global last_job_description

    try:

        url = request.args.get("url")

        if not url:
            return jsonify({"error": "No URL provided"})

        job = extract_job(url)

        if job is None:
            return jsonify({"error": "Could not fetch job data"})

        description = job.get("description", "")

        # save description for sentiment analysis
        last_job_description = description

        prediction = predict_job(description)

        return jsonify({
            "title": job.get("title"),
            "company": job.get("company"),
            "description": description,
            "ml_prediction": prediction
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({"error": str(e)})


@app.route("/sentiment")
def sentiment():

    global last_job_description

    sentiment_result = analyze_sentiment(last_job_description)

    return jsonify({
        "sentiment": sentiment_result
    })


if __name__ == "__main__":
    app.run(debug=True)