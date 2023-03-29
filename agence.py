from voitures import Voiture
from datetime import datetime
import pandas as pd
import csv
import os
from pymongo import MongoClient  
import base64
import pymongo
import gridfs
from io import BytesIO
from PIL import Image

class Agence:
    
    def __init__(self):
        self.data=pd.DataFrame()
        self.my_listcars = []
        #initialize le fichiers csv
        file_path = 'voitures.csv'
        if os.path.getsize(file_path) == 0:
         with open("voitures.csv", "w", newline="") as file:
             writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
             writer.writerow(["Matricule", "Marque", "Date de circulation", "Kilometrage", "Cylindre"])
# pour version CSV    
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
# pour version CSV
    def ajouter(self,v):#ajouter a un csv
        v1=v        
        with open("voitures.csv", "a", newline="") as file:
         writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
         writer.writerow([v1.matricule, v1.marque, v1.date_circulation, v1.kilometrage, v1.cylindre])
        
        self.load()
# pour version CSV       
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
# pour version CSV   
    def rechercherparmat(self,mat):
        test=False
        for v in self.my_listcars:
            v1=Voiture()
            v1=v           
            if(v.matricule==mat):
             test=True
             break
        return test  
# pour version CSV      
    def afficher(self):
        self.load()
        x=0
        print(len(self.my_listcars))

        print("_____________________________")
        
        for v in self.my_listcars:
            print("\n------------------------")
            self.my_listcars[x].Affiche()
            x+=1
        print("_____________________________")
# pour traitement dataframe
    def preprocessing(self,df):
        df_copie=df
        # suppression de la colonne matricule
        df_copie.drop('Matricule', axis=1, errors='ignore',inplace=True)
        # transformation de la colonne date_circulation en age voiture
        df_copie['Date de circulation'] = pd.to_datetime(df_copie['Date de circulation'])
        df_copie['AgeV'] = datetime.datetime.now().year - df_copie['Date de circulation'].dt.year
        df_copie = df_copie.drop(columns=['Date de circulation'], axis=1)
# pour version CSV
    def trier_date(self):
        print("sorting")
        sorted_voitures = sorted(self.my_listcars, key=lambda x: datetime.strptime(x.date_circulation, "%d/%m/%Y"))
        self.my_listcars.clear()
        print("endsorting")
        for voiture in sorted_voitures:
            v1=Voiture()
            v1=voiture
            v1.Affiche()      
            self.my_listcars.append(v1)
            print("sorting")
        with open("voitures.csv", "w", newline="") as file:
              writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
              writer.writerow(["Matricule", "Marque", "Date de circulation", "Kilometrage", "Cylindre"])
        for car in self.my_listcars:
              v1=Voiture()
              v1=car
              v1.Affiche()
              with open("voitures.csv", "a", newline="") as file:
                writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
                writer.writerow([v1.matricule, v1.marque, v1.date_circulation, v1.kilometrage, v1.cylindre])
# pour version CSV
    def getvoitureplusrecente(self):
        v=self.my_listcars[-1]
        v.Affiche()
# pour version CSV
    def getvoitureplusancienne(self):
        v=self.my_listcars[0]
        v.Affiche()

#pour version DB
    def readAll(self):
        client = MongoClient("mongodb+srv://lina:lina@cluster0.st42f.mongodb.net/test")
        db = client.Agence_database
        collection = db.Agence_collection
        cursor = collection.find({})
        datas = list(cursor)
        self.data = pd.DataFrame(columns=['Matricule', 'Marque', 'Date de circulation', 'Kilometrage', 'Cylindre', 'description', 'image'])

        for item in datas:
            Matricule= item['matricule']
            Marque=item['marque']
            date=item['date_circulation']
            Km=item['kilometrage']
            Cy=item['cylindre']
            desc=item['description']
            img=item['image']
            image = Image.open(BytesIO(img))
            row = {
                'Matricule': Matricule,
                'Marque': Marque,
                'Date de circulation':date,
                'Kilometrage': Km,
                'Cylindre': Cy,
                'description':desc,
                'image': image
            }
            self.data = self.data.append(row, ignore_index=True)
            #print(data)
#pour version DB
    def AfficheAll(self):
     for index, row in self.data.iterrows():
        v=Voiture(row['Matricule'],row['Marque'],row['Date de circulation'],row['Kilometrage'],row['Cylindre'],row['description'],row['image'])
        v.Affiche()
       
    


if __name__ == '__main__':
    a=Agence()
    a.readAll()
    a.AfficheAll()
   # a.afficher()
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
    #print("-------sorting test-----")
    #a.trier_date()
    #a.afficher()
    #print("-------plus anc plus rec test-----")
    #a.getvoitureplusancienne()
    #a.getvoitureplusrecente()
    # a.search_voiture()