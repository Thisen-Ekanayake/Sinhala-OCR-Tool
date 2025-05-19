import os
from PIL import Image
import pytesseract

def extract_text_from_images(folder):
    full_text = ""

    image_files = sorted(os.listdir(folder), key=lambda x: int(x.split('_')[-1].split('.')[0]))

    for i, image_name in enumerate(image_files):
        image_path = os.path.join(folder, image_name)

        try:
            text = pytesseract.image_to_string(Image.open(image_path), lang='sin', config='--psm 6')
            if len(text.strip()) < 15:
                print(f"Page {i+1} returned short text. Retrying...")
                text = pytesseract.image_to_string(Image.open(image_path), lang='sin', config='--psm 4')
            full_text += f"\n--- Page {i+1} ---\n{text.strip()}\n"
        except Exception as e:
            print(f"OCR failed on page {i+1}: {e}")

    return full_text

def cleanup(folder):
    try:
        for file in os.listdir(folder):
            os.remove(os.path.join(folder, file))
        os.rmdir(folder)
        print(f"Cleaned up: {folder}")
    except Exception as e:
        print(f"Cleanup failed: {e}")
