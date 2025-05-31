# Sinhala PDF OCR Tool

A simple, standalone GUI application to convert **scanned Sinhala and English PDFs** into clean `.txt` files using Tesseract OCR.

Built for ease of use - even for non-technical users—this tool uses Python, Tesseract, and Poppler to extract meaningful text from image-based documents, including mixed-language content (Sinhala + English). 

Perfect for digitizing school textbooks, government gazettes, Hansard reports, and other printed material in Sinhala or Sinhala-English formats.

[![Version](https://img.shields.io/badge/version-v1.1.0-blue)](https://github.com/Thisen-Ekanayake/sinhala-ocr-tool/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Download](https://img.shields.io/badge/Download-.exe-blue?style=flat&logo=windows)](https://github.com/Thisen-Ekanayake/sinhala-ocr-tool/releases/download/v1.1.0/Sinhala-OCR-Tool.exe)


## Features
- File picker to select one or more PDF files (via GUI)
- Sinhala OCR powered by Tesseract
- Automatic PDF to image conversion via [Poppler]
- Outputs clean, readable .txt files (one per PDF)
- Cleans up temporary files after conversion
- Built-in logging for error tracking (ocr_log.txt)

## Installation
Since OCR requires external dependencies, a few manual steps are needed:

**1. Download Dependencies**
- These are already included with the .exe if you're using the packaged version!

| Dependency    | Download Link                                                                           |
| ------------- | --------------------------------------------------------------------------------------- |
| **Tesseract** | [Tesseract OCR for Windows](https://github.com/UB-Mannheim/tesseract/wiki)              |
| **Poppler**   | [Poppler for Windows (ZIP)](https://github.com/oschwartz10612/poppler-windows/releases) |


**After installing:**

- Note the Tesseract installation path *(e.g.,)*
```
C:\Program Files\Tesseract-OCR\tesseract.exe
```
- Extract the Poppler ZIP and note the bin folder path *(e.g.,)*
```
...\poppler-xx\Library\bin
```

**2. (If using source code) Install Python requirements**
```
pip install -r requirements.txt
```

## How to Use
**Executable (.exe) version:**
- Run the .exe file (double-click)
- Use the file picker to select one or more PDF files
- Wait for the extraction to complete
- The output .txt files will appear in the same folder as your PDFs

**Python version:**
```
python main.py
```
- Optionally *(to enable verbose logs)*:
```
python main.py --debug 
```

## Output Format
- Each file is in .txt format.

## Known Issues
- Currently does not auto-install Tesseract or Poppler
- OCR accuracy may vary depending on scan quality

## Future Improvements
- Automatic installer for Tesseract and Poppler
- Add progress bar in the GUI
- Option to choose output format (.txt, .docx)
- Full Unicode normalization and font fallback suggestions

## Author
- Thisen Ekanayake.

## License
- MIT License – free to use, modify, and share.