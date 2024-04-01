import os
import requests
from robocorp.browser import Page
from utilities.abc.browser import Browser
from RPA.Excel.Files import Files as Excel
from pathlib import Path

from .locators import Locators

class Spreadsheet(Browser):
    def __init__(self):
        super(Spreadsheet, self).__init__()

    def fill_spreadsheet(self):
        """
        Main task which solves the RPA challenge!

        Downloads the source data Excel file and uses Playwright to fill the entries inside
        rpachallenge.com.
        """
        try:
            # Reads a table from an Excel file hosted online.
            excel_file = self.download_file(
                Locators.EXCEL_URL, target_dir=Locators.OUTPUT_DIR, target_filename=Locators.FILE_NAME
            )
            excel = Excel()
            excel.open_workbook(excel_file)
            rows = excel.read_worksheet_as_table("Sheet1", header=True)

            # Surf the automation challenge website and fill in information from the table
            #  extracted above.
            page = self.browser.goto(Locators.main_url)
            page.click(Locators.button_start)
            for row in rows:
                self.fill_and_submit_form(row, page=page)
            element = page.locator(Locators.div_congratulations)
            self.browser.screenshot(element)
        finally:
            # A place for teardown and cleanups. (Playwright handles browser closing)
            print("Automation finished!")



    def download_file(self, url: str, *, target_dir: Path, target_filename: str) -> Path:
        """
        Downloads a file from the given URL into a custom folder & name.

        Args:
            url: The target URL from which we'll download the file.
            target_dir: The destination directory in which we'll place the file.
            target_filename: The local file name inside which the content gets saved.

        Returns:
            Path: A Path object pointing to the downloaded file.
        """
        # Obtain the content of the file hosted online.
        response = requests.get(url)
        response.raise_for_status()  # this will raise an exception if the request fails
        # Write the content of the request response to the target file.
        target_dir.mkdir(exist_ok=True)
        local_file = target_dir / target_filename
        local_file.write_bytes(response.content)
        return local_file


    def fill_and_submit_form(self, row: dict, *, page: Page):
        """
        Fills a single form with the information of a single row from the table.

        Args:
            row: One row from the generated table out of the input Excel file.
            page: The page object over which the browser interactions are done.
        """
        field_data_map = {
            "labelFirstName": "First Name",
            "labelLastName": "Last Name",
            "labelCompanyName": "Company Name",
            "labelRole": "Role in Company",
            "labelAddress": "Address",
            "labelEmail": "Email",
            "labelPhone": "Phone Number",
        }
        for field, key in field_data_map.items():
            page.fill(f"//input[@ng-reflect-name='{field}']", str(row[key]))
        page.click("input:text('Submit')")


