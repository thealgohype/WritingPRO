import streamlit as st
import mechanicalsoup

# Function to fetch and parse text from the URL
def fetch_text_from_url(url):
    # Create a browser object
    browser = mechanicalsoup.StatefulBrowser()

    # Open the URL
    browser.open(url)

    # Get the page content
    page = browser.get_current_page()

    # Extract text from the page
    text = page.get_text()

    return text

# Streamlit app
def main():
    st.title("URL Text Parser")

    # Input URL from the user
    url = st.text_input("Enter the URL:")

    if url:
        try:
            # Fetch and display the text from the URL
            text = fetch_text_from_url(url)
            st.write(text)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()