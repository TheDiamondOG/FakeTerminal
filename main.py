import os
import socket
import sys
import subprocess
import urllib.request
import signal
import importlib.util
import readline

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

limited_mode = True

try:
    import requests

    limited_mode = False
except Exception:
    print("Could not get all custom libraries to run, please run the command 'install_requirements' to get the full thing with all custom commands")
    limited_mode = True

required_libraries = [
    "requests",
    "rich",
    "flask",
    "pyfiglet"
]

addons = []

class CoolSystemCrap:
    def get_user_name(self):
        return os.getenv('USER') or os.getlogin()

    def get_hostname(self):
        return socket.gethostname()

    def path_changer(self, path: str):
        if path == ".." or path == ",,":
            if "/" in os.getcwd():
                path_split = os.getcwd().split("/")
                path_splitter = "/"
            else:
                path_split = os.getcwd().split("\\")
                path_splitter = "\\"

            path_split.pop(-1)

            os.chdir(f'{path_splitter}'.join(path_split))
        else:
            if os.path.exists(path):
                os.chdir(path)
            else:
                print(cool_colors.colorize("Not a real path", "cyan"))

    def get_path(self):
        return os.getcwd()


class CommandSystem:
    def __init__(self):
        self.custom_command_list = {}
        self.history = []

    def add_command(self, command: str, description: str, category: str, method, custom_libs: bool):
        if category not in self.custom_command_list:
            self.custom_command_list[category] = []
        command_template = {
            "command": command,
            "description": description,
            "custom_libs": custom_libs,
            "function": method
        }
        self.custom_command_list[category].append(command_template)

    def remove_command(self, command: str):
        for category in self.custom_command_list.values():
            for commannd in category:
                if commannd["command"] == command:
                    category.remove(commannd)
                    return

    def check_command(self, command: str):
        for category in self.custom_command_list.values():
            for commannd in category:
                if commannd["command"] == command:
                    return True
        return False

    def command_list(self):
        return self.custom_command_list

    def requires_custom_libs(self, command: str):
        for category in self.custom_command_list.values():
            for commannd in category:
                if commannd["command"] == command:
                    return commannd["custom_libs"]
        return None

    def process_command(self, command):
        if isinstance(command, str):
            command_split = command.split(" ")
        elif isinstance(command, list):
            command_split = command
        else:
            return False

        # Add command to history
        if command not in self.history:
            self.history.append(command)

        for category in self.custom_command_list.values():
            for commannd in category:
                if command_split[0] == commannd["command"]:
                    args = command_split[1:]
                    if commannd["function"] == exit:
                        exit()
                    if commannd["custom_libs"]:
                        if not limited_mode:
                            commannd["function"](args)
                            return
                    else:
                        commannd["function"](args)
                        return
        else:
            if isinstance(command, list):
                command = ' '.join(command)
            os.system(command)


def restart(args: list = None):
    print("Restarting script...")
    os.execl(sys.executable, sys.executable, *sys.argv)


class ColorText:
    COLORS = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[39m'
    }

    BACKGROUNDS = {
        'black': '\033[40m',
        'red': '\033[41m',
        'green': '\033[42m',
        'yellow': '\033[43m',
        'blue': '\033[44m',
        'magenta': '\033[45m',
        'cyan': '\033[46m',
        'white': '\033[47m',
        'reset': '\033[49m'
    }

    STYLES = {
        'bold': '\033[1m',
        'underline': '\033[4m',
        'reversed': '\033[7m',
        'reset': '\033[0m'
    }

    def colorize(self, text: str, color=None, background=None, style=None):
        colored_text = text

        if style and style in self.STYLES:
            colored_text = self.STYLES[style] + colored_text

        if color and color in self.COLORS:
            colored_text = self.COLORS[color] + colored_text

        if background and background in self.BACKGROUNDS:
            colored_text = self.BACKGROUNDS[background] + colored_text

        return colored_text + self.STYLES['reset']


