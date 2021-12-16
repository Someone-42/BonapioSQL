import DBUtils as db
import os

DATA_DIR = "./Data/"
SQL_ORDERS_DIR = "./SQLOrders"
USER_DB_NAME = DATA_DIR + "Utilisateurs.db"

def check_for_dir(dir: str):
    if not os.path.exists(dir):
        os.mkdir(dir)

def init():
    check_for_dir(DATA_DIR)
    check_for_dir(SQL_ORDERS_DIR)

def main():
    pass

def test1():
    pass
    
if __name__ == "__main__":
    init()
    test1()