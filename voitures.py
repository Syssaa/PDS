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
       self.marque = marque.upper()
       self. date_circulation=  date_circulation
       self.kilometrage = kilometrage
       self.cylindre = cylindre
       self.description=description
       self.image=image

    def affiche(self):
        print((" {0:<8} | {1:<9} | {2:<15} |  {3:<8}| {4:<10} ").format(self.matricule,self.marque,self.date_circulation.strftime('%d/%m/%Y'),self.kilometrage,self.cylindre))
    def Affiche(self):
        print((" {0:<8} | {1:<9} | {2:<15} |  {3:<8}| {4:<10} ").format(self.matricule,self.marque,self.date_circulation,self.kilometrage,self.cylindre))
        

    def AfficheFull(self):
        print((" {0:<8} | {1:<9} | {2:<15} |  {3:<8}| {4:<10} ").format(self.matricule,self.marque,self.date_circulation,self.kilometrage,self.cylindre))
        print(self.description)
        self.image.show()

    def Saisir(self):
        self.matricule=input("matriqule: ")
        self.marque=input("marque:")
        self.marque=self.marque.upper()
        self.date_circulation=input("date de circulation: ")
        self.date_circulation=datetime.strptime(self.date_circulation,'%d/%m/%Y')  
        self.kilometrage=input("Kilometrage: ")
        self.cylindre=input("Cylindre: ")
        self.description=input("Description: ")
    
    def SaveDb(self):
     # Set up a MongoDB client to connect to your Atlas cluster
      client = MongoClient("mongodb+srv://lina:lina@cluster0.st42f.mongodb.net/test")
      # Access a database and a collection
      db = client.Agence_database
      collection = db.Agence_collection
      voiture = {'matricule':self.matricule,'marque':self.marque, 'date_circulation':self.date_circulation,'kilometrage':self.kilometrage,'cylindre':self.cylindre, 'description':self.description, 'image':self.image}
      result = collection.insert_one(voiture)
  
    def ReadbyMat(self):
        client = MongoClient("mongodb+srv://lina:lina@cluster0.st42f.mongodb.net/test")
        db = client.Agence_database
        collection = db.Agence_collection
        result = collection.find_one({'matricule': self.matricule})
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
    #Filling Database
    # with open("img\TOYOTAYARIS1.jpg", "rb") as f:
    #   photo = f.read()
    # #1
    # v=Voiture("TUN4948","TOYOTA","12/10/2013",1002,4,"Yaris MK1 2 portes, Importer En 2006 fab en Japon, Très économique 4cv diesel Moteur 4cy 1.4 d4d diesel Toute options, Climatisé, Fermeture Central, Assistée, Abs, Vitre Électrique 4 pneus neuf, disques et plaquettes, tous les vitre d origine, intérieur très propre",photo)    
    # v.SaveDb()
   
    # #2
    # with open("img\im2.jpg", "rb") as f:
    #   photo = f.read()
    # v=Voiture("TUN1948","AUDI","09/09/2018",110000,4,"toit panoramique jantes allu boite auto régulateur de vitesse LED rétroviseurs rabattables démarrage sans clé écran rétroviseurs électriques vitres électriques accoudoir central avant climatisation automatique kit téléphone bluetooth ordinateur de bord volant cuir multifonctions",photo)    
    # v.SaveDb()
   
    # #3
    # with open("img\im3.jpg", "rb") as f:
    #   photo = f.read()
    # v=Voiture("TUN448","MAZDA","02/02/2019",86000,3,"toit ouvrant jantes allu écran affichage tête haute sellerie cuir camera de recul rétroviseurs électriques vitres électriques accoudoir central avant climatisation automatique kit téléphone ordinateur de bord volant cuir multifonctions",photo)    
    # v.SaveDb()
   
    # #4
    # with open("img\im4.jpg", "rb") as f:
    #   photo = f.read()
    # v=Voiture("TUN4958","LEON","06/06/2017",138000,4,"écran  camera de recul  toit panoramique  jantes allu  LED  rétroviseurs électriques  vitres électriques  accoudoir central avant  radars de stationnement  Climatisation auto  commandes vocales  kit téléphone  régulateur de vitesse  ordinateur de bord  volant cuir multifonctions",photo)    
    # v.SaveDb()
   
    # #5
    # with open("img\im5.jpg", "rb") as f:
    #   photo = f.read()
    # v=Voiture("TUN5955","RENAULT","12/16/2013",145000,4,"Renault Twingo RS Line Modele : 2013 Kilométrage : 145 000 km  Tu 180 Toute option Boite automatique Puissance fiscale : 8 cv Energie : essence",photo)    
    # v.SaveDb()
   
    # #6
    # with open("img\im6.jpg", "rb") as f:
    #   photo = f.read()
    # v=Voiture("TUN1159","TOYOTA","1/07/2011",165000,3,"toyota yaris Voiture en excellent état général, intérieur et extérieur très bien entretenus AUTORADIO Commandes au volant CONNECTIVITÉ USB  Apple Carplay  AUX  Android Auto  Bluetooth ECRAN Tactile  7 pouces SELLERIE Tissu VOLANT Multi-fonctions",photo)    
    # v.SaveDb()
   
    # #7
    # with open("img\im7.jpg", "rb") as f:
    #   photo = f.read()
    # v=Voiture("TUN1200","MERCEDES","04/04/2022",9000,4,"MERCEDES-BENZ CLASSE C 1.5 pack AMG pack Night LED Digital Light toit panoramique ouvrant aide à la conduite éclairage d’ambiance sièges à réglage électrique sièges chauffant/ventilés sièges à mémoire sellerie cuir/alcantara système Start & Stop aide parking av/ar jantes allu sport AMG 19 plattes au volant rétroviseurs rabattables électriquement rétroviseurs électriques et dégivrants 4 vitres électriques accoudoir central avant climatisation automatique multi zone compteur numérique grand écran kit téléphone main libre ordinateur de bord prise audio USB régulateur de vitesse volant cuir crochet d’attelage/remorquage détecteur de pluie essuieglaces automatiques feux automatiques tapis AMG éclairage au sol logo Mercedes",photo)    
    # v.SaveDb()
   
    # #8
    # with open("img\im8.jpg", "rb") as f:
    #   photo = f.read()
    # v=Voiture("TUN3302","BMW","04/06/2010",114000,6,"Kilométrage certifié série 219 prix négociable j accepte l échange contre une voiture moins cher CARROSSERIE 4 x 4 ENERGIE Diesel PUISSANCE FISCALE 19 CV BOÎTE Automatique TRANSMISSION Intégrale COULEUR Noir",photo)    
    # v.SaveDb()
   
    # #9
    # with open("img\im9.jpg", "rb") as f:
    #   photo = f.read()
    # v=Voiture("TUN42827","BMW","12/10/2012",148000,6,"BMW serie 5 système Start & Stop sièges électriques rideaux arrière et lateraux aide parking av/ar rétroviseurs électriques et dégivrants climatisation automatique multi zone écran kit téléphone main libre ordinateur de bord prise audio USB régulateur de vitesse volant cuir détecteur de pluie essuieglaces automatiques feux automatiques BMW SÉRIE 5 2.0 CARROSSERIE Berline ENERGIE Essence PUISSANCE FISCALE 10 CV BOÎTE Automatique TRANSMISSION Traction COULEUR Noir",photo)    
    # v.SaveDb()
   
    # #10
    # with open("img\im10.jpg", "rb") as f:
    #   photo = f.read()
    # v=Voiture("TUN2827","VOLKSWAGEN","10/10/2018",76000,4,"VOLKSWAGEN GOLF 7 JOIN CARROSSERIE Citadine ENERGIE Diesel PUISSANCE FISCALE 5 CV BOÎTE Manuelle TRANSMISSION Traction COULEUR Jaune",photo)    
    # v.SaveDb()
   
    # #11
    # with open("img\im11.jpg", "rb") as f:
    #   photo = f.read()
    # v=Voiture("TUN3266","AUDI","10/08/2008",188000,6,"AUDI Q7 3.00 CARROSSERIE 4 x 4 ENERGIE Diesel PUISSANCE FISCALE 16 CV BOÎTE Automatique TRANSMISSION Traction COULEUR Noir 4 roues motrices S Line Seuil de porte S Line marches pieds boite auto palettes au volant fermeture hayon électrique écran camera de recul boiserie ronce de noyer interieur cuir sièges électriques radar de stationement rétroviseurs électriques vitres électriques accoudoir central avant climatisation automatique 4 zones kit téléphone ordinateur de bord volant cuir multifonctions",photo)    
    # v.SaveDb()

   # v1=Voiture()
   # v1.matricule='TUN3266'
   # found=v1.ReadbyMat()
   # print(found)
   # v1.Affiche()

    #v.marque="BMW"
    #v.Update()
    #found=v.ReadbyMat('TUN3266')
    #print(found)
    #v.Affiche()

    #res=v.Delete()
    #print(res)
    #found=v.ReadbyMat('TUN3266')
    #print(found)

    #  v.Saisir()
    # v.affiche()
    pass