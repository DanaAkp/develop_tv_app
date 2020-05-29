from command.abc_command import AbstractCommand
from api_tv.window_login import WindowLogin


class CommandLogin(AbstractCommand):
    def __init__(self):
        self.window = WindowLogin()

    def button_down(self):
        self.window.decrement()

    def button_up(self):
        self.window.increment()

    def button_ok(self):
        self.window.sign_in()

    def button_right(self):
        self.window.decrement()

    def button_left(self):
        self.window.increment()

    def button_zero(self):
        print('this login')
        # if self.window.is_login:
        #     self.window.input_login('0')
        # else:
        #     self.window.input_password('0')

    def button_one(self):
        if self.window.is_login:
            self.window.input_login('1')
        else:
            self.window.input_password('1')

    def button_two(self):
        if self.window.is_login:
            self.window.input_login('2')
        else:
            self.window.input_password('2')

    def button_three(self):
        if self.window.is_login:
            self.window.input_login('3')
        else:
            self.window.input_password('3')

    def button_four(self):
        if self.window.is_login:
            self.window.input_login('4')
        else:
            self.window.input_password('4')

    def button_five(self):
        if self.window.is_login:
            self.window.input_login('5')
        else:
            self.window.input_password('5')

    def button_six(self):
        if self.window.is_login:
            self.window.input_login('6')
        else:
            self.window.input_password('6')

    def button_seven(self):
        if self.window.is_login:
            self.window.input_login('7')
        else:
            self.window.input_password('7')

    def button_eight(self):
        if self.window.is_login:
            self.window.input_login('8')
        else:
            self.window.input_password('8')

    def button_nine(self):
        if self.window.is_login:
            self.window.input_login('9')
        else:
            self.window.input_password('9')
