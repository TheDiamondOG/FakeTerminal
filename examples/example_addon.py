addon_info = {
    "name": "Example Addon",
    "description": "An example addon",
    "version": "1.0.0",
    "custom_libs": False
}

def example_command(args):
    print("Example command cool:", args)

def register(command_system):
    command_system.add_command("example", "example command", "custom", example_command, False)
