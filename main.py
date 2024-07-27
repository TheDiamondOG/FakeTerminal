# Cool random imports
import os
import subprocess
import socket
import sys
import urllib.request
import signal
import importlib.util
import readline

# Clears the console window
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

limited_mode = True

# Try to import libraries that don't come with python
try:
    import requests

    limited_mode = False
except Exception:
    # If it fails tale the user to install them
    print("Could not get all custom libraries to run, please run the command 'install_requirements' to get the full thing with all custom commands")
    limited_mode = True

# The list of required libraries that I am not using
required_libraries = [
    "requests",
    "rich",
    "flask",
    "pyfiglet"
]

# Cool addons list
addons = []

def check_version():
    # Look for the version.txt file
    if os.path.exists("version.txt"):
        # Open the file to read
        with open("version.txt", "r") as f:
            # Get the program version from the file
            program_version = f.read()
    else:
        # Error if it does not exist
        print("Can't find the version.txt file, either run your terminal in the program folder, move the version.txt to your current folder, or update the program at https://github.com/TheDiamondOG/FakeTerminal")

    # Try statement to catch web errors
    try:
        # Get the current version of the program
        with urllib.request.urlopen("https://raw.githubusercontent.com/TheDiamondOG/FakeTerminal/master/version.txt") as response:
            last_update = response.read()
    except Exception:
        # The request fails because I was stupid and deleted the repo, no internet, or Github is just blocked, like it is in some school counties. All because they blame Github for blooket, gimkit, and kahoot hacks. Jokes on them I know how to use replit and how to set it up as a proxy. HOW DO YOU LIKE THAT. Also, the spy ware on the school chromebooks suck, they were bypassed by using the data:html feature. The same one used by the other spyware, that also blocked ipify.io, ipinfo.io, and buckshot rulet. Even though this happened 4 or more months ago I am still mad about this. So next project coming up, school blocker bypass using data:html because the software they use is too stupid enough to look through it.
        print("Failed to get current version, either https://raw.githubusercontent.com is blocked, or you have no internet")

    if program_version == "69":
        print("Very funny, everyone is laughing")

    # Checks to see if the version numbers are the same
    if program_version != last_update:
        print("You are running an outdated version of the program, please update it at https://github.com/TheDiamondOG/FakeTerminal")

class CoolSystemCrap:
    def get_user_name(self):
        # Honestly no clue if USER is in windows or if it's just a linux thing, so why not use both
        return os.getenv('USER') or os.getlogin()

    def get_hostname(self):
        # Used a file that only exists in linux, then I remembered that is meant to work on windows too
        return socket.gethostname()

    def path_changer(self, path: str):
        # This is for the cd .. feacher but with the ability to use ,,
        if path == ".." or path == ",,":
            # Check if it's a path done the right wat
            if "/" in os.getcwd():
                path_split = os.getcwd().split("/")
                path_splitter = "/"
            # Or the stupid way windows does it that needs every program to use 2 backslashes
            else:
                path_split = os.getcwd().split("\\")
                path_splitter = "\\"

            # Remove the last folder
            path_split.pop(-1)

            # Then change directory
            os.chdir(f'{path_splitter}'.join(path_split))
        else:
            # Change the directory if the path exists
            if os.path.exists(path):
                os.chdir(path)
            else:
                # Tells the user the path does not exist
                print(cool_colors.colorize("Not a real path", "cyan"))

    def get_path(self):
        # The original used a variable, then I remembered this is meant to also work on windows
        return os.getcwd()


