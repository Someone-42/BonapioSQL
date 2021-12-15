import CreateDatabase as db
import os

DATA_DIR = "./Data/"

def Init():
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)

def main():
    pass

def Test1():
    pass
    

if __name__ == "__main__":
    Init()
    Test1()