import os
import shutil
import pytesseract
from tkinter import filedialog, Tk, messagebox
from concurrent.futures import ThreadPoolExecutor
from pdf2image import convert_from_path
from utils import extract_text_from_images, cleanup

# Path to Tesseract & Poppler
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\Users\user\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin"

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def process_pdf(pdf_path):
    base_folder = os.path.dirname(pdf_path)
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    temp_folder = os.path.join(base_folder, f"temp_{filename}")

    os.makedirs(temp_folder, exist_ok=True)
    print(f"📄 Converting: {filename}.pdf")

    # Convert PDF pages to images
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    for i, image in enumerate(images):
        image.save(os.path.join(temp_folder, f"page_{i+1}.jpg"), "JPEG")

    # OCR each image
    full_text = extract_text_from_images(temp_folder)

    # Save as .txt file
    output_txt = os.path.join(base_folder, f"{filename}.txt")
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(full_text)
    print(f"✅ Saved: {output_txt}")

    # Cleanup
    cleanup(temp_folder)

def select_files():
    root = Tk()
    root.withdraw()
    pdf_files = filedialog.askopenfilenames(title="Select Sinhala PDF files", filetypes=[("PDF Files", "*.pdf")])

    if not pdf_files:
        messagebox.showinfo("No files", "No PDF files selected.")
        return

    with ThreadPoolExecutor() as executor:
        executor.map(process_pdf, pdf_files)

    messagebox.showinfo("Done", "OCR extraction completed for all files!")

if __name__ == "__main__":
    select_files()
