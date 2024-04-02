import os
from pathlib import Path
from utilities.abc.vaults import Vault

vault = Vault()

class Locators:
    FILE_NAME = "challenge.xlsx"
    EXCEL_URL = f"https://rpachallenge.com/assets/downloadFiles/{FILE_NAME}"
    OUTPUT_DIR = Path(os.getenv("ROBOT_ARTIFACTS", "output"))

    #main_url = "https://rpachallenge.com/"
    main_url = vault.url
    button_start = "button:text('Start')"
    div_congratulations = "css=div.congratulations"
