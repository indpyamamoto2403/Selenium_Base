import sys, os

current_dir  = os.path.dirname(os.path.abspath(__file__))

def add_all_folders(path):
    for folder in os.walk(path):
        sys.path.append(folder)

add_all_folders(current_dir)

