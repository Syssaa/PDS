from datetime import datetime

class Voiture:
    
    # def __init__(self):
    #     matricule=""
    #     marque=""
    #     date_circulation=""
    #     kilometrage=0
    #     cylindre=0
        
    # def __init__(self, matricule, marque,date_circulation,Kilometrage,cylindre):
    #     self.matricule=matricule
    #     self.marque=marque
    #     self.date_circulation=date_circulation
    #     self.kilometrage=Kilometrage
    #     self.cylindre=cylindre
    
    def __init__(self, matricule="", marque="", date_circulation="", kilometrage=0, cylindre=0):
        self.matricule = matricule
        self.marque = marque
        self.date_circulation = date_circulation
        self.kilometrage = kilometrage
        self.cylindre = cylindre
    
    def Saisir(self):
        
        self.matricule=input("matriqule: ")
        self.marque=input("marque: ")
        self.date_circulation=input("date de circulation: ")
        datec=datetime.strptime(self.date_circulation,'%d/%m/%Y') 
        self.date_circulation=datec.strftime('%d/%m/%Y')
        print(self.date_circulation)     
        self.kilometrage=input("Kilometrage: ")
        self.cylindre=input("Cylindre: ")



    def Afficher(self):
        datetime_object = datetime.strptime(self.date_circulation, '%d/%m/%Y')
        date_string = datetime_object.strftime('%d/%m/%Y')
        print(" {0:15s} | {1:8s} | {2:15s} | {3:15s} | {4:15s} |".format(self.matricule,self.marque,date_string,self.kilometrage,self.cylindre))
      # print(" {0:15s} | {1:8s} | {2:15s} | {3:15s} | {4:15s} |".format(self.matricule,self.marque,self.date_circulation,self.kilometrage,self.cylindre))

    

if __name__ == '__main__':
     
     v=Voiture()
     v.Saisir()
     v.Afficher()