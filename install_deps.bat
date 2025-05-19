@echo off
echo Installing dependencies...

:: Download Tesseract
echo Downloading Tesseract...
curl -L -o tesseract.exe https://github.com/UB-Mannheim/tesseract/wiki/tesseract-ocr-w64-setup-v5.3.3.20231005.exe
start /wait tesseract.exe

:: Download Poppler
echo Downloading Poppler...
curl -L -o poppler.zip https://github.com/oschwartz10612/poppler-windows/releases/download/v23.01.0-0/Release-23.01.0.zip
powershell -Command "Expand-Archive poppler.zip -DestinationPath poppler"

echo Done installing dependencies.
pause
