from voitures import Voiture
from datetime import datetime

import csv
import os

class Agence:
    def __init__(self):
        self.my_listcars = []
        #initialize le fichiers csv
        file_path = 'voitures.csv'
        if os.path.getsize(file_path) == 0:
         with open("voitures.csv", "w", newline="") as file:
             writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
             writer.writerow(["Matricule", "Marque", "Date de circulation", "Kilometrage", "Cylindre"])
    
    def load(self):#lire les données d'un csv
        self.my_listcars = []
        # read the Voiture objects from the CSV file
        with open("voitures.csv", "r", newline="") as file:
            reader = csv.reader(file,delimiter=';')
            header = next(reader) # skip header row
            voitures = []
            for row in reader:
                print(row)

                mat,marque,DC,km,cy=row
                v=Voiture(mat,marque,DC,km,cy)
                self.my_listcars.append(v)

    def ajouter(self,v):#ajouter a un csv
        v1=v        
        with open("voitures.csv", "a", newline="") as file:
         writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
         writer.writerow([v1.matricule, v1.marque, v1.date_circulation, v1.kilometrage, v1.cylindre])
        
        self.load()
        
        
        

    def supprimer(self,v):
        self.load()
        if(self.rechercherparmat(v.matricule)):
            for voiture in self.my_listcars:
             v1=Voiture()
             v1=voiture 
             #print(voiture.matricule)          
            if(voiture.matricule==v.matricule):
             self.my_listcars.remove(voiture)

             with open("voitures.csv", "w", newline="") as file:
              writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
              writer.writerow(["Matricule", "Marque", "Date de circulation", "Kilometrage", "Cylindre"])
             for car in self.my_listcars:
              v1=Voiture()
              v1=car
              v1.Afficher()
              with open("voitures.csv", "a", newline="") as file:
                writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
                writer.writerow([v1.matricule, v1.marque, v1.date_circulation, v1.kilometrage, v1.cylindre])
    
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
        self.load()
        x=0
        print(len(self.my_listcars))

        print("_____________________________")
        
        for v in self.my_listcars:
            print("\n------------------------")
            self.my_listcars[x].Afficher()
            x+=1
        print("_____________________________")
            
            
        


    def trier_date(self):
        print("sorting")
        sorted_voitures = sorted(self.my_listcars, key=lambda x: datetime.strptime(x.date_circulation, "%d/%m/%Y"))
        self.my_listcars.clear()
        print("endsorting")
        for voiture in sorted_voitures:
            v1=Voiture()
            v1=voiture
            v1.Afficher()      
            self.my_listcars.append(v1)
            print("sorting")
        with open("voitures.csv", "w", newline="") as file:
              writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
              writer.writerow(["Matricule", "Marque", "Date de circulation", "Kilometrage", "Cylindre"])
        for car in self.my_listcars:
              v1=Voiture()
              v1=car
              v1.Afficher()
              with open("voitures.csv", "a", newline="") as file:
                writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
                writer.writerow([v1.matricule, v1.marque, v1.date_circulation, v1.kilometrage, v1.cylindre])


    def getvoitureplusrecente(self):
        v=self.my_listcars[-1]
        v.Afficher()
    def getvoitureplusancienne(self):
        v=self.my_listcars[0]
        v.Afficher()




if __name__ == '__main__':
    a=Agence()
    a.afficher()
   # v=Voiture()
  #  v.Saisir()
    #print("-------Ajouter test-----")
    #a.ajouter(v)
    #a.afficher()
    #print("-------supprimer test-----")
    #a.supprimer(v)
    #a.afficher()
    #print("-------found test-----")
    #found=a.rechercherparmat("503")
    #print(found)
    #print("-------End of found test-----")
    
   # a.afficher()
    print("-------sorting test-----")
    a.trier_date()
    a.afficher()
    print("-------plus anc plus rec test-----")
    a.getvoitureplusancienne()
    a.getvoitureplusrecente()
    # a.search_voiture()