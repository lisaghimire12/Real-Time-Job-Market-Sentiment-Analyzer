from flask import Flask, request, jsonify
from scraper import extract_job
from link_checker import verify_job_link

app = Flask(__name__)

@app.route("/")
def home():
    return "Fake Job Detection API is running"

@app.route("/analyze", methods=["GET"])
def analyze():

    try:

        url = request.args.get("url")

        if not url:
            return jsonify({"error":"No URL provided"})

        job = extract_job(url)

        result = verify_job_link(job)

        return jsonify({
            "title": job.get("title","Unknown"),
            "company": job.get("company","Unknown"),
            "description": job.get("description","No description found"),
            "verdict": result.get("status","UNKNOWN"),
            "score": result.get("score",0)
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "title":"Error",
            "company":"Error",
            "description": str(e),
            "verdict":"ERROR",
            "score":0
        })
    
if __name__ == "__main__":
    app.run(debug=True)