# Multi-page PDF OCR Extractor (Streamlit App)

A lightweight, browser-based tool built with **Streamlit** that lets us upload multi-page PDFs (such as scanned tickets or invoices), extract text from each page using **Tesseract OCR**, and view the results in a clean, structured JSON format.

---

## Features

- Upload **multi-page PDFs**
- Convert each page into an image using `pdf2image`
- Apply **Tesseract OCR** to extract text from each page
- Display results per page
- Show all extracted content as **JSON output**

> Ideal for scanned transport tickets, weighbridge slips, receipts, etc.

---

## Tech Stack

- Python 3.8+
- Streamlit
- Tesseract OCR
- Poppler (for PDF to image conversion)
- OpenCV
- Pillow
- pdf2image

---

## Installation

### 1. Clone the Repository
    git clone https://github.com/your-username/pdf-ocr-streamlit.git
    cd pdf-ocr-streamlit

### 2. Create Virtual Environment

    python -m venv venv
    venv\Scripts\activate 

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Run the command 

    streamlit run app.py

## Demo

  [Demo]((https://raw.githubusercontent.com/himanshisharmaa/OCR-PDF/main/demo.gif))


  
