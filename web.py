import streamlit as st
import fitz  # PyMuPDF->read text from pdf
import os # get api
import google.generativeai as genai
import plotly.express as px
import pandas as pd


def preprocess_text(text):
    import re
    text = re.sub(r'\s+', ' ', text)   #removes whitespaces--> tabs, empty lines etc
    text = re.sub(r'\[[0-9]+\]', '', text)  #removes line refernces eg [0] or [1]
    return text.strip()



def extract_text_from_pdf(file):  #reads text from pdf
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)  
        text += page.get_text()
    return text

def summarize_article(article):
    my_api_key = os.getenv("API_KEY")
    try:
        # Set the API Key
        genai.configure(api_key=my_api_key)

        # Loading the Gemini Model for summarization
        model = genai.GenerativeModel('gemini-pro')

        prompt = (
            f"Summarize the following article in {summary_style} style and in a less than {max_length} words, "
            f":\n\n{article}\n\n"
          
        )
        response = model.generate_content([prompt])
        summary = response.text

        

        return summary.strip()
    
    except Exception as err:
        st.error(f"An error occurred: {err}")
    return "An error occurred while summarizing the article."

st.title("PubMed Article Summarizer")

st.write("Upload a PubMed article to get a summarized version.")
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])


# Users to choose the summary style
summary_style = st.selectbox(
    "Choose the summary style:",
    ["formal", "informal", "technical"]
)

# Users to specify the maximum length of the summary
max_length = st.number_input(
    "Specify the maximum number of words in the summary:", min_value=10, max_value=1050, value=150
)


if uploaded_file is not None:
    try:
        article = extract_text_from_pdf(uploaded_file)
        preprocessed=preprocess_text(article)
        if st.button("Summarize"):
            summary = summarize_article(preprocessed)

            col1, col2 = st.columns([1,1])
            with col1:
                st.subheader("Original Article")
                st.markdown(
                    f"""
                    <div style="height: 400px; width: 100%; overflow-y: scroll; border: 1px solid #ccc; padding: 10px;">
                        <pre>{article}</pre>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col2:
                st.subheader("Summarized Article")
                st.markdown(
                    f"""
                    <div style="height: 400px; width: 100%; overflow-y: scroll; border: 1px solid #ccc; padding: 10px;">
                        <pre>{summary}</pre>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            st.download_button(
            label="Download Summary",
            data=summary,
            file_name="summary.txt", #name of the downloaded file.
            mime="text/plain",
            )
            

    except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")
