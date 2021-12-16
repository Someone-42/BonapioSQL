import CreateDatabase as db
import os

DATA_DIR = "./Data/"

def init():
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)

def main():
    pass

def test1():
    pass
    
if __name__ == "__main__":
    init()
    Test1()