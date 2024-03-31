import unittest
from unittest.mock import patch, MagicMock
from utilities.pdf.definition import HTMLConversor


BROWSER_PATH = "utilities.abc.browser.browser"
PDF_PATH = "utilities.pdf.definition"


class TestHTMLConversor(unittest.TestCase):
    @patch(f"{BROWSER_PATH}.goto")
    def test_open_the_intranet_website(self, mock_goto):
        conv = HTMLConversor()
        conv.open_the_intranet_website()
        mock_goto.assert_called_once_with("https://robotsparebinindustries.com/")

    @patch(f"{BROWSER_PATH}.page")
    def test_log_in(self, mock_page):
        mock_fill = MagicMock()
        mock_page.return_value = mock_fill

        conv = HTMLConversor()
        conv.log_in()

        mock_fill.fill.assert_any_call("#username", "maria")
        mock_fill.fill.assert_any_call("#password", "thoushallnotpass")
        mock_fill.click.assert_called_once_with("button:text('Log in')")

    def test_fill_and_submit_sales_form(self):
        # This test case can be implemented similarly to test_log_in
        pass

    @patch(f"{PDF_PATH}.HTTP")
    def test_download_excel_file(self, mock_http):
        conv = HTMLConversor()

if __name__ == '__main__':
    unittest.main()