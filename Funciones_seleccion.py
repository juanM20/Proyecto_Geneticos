from Individuo import Individuo
from Funciones_math import *
import random
from numpy import math

def seleccion_1(poblacion):
    
    seleccion = []
    rango_prob = []
    sum = 0

    for ind in poblacion:
        sum = sum + ind.aptitud

    for ind in poblacion:
        ind.prob = ind.aptitud / sum

    rango_prob.append([0,poblacion[0].prob])
    rango_prob.append([poblacion[0].prob, poblacion[0].prob + poblacion[1].prob])

    
    for i in range(len(poblacion)):
        va = random.uniform(0,1)

        if va > rango_prob[i][0] and va < rango_prob[i][1]:
            poblacion[i].apto_cruza = True
            seleccion.append(poblacion[i])
        else:
            poblacion[i].apto_cruza = False
            seleccion.append(poblacion[i])


    return seleccion


def Seleccion_ruleta(poblacion):
    
    seleccion = []
    Valores_esperados = []
     
    aptitudes = [ind.aptitud for ind in poblacion]
    sumatoria = sum(aptitudes)
    f = sumatoria / len(poblacion)
    
    for ind in poblacion:
        ind.prob = ind.aptitud / f
        Valores_esperados.append(ind.aptitud / f) 
    
    T = sum(Valores_esperados)

    while len(seleccion) < len(poblacion):
        r = random.uniform(0, T)
        suma = 0 
        for ind in poblacion:
            suma = suma + ind.prob
            if suma >= r:
                ind.apto_cruza = True
                seleccion.append(ind)
                break

    return seleccion


def Seleccion_SobranteEstocastico_sinReemplazo(poblacion):
    
    seleccion = []
    Valores_esperados = []
    
    aptitudes = [ind.aptitud for ind in poblacion]
    sumatoria = sum(aptitudes)
    f = sumatoria / len(poblacion)
    
    for ind in poblacion:
        ind.prob = ind.aptitud / f
        Valores_esperados.append(ind.aptitud / f) 
    
    enteros = []
    
    for i in range(len(Valores_esperados)):
        dec, entero = math.modf(Valores_esperados[i])
        enteros.append(entero)

    dif = []
    
    for i in range(len(Valores_esperados)):
        dif.append(Valores_esperados[i]-enteros[i])

    i=0
    while(len(seleccion) < len(poblacion)):
        
        if(random.randint(0,1) == 1):
            poblacion[i].apto_cruza = True
            seleccion.append(poblacion[i])
  
        if(i < len(poblacion)-1):
            i = i + 1
        else:
            i = 0
            
    return seleccion
    
    
def Seleccion_SobranteEstocastico_conReemplazo(poblacion):
    
    
    seleccion = []
    Valores_esperados = []
    
    aptitudes = [ind.aptitud for ind in poblacion]
    sumatoria = sum(aptitudes)
    f = sumatoria / len(poblacion)
    
    for ind in poblacion:
        ind.prob = ind.aptitud / f
        Valores_esperados.append(ind.aptitud / f) 
    
    enteros = []
    
    for i in range(len(Valores_esperados)):
        dec, entero = math.modf(Valores_esperados[i])
        enteros.append(entero)

    dif = []
    
    for i in range(len(Valores_esperados)):
        dif.append(Valores_esperados[i]-enteros[i])
        poblacion[i].prob = Valores_esperados[i]-enteros[i]
        
    prob = []
    T = sum(dif)
    for i in range(len(dif)):
        prob.append(dif[i]/T)
    
    while len(seleccion) < len(poblacion):
        r = random.uniform(0, T)
        suma = 0 
        for ind in poblacion:
            suma = suma + ind.prob
            if suma >= r:
                ind.apto_cruza = True
                seleccion.append(ind)
                break

    return seleccion



def Seleccion_Torneo(poblacion):
    
    seleccion = []
    
    for i in range(len(poblacion)):
        
        contrincante_1 = random.randint(0, len(poblacion)-1)
        contrincante_2 = random.randint(0, len(poblacion)-1)
        
        if poblacion[contrincante_1].aptitud > poblacion[contrincante_2].aptitud:
            
            seleccion.append(poblacion[contrincante_1])
        else:
            seleccion.append(poblacion[contrincante_2])
            
    
    return seleccion
        