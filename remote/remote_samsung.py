from remote.abc_remote import AbstractRemote


class RemoteSamsung(AbstractRemote):
    def set_command(self):
        self.slots = {}
        self.slots.setdefault('23', self.current_window.button_zero)
        self.slots.setdefault('24', self.current_window.button_one)
        self.slots.setdefault('25', self.current_window.button_two)
        self.slots.setdefault('26', self.current_window.button_three)
        self.slots.setdefault('27', self.current_window.button_four)
        self.slots.setdefault('28', self.current_window.button_five)
        self.slots.setdefault('29', self.current_window.button_six)
        self.slots.setdefault('30', self.current_window.button_seven)
        self.slots.setdefault('31', self.current_window.button_eight)
        self.slots.setdefault('32', self.current_window.button_nine)
        self.slots.setdefault('56', self.current_window.button_up)
        self.slots.setdefault('58', self.current_window.button_down)
        self.slots.setdefault('57', self.current_window.button_left)
        self.slots.setdefault('55', self.current_window.button_right)
        self.slots.setdefault('123', self.current_window.button_ok)
        self.slots.setdefault('321', self.current_window.button_back)
        self.slots.setdefault('45', self.current_window.button_back)



