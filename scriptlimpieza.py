import pandas as pd
import numpy as np
import csv

fichero = 'oficialesprueba.csv'
results = []

with open(fichero) as csvfile:
    reader = csv.reader(csvfile) 
    for lista in reader: # Cada fila es una lista
        results.append(lista[0])



df = pd.DataFrame({'email':results })


print("-------------------------------------------------------------------")
print("-----Data Frame con los datos del csv------------------------------")
print("-------------------------------------------------------------------")
print(df)


df["email"]=df["email"].str.replace("@mail.ejercito.mil.ar","", regex=True)


print("-------------------------------------------------------------------")
print("-----Corto el dominio, para poder limpiar los usuarios-------------")
print("-------------------------------------------------------------------")
print(df)

#r"\W" = con esta expresion regular, todo lo que no sea un numero o una letra se elimina

discard = [r"\W","á","é","í","ó","ú"," ","ñ"]
df=df[~df.email.str.contains('|'.join(discard))]

print("--------------------------------------------------------------------")
print("-----Limpio los usuarios--------------------------------------------")
print("--------------------------------------------------------------------")
print(df)

df['email']= df['email'].apply(lambda x: x.lower() + '@mail.ejercito.mil.ar') 

print("--------------------------------------------------------------------")
print("Coloco nuevamente el dominio a los usuarios y exporto todo en un csv")
print("--------------------------------------------------------------------")
print(df)

df.to_csv("correoslimpios.csv", index=False)