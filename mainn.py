from recherche import Recherche
from voitures import Voiture
from agence import Agence
from PIL import Image


if __name__ == '__main__':
     a=Agence()
     #a.readAll()
     #a.AfficheAll()
     r=Recherche()
     #vt=Voiture("TUN12","TOYOTA","15/05/2014","3000","4")
     #r.RechercheQuery_VDB(vt)
     #r.RechercheImage_VDB("img/im2.jpg")
     r.RechercheText_VDB("Yaris neuf et propre boite Toute options climatisé")
     
