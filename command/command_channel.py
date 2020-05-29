from command.abc_command import AbstractCommand
from api_tv.window_channel import WindowChannel


class CommandChannel(AbstractCommand):
    def __init__(self):
        self.window = WindowChannel()

    def button_back(self):
        self.window.get_back_button()

    def button_ok(self):
        self.window.get_window_player()

    def button_up(self):
        self.window.increment_focus()

    def button_down(self):
        self.window.decrement_focus()

    def button_left(self):
        self.window.increment_focus()

    def button_right(self):
        self.window.decrement_focus()

    def button_zero(self):
        print('this channel')
