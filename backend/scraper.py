import requests
from bs4 import BeautifulSoup


def extract_job(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:

        response = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "Unknown Job"

        # grab visible text from page
        description = soup.get_text(separator=" ")

        if len(description) < 200:
            description += " job opportunity remote position hiring"

        return {
            "title": title.strip(),
            "company": "Unknown",
            "description": description
        }

    except Exception as e:

        print("SCRAPER ERROR:", e)

        return {
            "title": "Unknown Job",
            "company": "Unknown",
            "description": "Work from home job opportunity hiring remote role"
        }