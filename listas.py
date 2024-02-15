import os
import pandas as pd
List1 = [8, 9, 3, 6, 1, 10]
List1.reverse()
print("The reversed list is", List1)

List2 = [91, 67, 120, 34, 76, 54, 78, 87, 56, 64, 345]
List2.sort()
print ("The sorted list is" , List2)

List3 = []
List3 = List1.copy()
print("List3 =", List3)

indexvalue = List2[2:6]
print("The index values are" , indexvalue)

df = pd.read_csv("./credit.csv")
print(df.head(5))

import requests
from bs4 import BeautifulSoup

# URL de la página web a la que queremos hacer scraping
url = 'https://elcomercio.pe/'

# Realizamos la solicitud GET a la página
response = requests.get(url)

# Verificamos si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parseamos el contenido HTML de la página utilizando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontramos todos los elementos <h2> que contienen los títulos de los artículos
    titles = soup.find_all('h2')
    
    # Iteramos sobre los elementos encontrados e imprimimos el texto de cada uno
    for title in titles:
        print(title.text)
else:
    print('La solicitud no fue exitosa. Código de estado:', response.status_code)

