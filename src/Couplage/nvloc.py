import os.path
import sys
from pathlib import Path

# exemple de commande pour lancer de programme
# python3 nvloc.py ./ckjm/src/gr/spinellis/ckjm/MethodVisitor.java
def file_is_a_file(file_path):
    folder = Path(os.path.abspath(file_path))

    if os.path.isfile(folder):
        nvloc(file_path)
    else:
        print("The path provided \"", file_path, "\" does not lead to a file")


def nvloc(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()
    total_line = 0

    for line in lines:
        if not line in ['\n', '\r\n']:
            total_line += 1

    print(total_line)
    file.close()

    return total_line


file_is_a_file(sys.argv[1])
