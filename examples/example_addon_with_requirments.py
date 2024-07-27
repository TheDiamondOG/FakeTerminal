addon_info = {
    "name": "Example Addon",
    "description": "An example addon with custom libs",
    "custom_libs": True
}

requirements = [
    "requests",
    "rich"
]

def example_command(args):
    print("Example command cool:", args)

def register(command_system):
    command_system.add_command("example", "example command", "custom", example_command, True)
