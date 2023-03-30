import nltk
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer
import os
import pandas as pd
class TransformationVoitureTexte (BaseEstimator, TransformerMixin):
  
    
    
    def __init__(self, language='french'):
        
        
        
        self.stopwords = set(stopwords.words(language))
        self.cv = CountVectorizer()
        
    
    
    
    def fit(self, X, y=None):
        def segmenter(document):
         tokens = nltk.word_tokenize(document.lower())
         return [token for token in tokens if token not in self.stopwords and token.isalpha()]
        self.cv = CountVectorizer(tokenizer=segmenter)
        self.cv.fit(X)
    
    
    def transform(self, X, y=None):
        res=self.cv.transform(X)
        print(res.toarray())
        return res
    
    def getPaths(self):
        dir_path = os.getcwd()
        data_path=dir_path+'\\Desc_voiture'
        nameslist = os.listdir(data_path)
        Paths=[]
        for name in nameslist:      
               text_path = os.path.join(data_path, name) 
               Paths.append(text_path)
        return Paths

    def getCorpus(self,Paths):
          Paths=self.getPaths()

          Corpus = []
          for path in Paths:
               file = open(path, 'r',encoding='utf-8')
               text = file.read()
               text=text.lower()
               file.close()
               Corpus.append(text)
          df = pd.DataFrame({'paths': Paths, 'Corpus': Corpus})
          return df

if __name__ == '__main__':

    transformer = TransformationVoitureTexte()

    dir_path = os.getcwd()
    data_path=dir_path+'\\Desc_voiture'
    nameslist = os.listdir(data_path)
    Paths=[]
    for name in nameslist:      
      text_path = os.path.join(data_path, name) 
      Paths.append(text_path)

    Corpus = []
    for path in Paths:
        file = open(path, 'r',encoding='utf-8')
        text = file.read()
        text=text.lower()
        file.close()
        Corpus.append(text)
    transformer.fit(Corpus)
    X=transformer.transform(Corpus)
    print(X.toarray())
