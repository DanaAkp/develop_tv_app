from command.abc_command import AbstractCommand
from api_tv.window_player import WindowPlayer


class CommandPlayer(AbstractCommand):
    def __init__(self, name_channel: str = ''):
        self.is_click_back = False
        self.window = WindowPlayer(name_channel)

    def button_back(self):
        self.is_click_back = True

    def button_ok(self):
        self.window.get_back_button()
