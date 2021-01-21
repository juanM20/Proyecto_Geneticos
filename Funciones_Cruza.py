from Individuo import Individuo
import random

def Cpunto(p1,p2):
    
    x = random.randint(1, (len(p1)-1))
    h1 = [] 
    h2 = []
    for i in range(x):
        h1.append(p1[i]) 
        h2.append(p2[i])
    for n in range(x,len(p2)): 
        h1.append(p2[n])
        h2.append(p1[n])
    return h1, h2

def cxTwoPoint(ind1, ind2):
    while True:
        cxpoint = random.randint(1, len(ind1.genotipo) - 1)
        cxpoint2 = random.randint(1, len(ind2.genotipo) - 1)
        if (cxpoint!=cxpoint2):
            break
    ind1.genotipo[cxpoint:], ind2.genotipo[cxpoint:] = ind2.genotipo[cxpoint:].copy(), ind1.genotipo[cxpoint:].copy()
    ind1.genotipo[cxpoint2:], ind2.genotipo[cxpoint2:] = ind2.genotipo[cxpoint2:].copy(), ind1.genotipo[cxpoint2:].copy()
    return ind1, ind2

def CUniforme(p1,p2):
    mascara = bin(random.randint(1, (len(p1.genotipo))/2 - 1)) 
    h1 = []
    h2 = []
    for i in range(len(mascara)):
        if mascara[i] == 1:
            h1.append(p1[i])
            h2.append(p2[i])
        else:
            h1.append(p2[i])
            h2.append(p1[i])

    return  h1, h2


def Cruza_dosPuntos(poblacion):
    
    Hijos = []
    random.shuffle(poblacion)

    for i in range(len(poblacion)):
        if i%2 == 0:
            hijo1 = Individuo()
            hijo2 = Individuo()
            hijo1.genotipo, hijo2.genotipo = cxTwoPoint(poblacion[i-1].genotipo, poblacion[i].genotipo)
            hijo1.Generar_fenotipo()
            hijo2.Generar_fenotipo()
            
            Hijos.append(hijo1)
            Hijos.append(hijo2)

    return Hijos



def Cruza_Punto(poblacion):
        
    Hijos = []
    random.shuffle(poblacion)

    for i in range(len(poblacion)):
        if i%2 == 0:
            hijo1 = Individuo()
            hijo2 = Individuo()
            hijo1.genotipo, hijo2.genotipo = Cpunto(poblacion[i-1].genotipo, poblacion[i].genotipo)
            hijo1.Generar_fenotipo()
            hijo2.Generar_fenotipo()
           
            Hijos.append(hijo1)
            Hijos.append(hijo2)

    return Hijos


def Cruza_Uniforme(poblacion):
        
    Hijos = []
    random.shuffle(poblacion)

    for i in range(len(poblacion)):
        if i%2 == 0:
            hijo1 = Individuo()
            hijo2 = Individuo()
            hijo1.genotipo, hijo2.genotipo = Cpunto(poblacion[i-1].genotipo, poblacion[i].genotipo)
            hijo1.Generar_fenotipo()
            hijo2.Generar_fenotipo()
            
            Hijos.append(hijo1)
            Hijos.append(hijo2)

    return Hijos