from platform import system
import os
import csv
import subprocess
import shlex

"""
PYTHON: Requires a single command, no need to parse any output
C++: Requires one maybe two commands, if 2 commands are required the output must be parsed
JAVA: requires both commands listed below
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
    delimiter = "\\"

else:
    operating_system = "nix"
    delimiter = "/"

print("OS:", operating_system, "\n\nFinding neccessary commands ... things may flash on the screen be calm")

files = [f for f in os.listdir('.') if os.path.isfile(f)]

mode = ''
master = 0

for f in files:
    if '_master' in f:
        if '.class' in f:
            continue

        print('found', f)

        if '.py' in f:
            mode = 'python'

        elif '.cpp' in f:
            mode = 'c++'

        elif '.java' in f:
            mode = 'java'

        master = f
        break

if mode == '':
    exit("We seem to have encountered an error trying to find the language")

command_index = -1

if mode == 'python':
    for command in commands[operating_system][mode]:
        try:
            process = subprocess.Popen([command, master], stdout=subprocess.PIPE)
            master_output = process.communicate()[0]
            command_index = commands[operating_system][mode].index(command)
            break
        except:
            continue
elif mode == 'java':
    os.system(f'javac {master}')
    process = subprocess.Popen(['java', master.replace('.java', '')], stdout=subprocess.PIPE)
    master_output = process.communicate()[0]
    command_index = 0
elif mode == 'c++':
    # need to impliment cl command
    try:
        os.system(f'g++ {master} -o {master.replace(".cpp", "")} ')
        process = subprocess.Popen([f'{os.getcwd()}{master.replace(".cpp", "")}'], stdout=subprocess.PIPE)
        sub_output = process.communicate()[0]
    except:
        None

if command_index == -1:
    exit("failed find the command")

print(files)

with open("comparison.csv", "w+") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['File', 'Master Input', 'Sub Output', 'Matching'])

    if mode == 'python':
        for f in files:
            if f == master or f == __name__ or f == "_codeChecker.py" or '.py' not in f:
                continue
            try:
                process = subprocess.Popen([command, f], stdout=subprocess.PIPE)
                sub_output = process.communicate()[0]

                print(
                    f"\n{f}\n\tMaster:\t{master_output}\n\tSub:\t{sub_output}\n\tPass:\t{master_output == sub_output}")
                writer.writerow([f, master_output, sub_output, master_output == sub_output])
            except:
                print(f"{f} forced an error")

            process = None

        for f in files:
            if '.pyc' in f:
                os.system(f'rm {f}')

    if mode == 'c++':
        if command_index == 0 or command_index == 'gcc':  # gcc logic
            for f in files:
                if f == master or '.cpp' not in f:
                    continue
                c = f'g++ {f} -o x ' \
                    f'&& {os.getcwd()}"x'

                try:
                    os.system(f'g++ {f} -o {f.replace(".cpp", "")} ')
                    process = subprocess.Popen([f'{os.getcwd()}{f.replace(".cpp", "")}'], stdout=subprocess.PIPE)
                    sub_output = process.communicate()[0]
                    print(
                        f"\n{f}\n\tMaster:\t{master_output}\n\tSub:\t{sub_output}\n\tPass:\t{master_output == sub_output}")
                    writer.writerow([f, master_output, sub_output, master_output == sub_output])

                except:
                    print(f'{f} forced an error')

    if mode == 'java':
        for f in files:
            if f == master or '.java' not in f:
                continue

            c = f"java {f.replace('.java', '')}"

            try:
                os.system(f'javac {f}')
                f = f.replace('.java', '')
                process = subprocess.Popen(['java', f], stdout=subprocess.PIPE)
                sub_output = process.communicate()[0]
                print(
                    f"\n{f}\n\tMaster:\t{master_output}\n\tSub:\t{sub_output}\n\tPass:\t{master_output == sub_output}")
                writer.writerow([f, master_output, sub_output, master_output == sub_output])

            except:
                print(f'{f} forced an error')

        for f in files:
            if '.class' in f:
                os.system(f'rm {f}')
