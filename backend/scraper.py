import requests
from bs4 import BeautifulSoup


def extract_job(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("title").text if soup.find("title") else "Unknown Job"

    description = soup.get_text()

    job = {
        "title": title,
        "company": "Unknown",
        "description": description
    }

    return job