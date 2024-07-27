# Fake Terminal
This is a python app used to bypass terminal blocks, but also to have a cool layout with having custom commands and addons
# Install
Clone the GitHub repository
```shell
git clone https://github.com/TheDiamondOG/FakeTerminal
```

Run a python app
```shell
python3 main.py
```

# Run with bypass
On windows with the terminal blocked do these steps
1. Copy folder to `C:\Users\%USER%\Documents\`
2. Click `Win+R`
3. Then type `cmd.exe python3 C:\Users\%USER%\Documents\FakeTerminal\main.py`
# Making Addons

To add a custom command you can use this as an example
```python
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
```

Let's break down the example

First with the addon info
```python
addon_info = {  
    "name": "Example Addon",  
    "description": "An example addon", 
    "version": "1.0.0",
    "custom_libs": False  
}
```
This is required for the addon to work
Replace the "Example Addon" with you addon name
Replace the "An example addon" with your addon description
Replace the "1.0.0" with your addon version
Keep the `custom_libs` the same

Now let's do the command function
```python
def example_command(args):  
    print("Example command cool:", args)  
```
All command functions need args for the arguments, if you script does not need it use args=None

Lastly lets talk about register
```python
def register(command_system):  
    command_system.add_command("example", "example command", "custom", example_command, False)
```

This function is required for you to add a command
The "example" part is the command
The "example command" part is the description of the command
The "custom" part is the category name
The "False" is if the command requires

If you need any custom libraries that don't come with the script use this
```python
addon_info = {  
    "name": "Example Addon",  
    "description": "An example addon with custom libs",  
    "version": "1.0.0",
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
```
The only differences are the `requirements` list, `custom_libs` being `True` and a command having `True` instead of False mean the command requires one of the custom commands

Remember to put all custom libraries imported under a try statement
```python
try:  
    # Any custom lib you want here  
    import requests  
except Exception:  
    print("Your error message")
```

# Installing Addons
1. Download Addon
2. Move into addons folder
3. Run the program
4. Run the command `list_addons` and check to see if the addon install correctly

# Ideas
Linux Mode
- When on windows it will translate linux commands to windows commands
- This will involve argument and command changing
Info Getting
- Get Mac Address
- Get Environment Variables