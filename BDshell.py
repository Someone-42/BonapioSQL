"""
Module permettant d'interagir avec le SGBD sqlite en ligne de commande dans le shell

Placer le module dans le répertoire où stocker la base de donnée puis l'exécuter avant d'utiliser les différentes fonctions suivante dans le shell :

affiche(nom_base)
execute(nom_base,ordre_SQL)
execute_fichier(nom_base,nom_fichier)

Remarque : Le nom de la base doit avoir pour extension ".db"


Créé le 25-11-2021
par Thomas Ravary

"""


import sqlite3

import os
PATH = os.getcwd()+"\\"

def get_connection(nom_base):
    conn=sqlite3.connect(PATH+nom_base)
    conn.execute("PRAGMA foreign_keys = 1")
    return conn

def print_tuple(t,largeur_colonne,fill=" ",sep="",align="<"):
    print(sep.join(["{{:{0}{1}{2}}}".format(fill,align,largeur).format(value) for (value,largeur) in zip(t,largeur_colonne)]))

def print_cursor_selection(cursor,largeur_min=15):
    names=[d[0] for d in cursor.description]
    rows=[row for row in cursor]
    largeur_colonne = [ max(largeur_min,len(names[k])+1,max([0]+[len(str(row[k]))+1 for row in rows])) for k in range(len(names))]
    print_tuple(names,largeur_colonne)
    print_tuple(len(names)*[" "],largeur_colonne,fill="-",align=">")
    for row in rows:
        print_tuple(row,largeur_colonne)
    print()

def affiche_base(nom_base):
    """ Affiche toutes les tables de la base dont le nom est donné en argument """
    conn=get_connection(nom_base)
    cur=conn.cursor()
    table_names=[table_names_d[0] for table_names_d in cur.execute("SELECT name FROM sqlite_master WHERE type='table';")]
    for table_name in table_names:
        table_name=table_name
        print(table_name)
        cur.execute("SELECT * FROM "+table_name)
        print_cursor_selection(cur)
    conn.close()

def execute(nom_base,ordre_SQL):
    """ Execute l'ordre_SQL donné sous forme de chaine de caractère donné en argument sur la base donnée en argument """
    conn=get_connection(nom_base)
    cur=conn.cursor()
    cur.execute(ordre_SQL)
    if ordre_SQL[:6]=="SELECT":
        print_cursor_selection(cur)
    conn.commit()
    conn.close()

def execute_fichier(nom_base,nom_fichier):
    """ Execute les ordres SQL écrits dans le fichier dont le nom est donné en argument sur la base donnée en argument """
    with open(PATH+nom_fichier,"r") as f:
        ordres=f.read().split(";")
    conn=get_connection(nom_base)
    cur=conn.cursor()
    for ordre in ordres:
        print(">"+ordre)
        cur.execute(ordre)
        if ordre[:6]=="SELECT":
            print_cursor_selection(cur)
    conn.commit()
    conn.close()

