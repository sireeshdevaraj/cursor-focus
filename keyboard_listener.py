import keyboard
import subprocess

EXECUTABLE_LOCATION = "./dist/main/main.exe"

def run_exec(path):
    subprocess.run(path)

keyboard.add_hotkey('shift+f+space', run_exec, args=(EXECUTABLE_LOCATION,))

keyboard.wait()