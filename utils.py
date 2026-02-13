import csv
import time
import pyautogui as pyg
import mouse
import pandas as pd
from PIL import ImageGrab, Image
from pytesseract import pytesseract
from config import REGIONS, CLICK_POSITIONS, DATA_FILE


def capture_regions():
    extracted_images = []
    for region in REGIONS["options"]:
        img = ImageGrab.grab(region)
        extracted_images.append(img)
    return extracted_images


def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text.strip()


def clean_ocr_output(raw_values):
    cleaned = []
    for value in raw_values:
        try:
            cleaned.append(int(value.split("/")[0]))
        except:
            cleaned.append(value.split("/")[0])
    return cleaned


def determine_position(extracted_values):
    numeric_values = []
    for v in extracted_values:
        if isinstance(v, int):
            numeric_values.append(v)
        else:
            numeric_values.append(9999)

    selected_index = numeric_values.index(min(numeric_values))
    return selected_index


def execute_action(selected_index):
    position = CLICK_POSITIONS.get(selected_index)
    if position:
        pyg.moveTo(position)
        mouse.press()
        time.sleep(1)
        mouse.release()


def read_balance():
    img = ImageGrab.grab(REGIONS["balance"])
    text = pytesseract.image_to_string(img)
    try:
        return int(text.strip())
    except:
        return 0


def log_result(odds_tuple, selected_index, win_index):
    row = [str(odds_tuple), selected_index, win_index]
    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)
