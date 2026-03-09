import requests
from bs4 import BeautifulSoup
from fake_job_model import predict_job


def scan_jobs():

    api = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(api, headers=headers)

    jobs = response.json()[1:]  # skip metadata

    suspicious_jobs = []

    for job in jobs[:100]:   # scan first 100 jobs

        title = job.get("position", "")
        company = job.get("company", "")
        description_html = job.get("description", "")

        soup = BeautifulSoup(description_html, "html.parser")
        description = soup.get_text()

        prediction = predict_job(description)

        if prediction == "Fake Job":

            suspicious_jobs.append({
                "title": title,
                "company": company,
                "risk": "HIGH"
            })

    return suspicious_jobs