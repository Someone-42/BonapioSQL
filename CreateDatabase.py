import BDshell as db
import os

def create_database(db_name: str):
    """ Cree la database en suivant le modele relationel """
    f = open("Programmation/TDs/TD - Brevet des colleges/CreateDB.txt", "r")
    for order in f.read().split(';'): # Je separe les ordres par des ; et non pas des \n
        db.execute(db_name, order)

def reset_db(db_name: str):
    """ Remet la database a 0 (utile pour les erreurs) """
    if os.path.exists(db_name): os.remove(db_name)
    create_database(db_name)

def get_insert_order(table_name: str, *values) -> str:
    """ Renvoies l'ordre d'insert a partir des valeurs """
    s = []
    for v in values:
        if isinstance(v, str):
            s.append("'" + v.replace("'", "''") + "'")
        else:
            s.append(str(v))
    return "INSERT INTO " + table_name + " VALUES (" + ", ".join(s) + ");"

def check_value(value, l: list) -> bool:
    """ Regardes si la valeur est une clé """
    if value not in l:
        l.append(value)
        return True
    return False