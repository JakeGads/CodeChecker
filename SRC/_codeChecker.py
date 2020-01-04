from platform import system

from os import system as call
import os


import subprocess
import shlex

"""
PYTHON: Requires a single command, no need to parse any output
C++: Requires one maybe two commands, if 2 commands are required the output must be parsed
java: requires both commands listed below
"""
commands = {
    "nix": {
        "python": ["python3", "py3"],
        "c++": ["gcc"],
        "java": ["javac", "java"],
    },

    "nt": {
        "python": ["python", "python3", "py", "py3"],
        "c++": ["gcc", "cl"],  # cl needs to be tied to an executed call as well
        "java": ["javac", "java"],
    },
}

if system() == "Windows":
    operating_system = "nt"
    deliminiter = "\\"
else:
    operating_system = "nix"
    deliminiter = "/"

print("OS:", operating_system, "\n\nFinding neccessary commands ... things may flash on the screen be calm")

files = [f for f in os.listdir('.') if os.path.isfile(f)]

mode = ''
file = 0

for f in files:
    if '_master' in f:
        if '.py' in f:
            mode = 'python'
        elif '.cpp' in f or '.c' in f:
            mode = 'c++'
        elif '.java' in f:
            mode = 'java'
        file = f
        break

if mode == '':
    exit("We seem to have encounterd an ouchy trying to find the language")

command_index = -1

if mode != 'java':
    for command in commands[operating_system][mode]:
        try:
            process = subprocess.Popen([command, file], stdout=subprocess.PIPE)
            stdout = process.communicate()[0]
            command_index = commands[operating_system][mode].index(command)
            break
        except :
            continue
else:
    command_index = 'javac'

if command_index is -1:
    exit("couln't find the command")

if mode == 'python':


# process = subprocess.Popen(['python', 'Examples' + deliminiter + '_Hello_World.py'], stdout=subprocess.PIPE) # this lets me test the test the output
# stdout = process.communicate()[0]

# print('STDOUT:{}'.format(stdout))