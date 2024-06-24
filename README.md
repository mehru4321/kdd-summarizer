# PubMed Article Summarizer
This Streamlit application allows users to upload a PubMed article in PDF, DOCX, or TXT format and receive a summarized version of the article. Users can choose the quality metric for the summarization, such as coherence, conciseness, or relevance. Additionally, the app provides an option to download the summary.

# Features
Upload and read text from PDF, DOCX, or TXT files.
Preprocess text by removing excessive whitespaces and reference numbers.
Summarize articles using Google's Gemini API.
Choose a quality metric for the summarization.
Choose the style of the summary (formal, informal, technical).
Specify the maximum length of the summary.
Display the original and summarized articles in scrollable, non-editable text areas.
Download the summarized article as a text file.

# Installation
load datasets:
from datasets import load_dataset
dataset = load_dataset("ccdv/pubmed-summarization", "document")

Install the required dependencies:

Copy code

pip install -r requirements.txt

Set up the environment variable for the API key:


for Windows:
Copy code

setx OPENAI_API_KEY "your-api-key-here"

This command will set the OPENAI_API_KEY environment variable for the current session.

for MacOS
export OPENAI_API_KEY='your-api-key-here'

# Usage
Run the Streamlit application:

bash
Copy code
python -m streamlit run web.py
This command directly opens the application in your web browser. You should see the title "PubMed Article Summarizer".

Upload a PubMed article in PDF, DOCX, or TXT format of your choice.

Choose a quality metric for the summarization (coherence, conciseness, relevance).

Choose the style of the summary (formal, informal, technical).

Specify the maximum number of words in the summary.

Click the "Summarize" button to generate the summary.

View the original and summarized articles in the side-by-side scrollable text areas.

Download the summary using the "Download Summary" button.

# Code Explanation
Dependencies

streamlit: For creating the web application.

fitz (PyMuPDF): For reading text from PDF files.

os: For accessing environment variables.

google.generativeai (genai): For using Google's Gemini API for summarization.

plotly.express (px): For creating interactive visualizations.

pandas (pd): For data manipulation and visualization.

# Functions
preprocess_text(text): Removes excessive whitespaces and reference numbers from the text.

extract_text_from_pdf(file): Extracts text from a PDF file.

summarize_article(article): Summarizes the given article using the Gemini API.

# Streamlit Application
The application allows users to upload a PubMed article and choose a quality metric for the summarization.
Upon clicking the "Summarize" button, the article is summarized, and the original and summarized articles are displayed side-by-side in scrollable, non-editable text areas.
The summary can be downloaded as a text file.

 # Example
Upload a PDF, DOCX, or TXT file.
Choose "coherence" as the quality metric.
Choose "formal" as the summary style.
Set the maximum length of the summary to 200 words.
Click "Summarize".
View the original and summarized articles.
Download the summary.
