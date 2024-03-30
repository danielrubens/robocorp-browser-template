from .definition import Login
from robocorp.tasks import task

login = Login("login", "password")

@task
def call_login_task():
    print(login.handle_login())

@task
def call_password_task():
    print(login.handle_password())