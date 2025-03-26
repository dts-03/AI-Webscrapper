import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return "Failed to retrieve the webpage."

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract only the visible text from the page
        paragraphs = soup.find_all("p")
        scraped_text = " ".join([para.get_text() for para in paragraphs])

        return scraped_text if scraped_text else "No readable content found."
    
    except Exception as e:
        return f"Error: {str(e)}"
