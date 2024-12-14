import pytesseract
from PIL import Image
import cv2



def extract_text(image_path):
    # Loading the image using OpenCV
    image = cv2.imread(image_path)

    # Converting to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to improve OCR accuracy
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Converting to PIL Image format for Tesseract
    processed_image = Image.fromarray(thresh)

    # Extracting text using Tesseract
    extracted_text = pytesseract.image_to_string(processed_image)
    return extracted_text

