from robocorp.tasks import task


class Login:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def handle_login(self):
        return self.login
    
    def handle_password(self):
        return self.password