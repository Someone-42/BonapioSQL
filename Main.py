import DBUtils as db
import BDshell as dbs
import DataGen as dg
import os

from Generator import Generator

# Directories
DATA_DIR = "./Data/"
SQL_ORDERS_DIR = "./SQLOrders/"

# User Database
USER_DB_NAME = DATA_DIR + "Utilisateurs.db"
USER_DB_ORDER_FILE = SQL_ORDERS_DIR + "CreateUserDB.txt"

# AutoInsert file
AUTO_INSERT_ORDERS_FILE = SQL_ORDERS_DIR + "InsertOrders.txt"

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

def fill_db(names_freq: list, first_names_freq: list, quantity: int = 42):
    """ Inserts {quantity} amounts of random generated users in the database """
    # Generators
    first_name_gen = Generator(first_names_freq)
    name_gen = Generator(names_freq)

    # Creates a file containing SQL Insert orders to insert users
    with open(AUTO_INSERT_ORDERS_FILE, "w") as f:
        for i in range(quantity):
            f.write(db.get_insert_order("Utilisateur", name_gen.next(), first_name_gen.next(), dg.generate_telephone()))
    

    # Reads the file and executes its orders
    dbs.execute_fichier(USER_DB_NAME, AUTO_INSERT_ORDERS_FILE)

if __name__ == "__main__":
    init()
    # fill_db()
    dbs.affiche_base()