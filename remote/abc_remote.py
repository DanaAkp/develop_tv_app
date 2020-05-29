from command.abc_command import AbstractCommand
from command.command_login import CommandLogin
from command.command_channel import CommandChannel
from command.command_player import CommandPlayer
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class AbstractRemote(metaclass=ABCMeta):
    current_window: AbstractCommand
    slots: dict
    list_window = [CommandLogin(), CommandChannel(), CommandPlayer()]

    def click_button_back(self):
        self.current_window.button_back()

    def click_button_ok(self):
        self.current_window.button_ok()

    def click_button_up(self):
        self.current_window.button_up()

    def click_button_down(self):
        self.current_window.button_down()

    def click_button_left(self):
        self.current_window.button_left()

    def click_button_right(self):
        self.current_window.button_right()

    def click_button_zero(self):
        self.current_window.button_zero()

    def click_button_one(self):
        self.current_window.button_one()

    def click_button_two(self):
        self.current_window.button_two()

    def click_button_three(self):
        self.current_window.button_three()

    def click_button_four(self):
        self.current_window.button_four()

    def click_button_five(self):
        self.current_window.button_five()

    def click_button_six(self):
        self.current_window.button_six()

    def click_button_seven(self):
        self.current_window.button_seven()

    def click_button_eight(self):
        self.current_window.button_eight()

    def click_button_nine(self):
        self.current_window.button_nine()

    @abstractmethod
    def set_command(self):
        pass

