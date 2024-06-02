import streamlit as st
from chain import setup_stuff, writingpro_chain 


#wokring for direct links only
import requests
from bs4 import BeautifulSoup

setup_stuff()

def get_article(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the article text
        # Here, we look for common tags that contain article text. This can be adjusted as needed.
        paragraphs = soup.find_all('p')
        article_content = '\n'.join([para.get_text() for para in paragraphs])

        return article_content
    except Exception as e:
        print(f"Failed to load article from {url}: {e}")
        return "Oopsie"



# Define the Streamlit app

st.set_page_config(page_title="WritingPRO", page_icon=":writing_hand:", layout="wide")
st.subheader("WritingPRO : Your Newsletter Assistant")

article_url = st.text_input("Enter the URL of the blog/article you like")

if article_url:
    try:
        article_content = get_article(article_url)
        if article_content != "Oopsie":
            st.write("Article Content:")
            st.write(article_content)
            summary, outline, newsletter = writingpro_chain(article_url)
            st.write("Summary:")
            st.write(summary)
            st.write("Outline:")
            st.write(outline)
            st.write("Newsletter:")
            st.write(newsletter)          
        else:
            st.write("Failed to load the article. Please check the URL and try again.")
    except Exception as e:
        st.write(f"An error occurred: {e}")

st.divider()

