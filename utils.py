import os
import pytesseract
import shutil
from PIL import Image

def extract_text_from_images(folder_path):
    full_text = ""
    for img_file in sorted(os.listdir(folder_path)):
        if img_file.endswith(".jpg"):
            img_path = os.path.join(folder_path, img_file)
            text = pytesseract.image_to_string(Image.open(img_path), lang="sin")  # Tesseract must support Sinhala
            full_text += text + "\n"
    return full_text

def cleanup(folder_path):
    shutil.rmtree(folder_path)
    print(f"Cleaned up: {folder_path}")
