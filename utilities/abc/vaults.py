from robocorp import vault

class Vault:
    def __init__(self):
        self.secrets = vault.get_secret("DemoVault")
        self.url = self.secrets["url"]