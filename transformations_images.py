import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import os
from skimage.io import imread,imshow
from skimage.color import rgb2gray
from matplotlib import pyplot as plt
from skimage.transform import resize
class TransformationImageVoiture(BaseEstimator, TransformerMixin):
    def __init__(self):
       pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, size=100*200):
       images = np.zeros((len(X),100*200))
       i=0
       for path in X:   
        I = imread(path)
        gray_image = rgb2gray(I)
        #plt.imshow(I)
        I1 = resize(gray_image, (100,200))
        plt.imshow(I1, cmap='gray') 
        I1=I1.flatten().reshape(1, -1)
        print(I1.shape) 
        #images.append(I1)
        # Ajouter le vecteur à la matrice
        images[i,:] = I1
        i=i+1
       return images
if __name__ == '__main__':
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
