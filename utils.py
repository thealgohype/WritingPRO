import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
def get_article(url):
    # Try to fetch the content of the URL
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error on bad status
    except requests.RequestException as e:
        return str(e)
    # Check if the content type is HTML
    if 'text/html' in response.headers.get('Content-Type', ''):
        return extract_text_from_html(response.text)
    # Check if the content type is XML for RSS/Atom feeds
    elif 'xml' in response.headers.get('Content-Type', ''):
        return extract_text_from_feed(response.text)
    else:
        return "Unsupported content type"
def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find all text within the webpage
    # Remove script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()
    # Get text
    text = soup.get_text()
    # Break into lines and remove leading/trailing whitespace on each
    lines = (line.strip() for line in text.splitlines())
    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # Drop blank lines and join the text with space
    text = ' '.join(chunk for chunk in chunks if chunk)
    return text
def extract_text_from_feed(feed_content):
    feed = feedparser.parse(feed_content)
    text = ''
    for entry in feed.entries:
        text += entry.title + "\n" + entry.description + "\n"
    return text
