from abc import ABC
from RPA.Browser.Selenium import Selenium


class Browser(ABC):
    def __init__(self):
        self.browser = Selenium()