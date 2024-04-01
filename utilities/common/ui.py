import os
import time
import logging

from RPA.HTTP import HTTP
from selenium.common.exceptions import NoSuchWindowException

from .browser import Browser

class Ui(Browser):
    def __init__(self):
        super(Ui, self).__init__()
        
    def switch_to_x_window(self, window_contains_string: str, timeout: int = 30):
        logging.info(f"Switch to '{window_contains_string}' window")
        elapsed_time = 0
        while elapsed_time < timeout:
            for window in self.browser.get_window_titles():
                if window_contains_string in window:
                    try:
                        self.browser.switch_window(window)
                        self.current_window_name = window
                        logging.info(f"Switched to '{window_contains_string}' window")
                        return True
                    except NoSuchWindowException:
                        logging.info("Window closed while trying to switch to it.")
            elapsed_time += 1
        logging.info(
            f"Did not switch to '{window_contains_string}' window. Window titles: {self.browser.get_window_titles()}"
        )
        return
    
    def download_file(self, url: str):
        http = HTTP()
        http.download(url=url, overwrite=True)
    
    def wait_for_file(self, path, timeout=180):
        elapsed_time = 0
        while elapsed_time < timeout:
            if os.path.isfile(path):
                return True
            time.sleep(1)
            elapsed_time += 1
        return False
    
    def change_to_frame(self, frame_xpath: str):
        self.browser.unselect_frame()
        self.browser.wait_until_element_is_visible(frame_xpath, timeout=60)
        iframe = self.browser.find_element(frame_xpath)
        self.browser.select_frame(iframe)

    

