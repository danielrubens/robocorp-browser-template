from abc import ABC
from robocorp import browser


class Browser(ABC):
    def __init__(self):
        self.browser = browser
        browser.configure(
                browser_engine="chromium", screenshot="on", headless=False, isolated=True, slowmo=1
            )