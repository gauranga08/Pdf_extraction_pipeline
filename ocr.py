import pytesseract
from PIL import Image
import logging

# Extract text from image using pytesseract
def image_to_string(image, language):
    try:
        with Image.open(image) as img:
            return pytesseract.image_to_string(img, lang=language)
    except Exception as e:
        logging.error(f"Error during OCR extraction: {e}")
        return ""
