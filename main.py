import os
import shutil
import pytesseract
import logging
import argparse
from tkinter import filedialog, Tk, messagebox
from concurrent.futures import ThreadPoolExecutor
from pdf2image import convert_from_path
from PIL import Image

# ======================= CONFIGURATION ==========================
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\Users\user\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

# ========================== LOGGING =============================
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(script_dir, "ocr_log.txt")
logging.basicConfig(
    filename=log_file_path,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ======================= OCR FUNCTIONS ===========================
def extract_text_from_images(folder):
    text = ""
    files = sorted(os.listdir(folder), key=lambda x: int(x.split("_")[1].split(".")[0]))
    
    for image_file in files:
        image_path = os.path.join(folder, image_file)
        try:
            image = Image.open(image_path)
            page_text = pytesseract.image_to_string(image, lang="sin")
            if not page_text.strip():
                logging.warning(f"No text found in: {image_path}")
            text += page_text + "\n\n"
        except Exception as e:
            logging.error(f"Error processing {image_path}: {str(e)}")

    return text

def cleanup(folder):
    try:
        shutil.rmtree(folder)
        print(f"Cleaned up: {folder}")
    except Exception as e:
        logging.error(f"Failed to delete {folder}: {str(e)}")

# ======================= PROCESS EACH PDF ========================
def process_pdf(pdf_path):
    base_folder = os.path.dirname(pdf_path)
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    temp_folder = os.path.join(base_folder, f"temp_{filename}")

    os.makedirs(temp_folder, exist_ok=True)
    print(f"Converting: {filename}.pdf")

    try:
        images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
        for i, image in enumerate(images):
            image_path = os.path.join(temp_folder, f"page_{i+1}.jpg")
            image.save(image_path, "JPEG")
    except Exception as e:
        logging.error(f"Error converting PDF to images: {str(e)}")
        return

    full_text = extract_text_from_images(temp_folder)
    output_txt = os.path.join(base_folder, f"{filename}.txt")
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(full_text)
    print(f"Saved: {output_txt}")

    cleanup(temp_folder)

# ======================= FILE SELECT GUI =========================
def select_files():
    root = Tk()
    root.withdraw()
    pdf_files = filedialog.askopenfilenames(
        title="Select Sinhala PDF files",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not pdf_files:
        messagebox.showinfo("No files", "No PDF files selected.")
        return

    with ThreadPoolExecutor() as executor:
        executor.map(process_pdf, pdf_files)

    messagebox.showinfo("Done", "OCR extraction completed for all files!")
    root.destroy()

# ======================= MAIN ENTRY ==============================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    select_files()
