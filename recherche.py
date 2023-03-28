from voituretransformation import VoitureTransformation
from voitures import Voiture
import pandas as pd
import numpy as np
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
            df_sorted = data.sort_values('distances')
            print(df_sorted.columns)
            print(df_sorted)

            
       def RechercheText(self):
            pass
       def RechercheImage(self):
            pass
if __name__ == '__main__':
     r=Recherche()
     r.RechercheQuery()