class CommandFunctions:
    def install_requirements(self, args: list = None):
        for requirement in required_libraries:
            print(cool_colors.colorize(f"Installing {requirement}", "cyan"))
            subprocess.run(["pip", "install", requirement, "--break-system-packages"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        restart()

    def change_directory(self, args: list = None):
        cool_system_crap.path_changer(args[0])

    def get_current_ip_address(self, args: list = None):
        with urllib.request.urlopen("https://api.ipify.io") as response:
            data = response.read()
            print(cool_colors.colorize(data.decode('utf-8'), color="cyan"))

    def get_device_ip_address(self, args: list = None):
        print(cool_colors.colorize(socket.gethostbyname(socket.gethostname()), color="cyan"))

    def help(self, args: list = None):
        print(cool_colors.colorize("====== Help Command ======", color="blue"))
        for category in custom_command.command_list():
            category_split = category.split("_")
            count = 0
            for word in category_split:
                category_split[count] = word.capitalize()
                count += 1

            category_name = ' '.join(category_split)
            print(cool_colors.colorize(f"{category_name}:", color="cyan"))
            for command in custom_command.command_list()[category]:
                print()
                print(cool_colors.colorize(f"{command['command']}", color="cyan"))
                print(cool_colors.colorize(f" - {command['description']}", color="cyan"))
                print(cool_colors.colorize(f" - Requires Custom Libraries: <{command['custom_libs']}>", color="cyan"))
            print(cool_colors.colorize(f"-------------------------", color="blue"))

    def list_addons(self, args: list = None):
        count = 0
        print(cool_colors.colorize("====== List Addons ======", color="blue"))
        for addon in addons:
            print()
            count += 1

            print(cool_colors.colorize(f"{addon['name']}:", color="cyan"))
            print(cool_colors.colorize(f" - {addon['description']}", color="cyan"))
            print(cool_colors.colorize(f" - Requires Custom Libraries: <{addon['custom_libs']}>", color="cyan"))
            print(cool_colors.colorize(f"-------------------------", color="blue"))
        print(cool_colors.colorize(f"Addon Count: {count}", color="cyan"))


cool_colors = ColorText()
custom_command = CommandSystem()
cool_system_crap = CoolSystemCrap()
command_functions = CommandFunctions()

# Don't exit with keybindings because they are not cool
def ignore_crap(signum, frame):
    return

# All the custom commands I added for the script
custom_command.add_command("install_requirements", "Install all the requirements needed for some commands in this script", "important", command_functions.install_requirements, False)
custom_command.add_command("help", "Get all of the commands built into the script", "important", command_functions.help, False)
custom_command.add_command("list_addons", "List every addon you have", "addon_settings", command_functions.list_addons, False)
custom_command.add_command("restart", "Restart the script", "system", restart, False)
custom_command.add_command("exit", "Exits the terminal", "system", exit, False)
custom_command.add_command("cd", "Changing directory with the python script", "system", command_functions.change_directory, False)
custom_command.add_command("getip", "Get your current public ip", "network", command_functions.get_current_ip_address, False)
custom_command.add_command("getdeviceip", "Get your current device ip", "network", command_functions.get_device_ip_address, False)

# Adding all the addons into the script
def load_addons(addons_folder="addons"):
    # Check if the folder does not exist
    if not os.path.exists(addons_folder):
        # If it doesn't create it
        os.makedirs(addons_folder)
    # Get all the files in the folder
    for filename in os.listdir(addons_folder):
        # Check if the current file is a python file
        if filename.endswith(".py"):
            # Put the full path together
            addon_path = os.path.join(addons_folder, filename)

            # Import the addon
            spec = importlib.util.spec_from_file_location("addon_module", addon_path)
            addon_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(addon_module)

            # Import all the requirements
            if hasattr(addon_module, 'requirements'):
                for requirement in addon_module.requirements:
                    # Add the requirements to the list
                    required_libraries.append(requirement)
            # Get all the addon info
            if hasattr(addon_module, "addon_info"):
                addons.append(addon_module.addon_info)
            else:
                cool_colors.colorize(f"Addon {filename} does not have a any of the info added", "red")
            # Register all the actual custom commands
            if hasattr(addon_module, 'register'):
                addon_module.register(custom_command)
            else:
                # Say if the addon creator committed a stupid
                print(cool_colors.colorize(f"Addon {filename} does not have a register function", "red"))

# Make ctrl+c and ctrl+z not exit
signal.signal(signal.SIGINT, ignore_crap)
signal.signal(signal.SIGTSTP, ignore_crap)

# Load all the custom addons
load_addons()

# Print a custom welcome message
print(cool_colors.colorize("Welcome to Dia Terminal, this project is meant to be used to get around terminal restrictions while having extra cool commands", "cyan"))

# Run a loop
while True:
    # Get the command input with history feature
    command = input(f"{cool_system_crap.get_user_name()}@{cool_system_crap.get_hostname()} <({cool_system_crap.get_path()})> ")
    # Check if the command is a command
    if command.replace(" ", "") != "":
        custom_command.process_command(command)
