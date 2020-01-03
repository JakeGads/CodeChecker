from platform import system

commands = {
    "nix": {
        "python": ["python3", "py3"],
        "c++": ["gcc"],
    },

    "nt": {
        "python": ["python", "python3", "py", "py3"],
        "c++": ["gcc", "cl"]  # cl needs to be tied to an executed call as well
    },
}

if system() == "Windows":
    operating_system = "nt"
else:
    operating_system = "nix"


