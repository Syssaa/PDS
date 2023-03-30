from datetime import datetime
import pymongo
from pymongo import MongoClient  
import base64
import pymongo
import gridfs
from PIL import Image
from io import BytesIO
from PIL import Image 
class Voiture :
    def __init__(self,matricule='',marque='', date_circulation='',kilometrage='',cylindre='', description='', image=''):  
       self.matricule = matricule
       self.marque = marque
       self. date_circulation=  date_circulation
       self.kilometrage = kilometrage
       self.cylindre = cylindre
       self.description=description
       self.image=image

    def affiche(self):
        print((" {0:<8} | {1:<9} | {2:<15} |  {3:<8}| {4:<10} ").format(self.matricule,self.marque,self.date_circulation.strftime('%d/%m/%Y'),self.kilometrage,self.cylindre))
    def Affiche(self):
        print((" {0:<8} | {1:<9} | {2:<15} |  {3:<8}| {4:<10} ").format(self.matricule,self.marque,self.date_circulation,self.kilometrage,self.cylindre))
        print(self.description)
        self.image.show()

    def Saisir(self):
        self.matricule=input("matriqule: ")
        self.marque=input("marque:")
        self.date_circulation=input("date de circulation: ")
        self.date_circulation=datetime.strptime(self.date_circulation,'%d/%m/%Y')  
        self.kilometrage=input("Kilometrage: ")
        self.cylindre=input("Cylindre: ")
    
    def SaveDb(self):
     # Set up a MongoDB client to connect to your Atlas cluster
      client = MongoClient("mongodb+srv://lina:lina@cluster0.st42f.mongodb.net/test")
      # Access a database and a collection
      db = client.Agence_database
      collection = db.Agence_collection
      voiture = {'matricule':self.matricule,'marque':self.marque, 'date_circulation':self.date_circulation,'kilometrage':self.kilometrage,'cylindre':self.cylindre, 'description':self.description, 'image':self.image}
      result = collection.insert_one(voiture)
  
    def ReadbyMat(self,matricule_to_find):
        client = MongoClient("mongodb+srv://lina:lina@cluster0.st42f.mongodb.net/test")
        db = client.Agence_database
        collection = db.Agence_collection
        result = collection.find_one({'matricule': matricule_to_find})
        if result:
            self.matricule=result['matricule']
            self.marque=result['marque']
            self.date_circulation=result['date_circulation']
            self.kilometrage=result['kilometrage']
            self.cylindre= result['cylindre']
            self.description= result['description']
            # Get image data and convert it back to image
            image_bytes = result['image']            
            image = Image.open(BytesIO(image_bytes))
            self.image=image
            return True          
        else:
            return False
       
    def Update(self):
        # Set up a MongoDB client to connect to your Atlas cluster
        client = MongoClient("mongodb+srv://lina:lina@cluster0.st42f.mongodb.net/test")
        # Access a database and a collection
        db = client.Agence_database
        collection = db.Agence_collection
        # Find a document to update by its matricule value
        matricule_to_update = self.matricule
        query = {"matricule": matricule_to_update}

        # Define the update operation
        new_values = {"$set":{'matricule':self.matricule,'marque':self.marque, 'date_circulation':self.date_circulation,'kilometrage':self.kilometrage,'cylindre':self.cylindre, 'description':self.description, 'image':self.image}}

        # Update the document
        result = collection.update_one(query, new_values)

        # Check the result
        print(result.modified_count) 
   
    def Delete(self):
        client = MongoClient("mongodb+srv://lina:lina@cluster0.st42f.mongodb.net/test")
        db = client.Agence_database
        collection = db.Agence_collection
        result = collection.delete_one({'matricule': self.matricule})
        return result.deleted_count


if __name__=='__main__':

    with open("C:/Users/Lina/PDS/PDS/img/img_3015.jpg", "rb") as f:
      photo = f.read()
    v=Voiture("123M55","FIAT","12/12/2018",212000,12,"2019 FIAT RAV4 XLE avec seulement 15 000 miles au compteur ! Ce SUV est en excellent état et a été méticuleusement entretenu. Il dispose d'un moteur 4-cylindres de 2,5 L et d'une transmission automatique à 8 vitesses.",photo)
    found=v.ReadbyMat('123M55')
    print(found)
    v.SaveDb()
    #found=v.ReadbyMat('123M55')
    #print(found)
    #v.Affiche()

    #v.marque="BMW"
    #v.Update()
    #found=v.ReadbyMat('123M55')
    #print(found)
    #v.Affiche()

    #res=v.Delete()
    #print(res)
    #found=v.ReadbyMat('123M55')
    #print(found)
   





    
    
    #print(photo)
    # create image from bytes
    #image_stream = BytesIO(photo)
    #image = Image.open(image_stream)
    #image.show()
  #  v.Saisir()
   # v.affiche()