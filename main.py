import streamlit as st
from chain import setup_stuff, writingpro_chain
from utils import get_article
from bs4 import BeautifulSoup
import streamlit.components.v1 as components

setup_stuff()

# Define the Streamlit app
st.set_page_config(page_title="WritingPRO", page_icon=":writing_hand:", layout="wide")
st.subheader("WritingPRO : Your Newsletter Assistant")

article_url = st.text_input("Enter the URL of the blog/article you like")

if article_url:
    try:
        article_content = get_article(article_url)
        if article_content != "Oopsie":
            # st.write("Article Content:")
            # st.write(article_content)
            summary, outline, generated_newsletter = writingpro_chain(article_url)
            st.write("Summary:")
            st.write(summary)
            st.write("Outline:")
            st.write(outline)

            # Debug: Check the type of newsletter before writing it to Streamlit
            #print(f"Newsletter Type: {type(generated_newsletter)}")

            # Ensure the newsletter is correctly formatted for Streamlit
            if generated_newsletter:
                
                import streamlit as st
                import os

                # Save the generated newsletter to an HTML file
                newsletter_filename = "generated_newsletter.html"
                with open(newsletter_filename, "w", encoding="utf-8") as file:
                    file.write(generated_newsletter)

                # Provide a download button for the HTML file
                with open(newsletter_filename, "rb") as file:
                    btn = st.download_button(
                        label="Download Newsletter as HTML",                       data=file,
                        file_name=newsletter_filename,
                        mime="text/html")

                st.write("Newsletter:")
                st.write(generated_newsletter, unsafe_allow_html= True)  # prettify for better readability
            else:
                st.write("Failed to generate newsletter. Please try again.")
        else:
            st.write("Failed to load the article. Please check the URL and try again.")
    except Exception as e:
        st.write(f"An error occurred: {e}")

st.divider()
