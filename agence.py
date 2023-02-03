class Agence:
    def __init__(self, nom, adresse, telephone, email, liste_voitures):
        self.nom = nom
        self.adresse = adresse
        self.telephone = telephone
        self.email = email
        self.liste_voitures = liste_voitures

    def afficher(self):
        print("Nom: ", self.nom)
        print("Adresse: ", self.adresse)
        print("Telephone: ", self.telephone)
        print("Email: ", self.email)

    def afficher_voitures(self):
        for voiture in self.liste_voitures:
            voiture.afficher()
    def ajouter_voitures(self,voiture):
        self.liste_voitures.append(voiture)
    def supprimer(self,v):
        self.liste_voitures.remove(v)
    
    def rechercher (self,matricule):
        for voiture in self.liste_voitures:
            if voiture.matricule==matricule:
                return voiture
                return None
    def trier_date_circulation (self):
     self.liste_voitures.sort(key=lambda voiture: date_circulation)
     print(liste_voitures)
    def get_voiture_plusRecente(self):
        print("Voiture la plus recente: ")
        return self.liste_voitures[-1]
    
    def get_voiture_plusAncienne(self):
        print("Voiture la plus ancienne: ")
        return self.liste_voitures[0]
    