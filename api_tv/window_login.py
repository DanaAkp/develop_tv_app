# from api_tv.window_channel import WindowChannel
from command.command_channel import CommandChannel

class WindowLogin:
    def __init__(self):
        self.login = None
        self.password = None
        self.is_login = True

    def sign_in(self):
        if self.check_data():
            return CommandChannel()

    def check_data(self):
        if self.login is not None and self.password is not None:
            return True
        return False

    def increment(self):
        self.is_login = not self.is_login

    def decrement(self):
        self.is_login = not self.is_login

    def input_login(self, number):
        if self.login is not None:
            self.login += number
        else:
            self.login = number

    def input_password(self, number):
        if self.password is not None:
            self.password += number
        else:
            self.password = number
