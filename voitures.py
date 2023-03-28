from datetime import datetime
class Voiture :
    def __init__(self,matricule='',marque='', date_circulation='',kilometrage='',cylindre=''):  
       self.matricule = matricule
       self.marque = marque
       self. date_circulation=  date_circulation
       self.kilometrage = kilometrage
       self.cylindre = cylindre
    def affiche(self):
        print((" {0:<8} | {1:<9} | {2:<15} |  {3:<8}| {4:<10} ").format(self.matricule,self.marque,self.date_circulation.strftime('%d/%m/%Y'),self.kilometrage,self.cylindre))
    def Affiche(self):
        print((" {0:<8} | {1:<9} | {2:<15} |  {3:<8}| {4:<10} ").format(self.matricule,self.marque,self.date_circulation,self.kilometrage,self.cylindre))

    def Saisir(self):
        self.matricule=input("matriqule: ")
        self.marque=input("marque:")
        self.date_circulation=input("date de circulation: ")
        self.date_circulation=datetime.strptime(self.date_circulation,'%d/%m/%Y')  
        self.kilometrage=input("Kilometrage: ")
        self.cylindre=input("Cylindre: ")

if __name__=='__main__':
    v=Voiture()
    
    v.Saisir()
    v.affiche()