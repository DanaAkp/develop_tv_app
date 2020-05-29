from remote.remote_samsung import RemoteSamsung
from command.command_channel import CommandChannel
from command.command_login import CommandLogin


x = RemoteSamsung(CommandLogin(), {})
x.set_command()
y = x.slots['23']()

x.current_window = CommandChannel()
x.set_command()
z = x.slots['23']()
