import os

def add(file):
    with open('myrepo/index', 'a') as index:
        index.write(file + '\n')
    print(f"Added {file} to index")

if __name__ == "__main__":
    import sys
    add(sys.argv[1])
