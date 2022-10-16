from operator import contains
import os
import sys

def countCLOC(file):
    f = open(os.path.join(os.getcwd(),file), "r")
    
    cpt=0
    line = f.readline().strip()
    while True:
        if len(line) >= 2:
            if line[0] == "/" and line[1] == "/":
                cpt+=1
            elif line[0] == "/" and line[1] == "*":
                cpt+=1
                line = f.readline().strip()
                while line[len(line)-2] != "*" and line[len(line)-1] != "/":
                    cpt+=1
                    line = f.readline().strip()
                    if not line:
                        break
                    if len(line) < 2:
                        continue
                cpt+=1
        line = f.readline().strip()
        if not line:                                                                                                                                                                                                                                                
            break
    f.close()
    return cpt                                                                                                                                                                                          

def counLOC(file):
    f = open(os.path.join(os.getcwd(),file), "r")
    
    lines = f.readlines()

    f.close()
    return len(lines)

def DC(path):

    CLOC = 0
    LOC = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if contains(file,".java"):
                print(os.path.join(file))
                CLOC += countCLOC(os.path.join(root,file))
                LOC += counLOC(os.path.join(root,file))
    
    return CLOC/LOC
    
if len(sys.argv) > 0:
    print(DC(sys.argv[1]))