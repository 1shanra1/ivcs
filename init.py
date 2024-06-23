import os
import sys

directory = ".ivcs"
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory)

if not os.path.exists(path): 
    os.mkdir(path)
else:
    print("Repository already initialized")
    sys.exit(1)

# create HEAD
with open(os.path.join(path, "HEAD"), 'a') as f:
    f.write("ref: refs/heads/main")
