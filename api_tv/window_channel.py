# from api_tv.window_login import WindowLogin
# from api_tv.window_player import WindowPlayer
from command.command_player import CommandPlayer
from command.command_login import CommandLogin

class WindowChannel:
    def __init__(self):
        self.list_channel = ['TV channel #1', 'TV channel #2', 'TV channel #3', 'TV channel #4', 'TV channel #5']
        self.focus = 0

    def get_window_player(self):
        return CommandPlayer(self.list_channel[self.focus])

    def get_back_button(self):

        return CommandLogin()

    def increment_focus(self):
        self.focus += 1
        self.focus %= len(self.list_channel)

    def decrement_focus(self):
        self.focus -= 1
        while self.focus < 0:
            self.focus += len(self.list_channel)
