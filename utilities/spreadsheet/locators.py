import os
from pathlib import Path

class Locators:
    FILE_NAME = "challenge.xlsx"
    EXCEL_URL = f"https://rpachallenge.com/assets/downloadFiles/{FILE_NAME}"
    OUTPUT_DIR = Path(os.getenv("ROBOT_ARTIFACTS", "output"))

    main_url = "https://rpachallenge.com/"
    button_start = "button:text('Start')"
    div_congratulations = "css=div.congratulations"
