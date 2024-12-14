# OCR Receipt Manager

OCR Receipt Manager is a Python-based application that uses Optical Character Recognition (OCR) to extract text from images of receipts. This project provides an easy-to-use interface for uploading receipt images, processing them through OCR, and displaying the extracted text.

## Features
- **Upload Receipt Images**: Allows users to upload receipt images in various formats (e.g., PNG, JPEG).
- **OCR Processing**: Utilizes Tesseract OCR engine to extract text from the uploaded images.
- **Text Display**: Displays the extracted text from the receipt directly on the web interface.
- **Flask Web Application**: Built using Flask to provide a simple web interface for users.

## Requirements

Before running the project, make sure you have the following installed:

- **Python 3.x** (preferably the latest version)
- **Tesseract OCR**: You need to have Tesseract OCR installed on your machine. You can download it from [here](https://github.com/tesseract-ocr/tesseract).
- **Flask**: For running the web application.
- **pytesseract**: A Python wrapper for Tesseract.
- **Pillow**: Python Imaging Library for handling images.

You can install the necessary Python packages using the following:

```bash
pip install -r requirements.txt

