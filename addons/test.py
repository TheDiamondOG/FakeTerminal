addon_info = {
    "name": "Example Addon",
    "description": "An example addon with custom libs",
    "custom_libs": True
}

def test_command(args):
    print("Test command cool:", args)

def register(command_system):
    command_system.add_command("test", "test command", "test", test_command, False)
