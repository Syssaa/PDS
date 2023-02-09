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
     
def liste_en_matrice(self):
    matrice = np.zeros((len(self), 5))
    for i, voiture in enumerate(self):
        matrice[i, 0] = voiture['matricule']
        matrice[i, 1] = voiture['marque']
        matrice[i, 2] = voiture['date_circulation']
        matrice[i, 3] = voiture['kilometrage']
        matrice[i, 4] = voiture['cylindre']
    return matrice 
def distance_voitures(self,nouvelle_voiture, matrice_voitures):
    distances = np.zeros(matrice_voitures.shape[0])
    for i, voiture in enumerate(matrice_voitures):
        distances[i] = np.linalg.norm(nouvelle_voiture - voiture)
    return distances#La fonction np.argsort trie les indices du tableau distances en ordre croissant,
    #La fonction crée un tableau distances pour stocker les distances pour chaque voiture. 
    #Ensuite, la fonction boucle sur les voitures dans la matrice matrice_voitures et calcule la distance entre la nouvelle voiture et chaque voiture en utilisant la fonction np.linalg.norm. La fonction np.linalg.norm calcule la norme (distance) entre deux vecteurs.

def trier_distances(self,distances):
    distances = np.argsort(distances)
    return distances#trie les distances entre une nouvelle voiture et les voitures de l'agence en utilisant la fonction argsort de NumPy: 

def afficher_voitures_similaires(indices, matrice_voitures, nombre_similaires):
    print("Voitures les plus similaires :")
    for i in range(nombre_similaires):
        index = indices[i]
        voiture = matrice_voitures[index]
        print("- Voiture avec matricule:", voiture[0], " et kilometrage:", voiture[3])


     