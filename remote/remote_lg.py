from remote.abc_remote import AbstractRemote


class RemoteLG(AbstractRemote):
    def set_command(self):
        self.slots = {}
        self.slots.setdefault('65', self.current_window.button_zero)
        self.slots.setdefault('66', self.current_window.button_one)
        self.slots.setdefault('67', self.current_window.button_two)
        self.slots.setdefault('68', self.current_window.button_three)
        self.slots.setdefault('69', self.current_window.button_four)
        self.slots.setdefault('70', self.current_window.button_five)
        self.slots.setdefault('71', self.current_window.button_six)
        self.slots.setdefault('72', self.current_window.button_seven)
        self.slots.setdefault('73', self.current_window.button_eight)
        self.slots.setdefault('74', self.current_window.button_nine)
        self.slots.setdefault('1', self.current_window.button_up)
        self.slots.setdefault('2', self.current_window.button_down)
        self.slots.setdefault('3', self.current_window.button_left)
        self.slots.setdefault('4', self.current_window.button_right)
        self.slots.setdefault('55', self.current_window.button_ok)
        self.slots.setdefault('77', self.current_window.button_back)



