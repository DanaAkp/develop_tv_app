from remote.abc_remote import AbstractRemote


class RemoteSony(AbstractRemote):
    def set_command(self):
        self.slots = {}
        self.slots.setdefault('0', self.current_window.button_zero)
        self.slots.setdefault('1', self.current_window.button_one)
        self.slots.setdefault('2', self.current_window.button_two)
        self.slots.setdefault('3', self.current_window.button_three)
        self.slots.setdefault('4', self.current_window.button_four)
        self.slots.setdefault('5', self.current_window.button_five)
        self.slots.setdefault('6', self.current_window.button_six)
        self.slots.setdefault('7', self.current_window.button_seven)
        self.slots.setdefault('8', self.current_window.button_eight)
        self.slots.setdefault('9', self.current_window.button_nine)
        self.slots.setdefault('10', self.current_window.button_up)
        self.slots.setdefault('11', self.current_window.button_down)
        self.slots.setdefault('12', self.current_window.button_left)
        self.slots.setdefault('13', self.current_window.button_right)
        self.slots.setdefault('14', self.current_window.button_ok)
        # self.slots.setdefault('', self.current_window.button_back)



