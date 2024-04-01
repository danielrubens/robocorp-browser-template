from robocorp.tasks import task

from utilities.login.login import call_login_task, call_password_task
from utilities.pdf.definition import HTMLConversor
from utilities.spreadsheet.definition import Spreadsheet

from __tests__.test_runner import run_test


@task
def fill_spreadsheet():
    spreadsheet = Spreadsheet()
    spreadsheet.fill_spreadsheet()
    
@task
def credentials_call():
    call_login_task()
    call_password_task()

@task
def pdf_conversor_call():
    conversor = HTMLConversor()
    conversor.to_pdf()