from voituretransformation import VoitureTransformation
from voitures import Voiture
from transformations_images import TransformationImageVoiture
from transformations_texte import TransformationVoitureTexte
import pandas as pd
import numpy as np
import os
class Recherche:
       def __init__(self):
              pass
       
       def calculedistance(self,Data,Query):
        distances = []
        new_=Query.iloc[0]
        for i in range(len(Data)):
            Data_row = Data.iloc[i]
            distance = np.sqrt(np.sum((Data_row - new_)**2))
            distances.append(distance)
        #Data['Distance']=distances
        return distances

        
       def RechercheQuery(self):
            v=VoitureTransformation()
            # chemin de fichier excel
            data_path='C:/Users/Lina/PDS/PDS/voitures.csv'
            data=pd.read_csv(data_path , sep=';')
            v.fit(data)
            df=v.transformer(data)
            #print(df.columns)
            #print(df)
            vt=Voiture()
            vt.Saisir()
            vt.affiche()
            new_rows = {'Matricule':vt.matricule,'Marque': vt.marque,'Date de circulation':vt.date_circulation,'Kilometrage': vt.kilometrage, 'Cylindre': vt.cylindre}
            new_rowdf = pd.DataFrame([new_rows])
            df_v=v.transformer(new_rowdf)
            #print(df_v.columns)
            #print(df_v)
            distances=self.calculedistance(df,df_v)
            data['distances']=distances
            df_sorted = data.sort_values('distances', ascending=True)
            print(df_sorted.columns)
            print(df_sorted)

            
       def RechercheText(self):
          transformer = TransformationVoitureTexte()
          df=transformer.getCorpus(transformer.getPaths())
          #result=pd.DataFrame()
          Corpus=df['Corpus']
          #print(df)
          transformer.fit(Corpus)
          X=transformer.transform(Corpus)
          data=X.toarray()
          NewText="2018 Honda Civic LX avec seulement 20 000 miles au compteur ! Cette voiture est en excellent état et a été régulièrement entretenue. Elle est équipée d'un moteur 4-cylindres de 2,0 L et d'une transmission à variation continue (CVT)."
          NewTextX=transformer.transform([NewText])
          query=NewTextX.toarray()
          distances = np.sqrt(np.sum((data - query) ** 2, axis=1))
          print("now\n")
          print(distances)
          df['distances']=distances
          print(df)
          df_sorted = df.sort_values('distances', ascending=True)

          print(df_sorted)

       
      
       
       def RechercheImage(self):
          img=TransformationImageVoiture()
          dir_path = os.getcwd()
          data_path=dir_path+'\\img'
          nameslist = os.listdir(data_path)
          imagespath=[]
          for name in nameslist:   
               image_path = os.path.join(data_path, name) 
               if image_path.endswith('.jpg'):
                    imagespath.append(image_path)
                    Mat=img.transform(imagespath,100*200)
          print(Mat)
          result=pd.DataFrame()
          result['url']=imagespath

          ###New image
          data_path=dir_path+'\\imgquery'
          nameslist = os.listdir(data_path)
          imagespath=[]
          for name in nameslist:   
           image_path = os.path.join(data_path, name) 
           if image_path.endswith('.jpg'):
             imagespath.append(image_path)
             MatNew=img.transform(imagespath,100*200)
          print(MatNew)

          distances = np.sqrt(np.sum((Mat - MatNew) ** 2, axis=1))
          print("now\n")
          print(distances)
          result['distances']=distances
          df_sorted = result.sort_values('distances', ascending=True)

          print(df_sorted)


import pymongo
from pymongo import MongoClient         
if __name__ == '__main__':
     #r=Recherche()
     #r.RechercheQuery()
     #r.RechercheImage()
    # r.RechercheText()
    

     # Set up a MongoDB client to connect to your Atlas cluster
     client = MongoClient("mongodb+srv://lina:lina@cluster0.st42f.mongodb.net/test")

     # Access a database and a collection
     db = client.Agence_database
     collection = db.Agence_collection

     # Insert a document into the collection
     document = {"name": "John", "age": 30}
     result = collection.insert_one(document)
     print("Inserted document with ID:", result.inserted_id)

     # Find all documents in the collection
     for document in collection.find():
      print(document)
