from robocorp.tasks import task
from robocorp import browser

from RPA.HTTP import HTTP
from RPA.Excel.Files import Files
from RPA.PDF import PDF

class HTMLConversor:
    def __init__(self):
        pass
    
    def to_pdf(self):
        self.robot_spare_bin_python()

    def robot_spare_bin_python(self):
        """Insert the sales data for the week and export it as a PDF"""
        browser.configure(
            slowmo=100,
        )
        self.open_the_intranet_website()
        self.log_in()
        self.download_excel_file()
        self.fill_form_with_excel_data()
        self.collect_results()
        self.export_as_pdf()
        self.log_out()

    def open_the_intranet_website(self):
        """Navigates to the given URL"""
        browser.goto("https://robotsparebinindustries.com/")

    def log_in(self):
        """Fills in the login form and clicks the 'Log in' button"""
        page = browser.page()
        page.fill("#username", "maria")
        page.fill("#password", "thoushallnotpass")
        page.click("button:text('Log in')")

    def fill_and_submit_sales_form(self, sales_rep):
        """Fills in the sales data and click the 'Submit' button"""
        page = browser.page()

        page.fill("#firstname", sales_rep["First Name"])
        page.fill("#lastname", sales_rep["Last Name"])
        page.select_option("#salestarget", str(sales_rep["Sales Target"]))
        page.fill("#salesresult", str(sales_rep["Sales"]))
        page.click("text=Submit")

    def download_excel_file(self):
        """Downloads excel file from the given URL"""
        http = HTTP()
        http.download(url="https://robotsparebinindustries.com/SalesData.xlsx", overwrite=True)

    def fill_form_with_excel_data(self):
        """Read data from excel and fill in the sales form"""
        excel = Files()
        excel.open_workbook("SalesData.xlsx")
        worksheet = excel.read_worksheet_as_table("data", header=True)
        excel.close_workbook()

        for row in worksheet:
            self.fill_and_submit_sales_form(row)

    def collect_results(self):
        """Take a screenshot of the page"""
        page = browser.page()
        page.screenshot(path="output/sales_summary.png")

    def export_as_pdf(self):
        """Export the data to a pdf file"""
        page = browser.page()
        sales_results_html = page.locator("#sales-results").inner_html()

        pdf = PDF()
        pdf.html_to_pdf(sales_results_html, "output/sales_results.pdf")

    def log_out(self):
        """Presses the 'Log out' button"""
        page = browser.page()
        page.click("text=Log out")