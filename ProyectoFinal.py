import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import ExcelWriter
from pandas import ExcelFile

def obtenerGenero(partido, estado, sexo):
    lista = []
    totalMujeres = 0
    totalHombres = 0

    for i in range(len(sexo)):
        if partido[i] == "PRI" and estado[i] == "Distrito Federal":
            if sexo[i] == "Mujer":
                totalMujeres += 1
            else:
                totalHombres += 1
    
    lista.append(totalMujeres)
    lista.append(totalHombres)
    return lista

db2000 = pd.read_excel("Base-Candidatas-Cámara-de-Diputados.xlsx", 
                    sheet_name="Candidatos_DIP_MR_RP_2000", 
                    usecols=["Sexo", "Partido Político", "Entidad Federativa", "Distrito Electoral"])

db2003 = pd.read_excel("Base-Candidatas-Cámara-de-Diputados.xlsx", 
                    sheet_name="Candidatos_DIP_MR_RP_2003", 
                    usecols=["Sexo", "Partido Político", "Entidad Federativa", "Distrito Electoral"])

db2006 = pd.read_excel("Base-Candidatas-Cámara-de-Diputados.xlsx", 
                    sheet_name="Candidatos_DIP_MR_RP_2006", 
                    usecols=["Sexo", "Partido Político", "Entidad Federativa", "Distrito Electoral"])

db2009 = pd.read_excel("Base-Candidatas-Cámara-de-Diputados.xlsx", 
                    sheet_name="Candidatos_DIP_MR_RP_2009", 
                    usecols=["Sexo", "Partido Político", "Entidad Federativa", "Distrito Electoral"])

db2012 = pd.read_excel("Base-Candidatas-Cámara-de-Diputados.xlsx", 
                    sheet_name="Candidatos_DIP_MR_RP_2012", 
                    usecols=["Sexo", "Partido Político", "Entidad Federativa", "Distrito Electoral"])

db2015 = pd.read_excel("Base-Candidatas-Cámara-de-Diputados.xlsx", 
                    sheet_name="Candidatos_DIP_MR_RP_2015", 
                    usecols=["Sexo", "Partido Político", "Entidad Federativa", "Distrito Electoral"])                    

listaX = ["Mujeres", "Hombres"]
genero2000 = obtenerGenero(db2000["Partido Político"], db2000["Entidad Federativa"], db2000["Sexo"])
genero2003 = obtenerGenero(db2003["Partido Político"], db2003["Entidad Federativa"], db2003["Sexo"])
genero2006 = obtenerGenero(db2006["Partido Político"], db2006["Entidad Federativa"], db2006["Sexo"])
genero2009 = obtenerGenero(db2009["Partido Político"], db2009["Entidad Federativa"], db2009["Sexo"])
genero2012 = obtenerGenero(db2012["Partido Político"], db2012["Entidad Federativa"], db2012["Sexo"])
genero2015 = obtenerGenero(db2015["Partido Político"], db2015["Entidad Federativa"], db2015["Sexo"])

plt.subplot(231)
plt.bar(listaX, genero2000)
plt.title("Cantidad de personas en el PRI en el Distrito Federal del 2000")
plt.xlabel("Sexo")
plt.ylabel("#Número de personas")

plt.subplot(232)
plt.bar(listaX, genero2003)
plt.title("Cantidad de personas en el PRI en el Distrito Federal del 2003")
plt.xlabel("Sexo")
plt.ylabel("#Número de personas")

plt.subplot(233)
plt.bar(listaX, genero2006)
plt.title("Cantidad de personas en el PRI en el Distrito Federal del 2006")
plt.xlabel("Sexo")
plt.ylabel("#Número de personas")

plt.subplot(234)
plt.bar(listaX, genero2009)
plt.title("Cantidad de personas en el PRI en el Distrito Federal del 2009")
plt.xlabel("Sexo")
plt.ylabel("#Número de personas")

plt.subplot(235)
plt.bar(listaX, genero2012)
plt.title("Cantidad de personas en el PRI en el Distrito Federal del 2012")
plt.xlabel("Sexo")
plt.ylabel("#Número de personas")

plt.subplot(236)
plt.bar(listaX, genero2015)
plt.title("Cantidad de personas en el PRI en el Distrito Federal del 2015")
plt.xlabel("Sexo")
plt.ylabel("#Número de personas")

plt.show()