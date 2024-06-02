import streamlit as st
from chain import setup_stuff, writingpro_chain
from utils import get_article
from bs4 import BeautifulSoup

setup_stuff()

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

            # Debug: Check the type of newsletter before writing it to Streamlit
            print(f"Newsletter Type: {type(newsletter)}")

            # Ensure the newsletter is correctly formatted for Streamlit
            if isinstance(newsletter, BeautifulSoup):
                st.write("Newsletter:")
                st.write(newsletter.prettify())  # prettify for better readability
            else:
                st.write("Failed to generate newsletter. Please try again.")
        else:
            st.write("Failed to load the article. Please check the URL and try again.")
    except Exception as e:
        st.write(f"An error occurred: {e}")

st.divider()
