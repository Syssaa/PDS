from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from agence import Agence
import pandas as pd
from io import BytesIO
import base64
from recherche import Recherche
from django.core.files.storage import FileSystemStorage
import os


def home(request):
     return render (request,'agences/accueil.html')

def listall(request):
     agence = Agence()
     agence.readAll()
     #return render (request,'hello')
    
     df = pd.DataFrame(agence.data)

     df['image_url'] = df['imagebase']
     df['Date_de_circulation']=df['Date de circulation']
     
     html = df.to_html()
     html_table = df.to_dict(orient='records')
     print(html_table)
     context = {'html_table': html_table,'df':df.size}
     
     return render (request,'agences/accueil.html', context)
     
def search(request):
    if request.method == 'POST':
        text_query = request.POST.get('text')
        image_query = request.FILES['file']

        
        r=Recherche()
        df = pd.DataFrame()
        if(text_query):
          res=r.RechercheText_VDB(text_query)
          df=res
        elif(image_query):
          
          directory = os.path.join(os.getcwd(), 'my_directory') # specify directory path here
          fs = FileSystemStorage(location=directory)
          filename = fs.save(image_query.name, image_query)
          path=os.path.join( directory,filename)
          path = path.replace("\\", "/")

          uploaded_file_url = fs.url(filename)

          res=r.RechercheImage_VDB(path)
          
          #res=r.RechercheText_VDB("test")
          df=res
          
        
        
        df['image_url'] = df['imagebase']
        df['Date_de_circulation']=df['Date de circulation']
        #print(df.columns)
        html_table = df.to_dict(orient='records')
        context = {'html_table': html_table,'df':df.size}
        
        return render (request,'agences/accueil.html', context)
    else:
          agence = Agence()
          agence.readAll()
          #return render (request,'hello')
     
          df = pd.DataFrame(agence.data)

          df['image_url'] = df['imagebase']
          df['Date_de_circulation']=df['Date de circulation']
          
          html = df.to_html()
          html_table = df.to_dict(orient='records')
         
          context = {'html_table': html_table,'df':df.size}
          
          
          return render (request,'agences/accueil.html', context)



     


