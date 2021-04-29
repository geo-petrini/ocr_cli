import os

# dir = "scans/prova/"
# dirs = dir.split('/')
# a = dirs[0]
# b = dirs[1]
# print(dirs)
# print(os.path.join(a, b))
prefix = "scan.txt"
# print(os.path.splitext(prefix)[-1])

if not (os.path.splitext(prefix)[-1] == ".txt"):
    prefix = prefix + ".txt"
    print("cambiato: "+prefix)
else:
    print("va bene")