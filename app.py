import streamlit as st
import pytesseract
from pdf2image import convert_from_bytes
import numpy as np
import cv2
import json

# Set the Tesseract executable path for Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set page config
# st.set_page_config(page_title="PDF OCR Extractor", layout="centered")
st.title("Multi-page PDF OCR Extractor")
st.write("Upload a PDF and extract text from all pages using Tesseract OCR.")

# ✅ This must show!
uploaded_pdf = st.file_uploader("Upload PDF File", type=["pdf"])

if uploaded_pdf:
    st.info("Processing PDF...")
    pages = convert_from_bytes(uploaded_pdf.read())
    st.success(f"{len(pages)} page(s) found.")

    results = []
    for i, page in enumerate(pages):
        image = np.array(page)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        text = pytesseract.image_to_string(thresh)

        results.append({
            "page": i + 1,
            "text": text.strip()
        })

        st.image(page, caption=f"Page {i+1}", use_column_width=True)
        st.text_area(f"Text from Page {i+1}", text.strip(), height=200)

    st.markdown("### JSON Output")
    st.json(results)
