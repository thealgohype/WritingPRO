import requests
from bs4 import BeautifulSoup

def get_article(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the article text
        paragraphs = soup.find_all('p')
        article_content = '\n'.join([para.get_text() for para in paragraphs])

        return article_content
    except Exception as e:
        print(f"Failed to load article from {url}: {e}")
        return "Oopsie"
