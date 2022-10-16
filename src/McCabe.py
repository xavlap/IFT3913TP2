from itertools import count
from operator import contains
import os
import sys

def mcCabeFile(file):
    f = open(os.path.join(os.getcwd(),file),"r")
    cpt=1

    while True:
        line = f.readline().strip()
        if not line:
            break
        if len(line) < 2:
            continue

        if line.startswith("//"):
            continue

        if line.startswith("/*"):
            line = f.readline().strip()
            while not line.endswith("*/"):
                line = f.readline().strip()
            line = f.readline() #not need to strip we dont read it
        else:
            cpt += line.count("if")
            cpt += line.count("for")
            cpt += line.count("while")
            cpt += line.count("case")
        
    
    return cpt

def mcCabeDir(path):
    cpt=0

    for root, dirs, files in os.walk(path):
        for file in files:
            if contains(file,".java"):
                print(file)
                cpt += mcCabeFile(os.path.join(root,file))
                

    return cpt
                

if len(sys.argv) > 0:
    print(mcCabeDir(sys.argv[1]))