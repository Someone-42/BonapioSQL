import DBUtils as db
import BDshell as dbs
import DataGen as dg
import os

# Directories
DATA_DIR = "./Data/"
SQL_ORDERS_DIR = "./SQLOrders/"

# User Database
USER_DB_NAME = DATA_DIR + "Utilisateurs.db"
USER_DB_ORDER_FILE = SQL_ORDERS_DIR + "CreateUserDB.txt"

def check_for_dir(dir: str):
    if not os.path.exists(dir):
        os.mkdir(dir)

def init():
    check_for_dir(DATA_DIR)
    check_for_dir(SQL_ORDERS_DIR)
    db.reset_db(USER_DB_NAME, USER_DB_ORDER_FILE)

def main():
    pass

def test1():
    dbs.affiche_base(USER_DB_NAME)
    
    # Values insertion test
    dbs.execute(USER_DB_NAME, db.get_insert_order("Utilisateur", "sarrasin", "jean", dg.generate_telephone()))
    dbs.execute(USER_DB_NAME, db.get_insert_order("Utilisateur", "sarrasin", "michel", dg.generate_telephone()))
    dbs.execute(USER_DB_NAME, db.get_insert_order("Utilisateur", "martin", "paul", dg.generate_telephone()))

    dbs.affiche_base(USER_DB_NAME)

if __name__ == "__main__":
    init()
    test1()