class CommandSystem:
    def __init__(self):
        # Cool lists and dicts
        self.custom_command_list = {}
        self.history = []

    def add_command(self, command: str, description: str, category: str, method, custom_libs: bool):
        # If the category does not exist, if not add it
        if category not in self.custom_command_list:
            self.custom_command_list[category] = []
        # The template for every command info crap
        command_template = {
            "command": command,
            "description": description,
            "custom_libs": custom_libs,
            "function": method
        }
        # Then add the command info to the command list
        self.custom_command_list[category].append(command_template)

    def remove_command(self, command: str):
        # Get every category
        for category in self.custom_command_list.values():
            # Get all commands
            for commannd in category:
                # Check if the command is the command
                if commannd["command"] == command:
                    # Then remove it
                    category.remove(commannd)
                    return

    def check_command(self, command: str):
        # Get every category again
        for category in self.custom_command_list.values():
            # Get every command again
            for commannd in category:
                # Then run the check I will never use
                if commannd["command"] == command:
                    return True
        return False

    def command_list(self):
        # Grabs the command list, this is not needing a comment, but I put it here
        return self.custom_command_list

    def requires_custom_libs(self, command: str):
        # Get all the categories
        for category in self.custom_command_list.values():
            # Get all the commands
            for commannd in category:
                # Check if the command is the command being looked for
                if commannd["command"] == command:
                    # Return the custom lib status for it
                    return commannd["custom_libs"]
        # If it does not exist then the function shuts up
        return None

    def process_command(self, command):
        # Check if the command is a string
        if isinstance(command, str):
            # Then split the string
            command_split = command.split(" ")
        elif isinstance(command, list):
            # If not just call it command_split
            command_split = command
        else:
            # If it's anything else break the whole command system
            return False

        # Add command to history
        if command and command not in self.history:
            # Add the command to the command history that is not saved
            self.history.append(command)
            readline.add_history(command)  # Add command to readline history

        # Check every category for the command
        for category in self.custom_command_list.values():
            for commannd in category:
                # If it finds it then run the command
                if command_split[0] == commannd["command"]:
                    args = command_split[1:]
                    # Check if it exits the script
                    if commannd["function"] == exit:
                        exit()
                    # Checks for the script not to break when custom libraries are not installed
                    if commannd["custom_libs"]:
                        if not limited_mode:
                            commannd["function"](args)
                            return
                    else:
                        commannd["function"](args)
                        return
        else:
            # Combine the list into a string
            if isinstance(command, list):
                command = ' '.join(command)
            # Then run the command through the system
            os.system(command)


def restart(args: list = None):
    # Restarts the script
    print("Restarting script...")
    os.execl(sys.executable, sys.executable, *sys.argv)

# Simple color system that I won't explain
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
        if style and style in self.STYLES:
            text = self.STYLES[style] + text

        if color and color in self.COLORS:
            text = self.COLORS[color] + text

        if background and background in self.BACKGROUNDS:
            text = self.BACKGROUNDS[background] + text

        return text + self.STYLES['reset']


class CommandFunctions:
    def install_requirements(self, args: list = None):
        # Installs all requirements from the list
        for requirement in required_libraries:
            print(cool_colors.colorize(f"Installing {requirement}", "cyan"))
            subprocess.run(["pip", "install", requirement, "--break-system-packages"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        restart()

    def change_directory(self, args: list = None):
        # Change the directory with the big changer
        cool_system_crap.path_changer(args[0])

    def get_current_ip_address(self, args: list = None):
        # Uses ipify to get your ip address then prints it
        with urllib.request.urlopen("https://api.ipify.io") as response:
            data = response.read()
            print(cool_colors.colorize(data.decode('utf-8'), color="cyan"))

    def get_device_ip_address(self, args: list = None):
        # Prints your device ip
        print(cool_colors.colorize(socket.gethostbyname(socket.gethostname()), color="cyan"))

    # Lists all the commands
    def help(self, args: list = None):
        print(cool_colors.colorize("====== Help Command ======", color="blue"))
        # Get all the categories
        for category in custom_command.command_list():
            # Split the category name by the _
            category_split = category.split("_")
            # Make a count
            count = 0
            # Get every word in the category name
            for word in category_split:
                # Capitalize the first letter of each word
                category_split[count] = word.capitalize()
                count += 1

            # Join the list together as a string
            category_name = ' '.join(category_split)

            # Print the category name
            print(cool_colors.colorize(f"{category_name}:", color="cyan"))
            # Get every command in the category
            for command in custom_command.command_list()[category]:
                # Print the command and command info
                print()
                print(cool_colors.colorize(f"{command['command']}", color="cyan"))
                print(cool_colors.colorize(f" - {command['description']}", color="cyan"))
                print(cool_colors.colorize(f" - Requires Custom Libraries: <{command['custom_libs']}>", color="cyan"))
            print(cool_colors.colorize(f"-------------------------", color="blue"))

    # Lists all the addons you have
    def list_addons(self, args: list = None):
        # Count to see how many addons you have
        count = 0

        print(cool_colors.colorize("====== List Addons ======", color="blue"))
        # Get every addon with info
        for addon in addons:
            print()
            # Add one to the addon count
            count += 1

            # Print out the addon info
            print(cool_colors.colorize(f"{addon['name']}:", color="cyan"))
            print(cool_colors.colorize(f" - {addon['description']}", color="cyan"))
            print(cool_colors.colorize(f" - Version: {addon['version']}", color="cyan"))
            print(cool_colors.colorize(f" - Requires Custom Libraries: <{addon['custom_libs']}>", color="cyan"))
            print(cool_colors.colorize(f"-------------------------", color="blue"))
        # Print addon count
        print(cool_colors.colorize(f"Addon Count: {count}", color="cyan"))

# All the custom classes
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

check_version()

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
