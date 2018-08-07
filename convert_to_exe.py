from cx_Freeze import setup, Executable
#  python convert_to_exe.py 

base = None

prog = input("Program: ")

executables = [Executable(prog, base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)
