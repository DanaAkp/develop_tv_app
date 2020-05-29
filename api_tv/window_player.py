from command.command_channel import CommandChannel


class WindowPlayer:
    def __init__(self, name_channel: str):
        self.name_channel = name_channel

    def get_back_button(self):
        return CommandChannel()

    def get_player(self):
        return self.name_channel
