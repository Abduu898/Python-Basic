import os

def list_dir(path, level=0):
    for entry in os.listdir(path): ## one elemnt of the path per time 
        full = os.path.join(path, entry) ## build the full path 
        if os.path.isdir(full): ## is it a folder?  
            print("  " * level + entry + "/") ##How many spaces
            list_dir(full, level + 1)     
        else:
            print("  " * level + entry) ## When the entry is file not a folder

list_dir(".")
