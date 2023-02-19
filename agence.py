from voitures import Voiture

class Agence:
    def __init__(self):
        self.my_listcars = []
    def ajouter(self,v):
        #v=Voiture()
        #v.Saisir()
        v1=v 
        v1.Afficher()
        self.afficher()
        self.my_listcars.append(v1)
        print(self.my_listcars[0].matricule)
        
        

    def supprimer(self,v):
        self.my_listcars.remove(v)
 
    def rechercherparmat(self,mat):
        test=False
        for v in self.my_listcars:
            v1=Voiture()
            v1=v           
            if(v.matricule==mat):
             test=True
             break
        return test  
        
    def afficher(self):
        print("_____________________________")
        print(self.my_listcars)
        x=0
        for v in self.my_listcars:
            print("\n--",x+1,"----------------------")
            self.my_listcars[x].Afficher()
            x=x+1
            
        print("_____________________________")


    def trier_date(self):
        self.my_listcars.sort(key=lambda x: x.date_circulation)
    def getvoitureplusrecente(self):
        v=self.my_listcars[-1]
        v.Afficher()
    def getvoitureplusancienne(self):
        v=self.my_listcars[0]
        v.Afficher()
    

def convert_marque(self, marque):
        marque_mapping = {}
        for i, m in enumerate(set([v.marque for v in self.voitures])):
            marque_mapping[m] = i
        return marque_mapping[marque]

def convert_date_circulation(self, date_circulation):
        year, month, day = map(int, date_circulation.split('-'))
        return year + month/12 + day/365

def to_vector(self, marque, date_circulation, cylindre, kilometrage):
        marque = self.convert_marque(marque)
        date_circulation = self.convert_date_circulation(date_circulation)
        vector = np.array([marque, date_circulation, cylindre, kilometrage])
        return vector / np.linalg.norm(vector)

def search_voiture(self, marque, date_circulation, cylindre, kilometrage):
        print("in")
        search_vector = self.to_vector(marque, date_circulation, cylindre, kilometrage)
        print("in 1")
        scores = []
        for v in self.voitures:
            voiture_vector = self.to_vector(v.marque, v.date_circulation, v.cylindre, v.kilometrage)
            similarity = np.dot(search_vector, voiture_vector)
            scores.append((v, similarity))
        print("in 2")
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores



if __name__ == '__main__':
    a =Agence()
    v=Voiture()
    v.Saisir()
    a.ajouter(v)
    v1=Voiture()
    v1.Saisir()
    a.ajouter(v1)
    v2=Voiture()
    v2.Saisir()
    a.ajouter(v2)
    found=a.rechercherparmat("12")
    print(found)
    
    a.afficher()
    a.trier_date()
    a.afficher()
    a.getvoitureplusancienne()
    a.getvoitureplusrecente()
    a.search_voiture()
    
