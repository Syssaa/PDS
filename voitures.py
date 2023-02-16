from datetime import datetime

class Voiture:
    
    def __init__(self):
        matricule=""
        marque=""
        date_circulation=""
        kilometrage=0
        cylindre=0
        
    #def __init__(self, matricule, marque,date_circulation,Kilometrage,cylindre):
     #   self.matricule=matricule
      #  self.marque=marque
       # self.date_circulation=date_circulation
        #self.kilometrage=Kilometrage
        #self.cylindre=cylindre
    def Saisir(self):
        
        self.matricule=input("matriqule: ")
        self.marque=input("marque: ")
        self.date_circulation=input("date de circulation: ")
        self.date_circulation=datetime.strptime(self.date_circulation,'%d/%m/%Y')      
        self.kilometrage=input("Kilometrage: ")
        self.cylindre=input("Cylindre: ")



    def Afficher(self):
       # datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
        print(" {0:15s} | {1:8s} | {2:15s} | {3:15s} | {4:15s} |".format(self.matricule,self.marque,datetime.strftime(self.date_circulation, '%m/%d/%Y'),self.kilometrage,self.cylindre))
        #print(self.matricule[0:15],"|",self.marque[0:8],"|",datetime.strftime(self.date_circulation, '%m/%d/%y'))
    
    

if __name__ == '__main__':
     print("hello")
     
     v=Voiture()
     v.Saisir()
     v.Afficher()