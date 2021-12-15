
class User:
    __slots__=("nom", "prenom", "telephone")
    def __init__(self, nom : str, prenom : str, telephone : str) -> None:
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
