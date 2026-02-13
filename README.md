# Real-Time OCR-Based Decision Automation System

## Overview

A Python-based automation system that captures predefined screen regions, extracts numeric values using OCR (Tesseract), applies rule-based decision logic, and executes automated UI interactions based on dynamic state.

This project demonstrates:

- Real-time screen processing  
- OCR-based data extraction  
- Structured data parsing  
- Rule-based decision modeling  
- Automated UI interaction workflows  
- Persistent state logging  

---

## Features

- Screen region capture using Pillow (ImageGrab)  
- OCR parsing with Tesseract  
- Configurable screen region mapping  
- Rule-based decision engine  
- Automated UI interaction via PyAutoGUI  
- CSV-based state logging  
- Modular, maintainable architecture  

---

## Architecture

- Screen Capture
- ↓
OCR Extraction
↓
Data Cleaning
↓
Decision Engine
↓
Automated Interaction
↓
Result Logging


---

## Project Structure

.
├── main.py
├── utils.py
├── config.py
├── requirements.txt
└── README.md


- **main.py** – Orchestrates execution loop  
- **utils.py** – Core automation logic  
- **config.py** – Configurable screen regions and constants  
- **requirements.txt** – Python dependencies  

---

## Technologies Used

- Python 3.x  
- Tesseract OCR  
- PyAutoGUI  
- Pillow (PIL)  
- Pandas  
- OpenCV (optional preprocessing)  
- CSV logging  

---

## Installation

### 1. Install Tesseract OCR

Download and install from:

https://github.com/tesseract-ocr/tesseract

After installation, update the path in `config.py`:

`TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"`

---

### 2. Install Python Dependencies

Run:

pip install -r requirements.txt


---

### 3. Run the Application

python main.py


Press `ESC` to terminate execution.

---

## Configuration

Screen regions and click coordinates are configurable in `config.py`:

REGIONS = {
"options": [...],
"balance": (...),
"result": (...)
}


This allows adaptation to different screen layouts without modifying core logic.

---

## Key Concepts Demonstrated

- Real-time automation systems  
- OCR-based structured data extraction  
- Data normalization and cleaning  
- Rule-based selection algorithms  
- Modular Python architecture  
- Stateful logging using CSV  
- Config-driven design pattern  

---

## Limitations

- Designed for fixed screen resolution layouts  
- OCR accuracy depends on image clarity  
- Windows-specific Tesseract path (configurable)  

---

## Future Improvements

- Add structured logging module  
- Add retry logic for OCR failures  
- Add OpenCV preprocessing for improved OCR accuracy  
- Convert to GUI-based configuration interface  
- Add unit tests for decision logic  

---

## License

This project is provided for educational and automation demonstration purposes.
