import keyboard
import time
from pytesseract import pytesseract
from config import TESSERACT_PATH
from utils import (
    capture_regions,
    extract_text_from_image,
    clean_ocr_output,
    determine_position,
    execute_action,
    read_balance,
    log_result,
)

pytesseract.tesseract_cmd = TESSERACT_PATH


def main_loop():
    while not keyboard.is_pressed("esc"):
        images = capture_regions()

        raw_values = []
        for img in images:
            raw_values.append(extract_text_from_image(img))

        extracted_values = clean_ocr_output(raw_values)

        selected_index = determine_position(extracted_values)

        execute_action(selected_index)

        current_balance = read_balance()

        odds_tuple = tuple(extracted_values)

        log_result(odds_tuple, selected_index, None)

        time.sleep(5)


if __name__ == "__main__":
    main_loop()
