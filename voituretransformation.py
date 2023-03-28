from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
import pandas as pd
from voitures import Voiture
import datetime as datetime

class VoitureTransformation (BaseEstimator, TransformerMixin):
    def __init__(self):
        self.encoder = OneHotEncoder(handle_unknown='ignore')
        self.scaler = MinMaxScaler()
    
    def fit(self, X, y=None):
        X_copy = X.copy()
        self.encoder.fit( X_copy[['Marque']])
    
    def transformer(self, X, y=None):
        df_copie = X.copy()
        #### preprocessing ###
        # suppression de la colonne matricule
        df_copie.drop('Matricule', axis=1, errors='ignore',inplace=True)
        # transformation de la colonne date_circulation en age voiture
        df_copie['Date de circulation'] = pd.to_datetime(df_copie['Date de circulation'])
        df_copie['AgeV'] = datetime.datetime.now().year - df_copie['Date de circulation'].dt.year
        df_copie = df_copie.drop(columns=['Date de circulation'], axis=1)
        #### OHE ###
        encoded = self.encoder.transform(df_copie[['Marque']]).toarray()
        cols = self.encoder.get_feature_names_out(['Marque'])
        df_encoded = pd.DataFrame(encoded, columns=cols)

        # normalize the 'Kilometrage' and 'Cylindre' columns
        if len(df_copie)>1:
         df_normalized = pd.DataFrame(self.scaler.fit_transform(df_copie[['Kilometrage', 'Cylindre','AgeV']]), columns=['Kilometrage', 'Cylindre','AgeV'])
        else:
         df_normalized = pd.concat([pd.DataFrame(encoded, columns=cols), pd.DataFrame(self.scaler.transform(pd.DataFrame(df_copie, index=[0])[['Kilometrage', 'Cylindre', 'AgeV']]), columns=['Kilometrage', 'Cylindre', 'AgeV'])], axis=1)

        # combine the encoded and normalized DataFrames
        df_combined = pd.concat([df_encoded, df_normalized], axis=1)

        return df_combined
    
if __name__ == '__main__':

  v=VoitureTransformation()
  # chemin de fichier excel
  data_path='C:/Users/Lina/PDS/PDS/voitures.csv'
  df=pd.read_csv(data_path , sep=';')
  v.fit(df)
  df=v.transformer(df)
  print(df.columns)
  print(df)
  vt=Voiture('','FIAT',"12/12/2022",1235445,54235)

  new_rows = {'Matricule':vt.matricule,'Marque': vt.marque,'Date de circulation':vt.date_circulation,'Kilometrage': vt.kilometrage, 'Cylindre': vt.cylindre}
  new_rowdf = pd.DataFrame([new_rows])
  df_v=v.transformer(new_rowdf)
  print(df_v.columns)
  print(df_v)
  