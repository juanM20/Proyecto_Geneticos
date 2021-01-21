from Individuo import Individuo
import random
from numpy import random
import numpy as np

def mutacion_desplazamiento(individuo):
    random.shuffle(individuo.genotipo)
    individuo.Generar_fenotipo()

def CMintercambio(p1):
    x = random.randint(0, (len(p1.genotipo)-1))
    y = random.randint(0, (len(p1.genotipo)-1))
    mp1 = [] 
    while x == y:
        x = random.randint(0, (len(p1.genotipo)-1))
        y = random.randint(0, (len(p1.genotipo)-1))
    else:
        a = p1.genotipo[x]
        b = p1.genotipo[y]
        p1.genotipo[y] = a
        p1.genotipo[x] = b
    
    p1.Generar_fenotipo()

def mutacion_IR(ind1): #Mutacion por intercambio reciproco
    while True:
        inicio = random.randint(0, len(ind1.genotipo) - 1)
        fin = random.randint(0, len(ind1.genotipo) - 1)
        if (inicio!=fin):
            break
    
    aux = ind1.genotipo[inicio]
    ind1.genotipo[inicio] = ind1.genotipo[fin]
    ind1.genotipo[fin] = aux

    ind1.Generar_fenotipo()

def mutacionInsercion(ind1):
    while True:
        inicio = random.randint(0, len(ind1.genotipo) - 1)
        fin = random.randint(0, len(ind1.genotipo) - 1)
        if (inicio!=fin):
            break
    diferencia = max(inicio, fin) - min(inicio, fin)
    if(inicio < fin):
        if(diferencia == 1):
            aux = ind1.genotipo[inicio]
            ind1.genotipo[inicio] = ind1.genotipo[fin]
            ind1.genotipo[fin] = aux
        else:
            aux = ind1.genotipo[inicio]
            for i in range(inicio, fin-1):
                ind1.genotipo[i] = ind1.genotipo[i+1]
            ind1.genotipo[fin] = aux
    else:
        if(diferencia == 1):
            aux = ind1.genotipo[inicio]
            ind1.genotipo[inicio] = ind1.genotipo[fin]
            ind1.genotipo[fin] = aux
        else:
            aux = ind1.genotipo[inicio]
            for i in range(inicio, fin, -1):
                ind1.genotipo[i] = ind1.genotipo[i-1]
            ind1.genotipo[fin] = aux

    ind1.Generar_fenotipo()

def L3_(v1, p1, p2, p3, unos):
	i = 0
	j = 0
	k = 0
	if(unos==1):
		i = 1
		j = 0
		k = 0
	elif(unos==2):
		i = 1
		j = 1
		k = 0

	if(p1 < p2 < p3): #0<1<2   1 0 0
		v1[p1]=i
		v1[p2]=j
		v1[p3]=k
	if(p2 < p1 < p3): #0<1<2   0 1 0
		v1[p2]=i
		v1[p1]=j
		v1[p3]=k
	if(p2 < p3 < p1):
		v1[p2]=i
		v1[p3]=j
		v1[p1]=k
	if(p3 < p2 < p1):
		v1[p3]=i
		v1[p2]=j
		v1[p1]=k
	if(p1 < p3 < p2):
		v1[p1]=i
		v1[p3]=j
		v1[p2]=k
	if(p3 < p1 < p2):
		v1[p3]=i
		v1[p1]=j
		v1[p2]=k
	return v1

def L4_(v1, p1, p2, p3, p4, unos):
	i = 0
	j = 0
	k = 0
	l = 0
	if(unos==1):
		i = 1
		j = 0
		k = 0
		l = 0
	elif(unos==2):
		i = 1
		j = 1
		k = 0
		l = 0
	elif(unos==3):
		i = 1
		j = 1
		k = 1
		l = 0

	if(p1 < p2 < p3 < p4):
		v1[p1]=i
		v1[p2]=j
		v1[p3]=k
		v1[p4]=l
	if(p1 < p2 < p4 < p3):
		v1[p1]=i
		v1[p2]=j
		v1[p4]=k
		v1[p3]=l
	if(p1 < p3 < p2 < p4):
		v1[p1]=i
		v1[p3]=j
		v1[p2]=k
		v1[p4]=l
	if(p1 < p3 < p4 < p2):
		v1[p1]=i
		v1[p3]=j
		v1[p4]=k
		v1[p2]=l
	if(p1 < p4 < p2 < p3):
		v1[p1]=i
		v1[p4]=j
		v1[p2]=k
		v1[p3]=l
	if(p1 < p4 < p3 < p2):
		v1[p1]=i
		v1[p4]=j
		v1[p3]=k
		v1[p2]=l

	if(p2 < p1 < p3 < p4):
		v1[p2]=i
		v1[p1]=j
		v1[p3]=k
		v1[p4]=l
	if(p2 < p1 < p4 < p3):
		v1[p2]=i
		v1[p1]=j
		v1[p4]=k
		v1[p3]=l
	if(p2 < p3 < p1 < p4):
		v1[p2]=i
		v1[p3]=j
		v1[p1]=k
		v1[p4]=l
	if(p2 < p3 < p4 < p1):
		v1[p2]=i
		v1[p3]=j
		v1[p4]=k
		v1[p1]=l
	if(p2 < p4 < p1 < p3):
		v1[p2]=i
		v1[p4]=j
		v1[p1]=k
		v1[p3]=l
	if(p2 < p4 < p3 < p1):
		v1[p2]=i
		v1[p4]=j
		v1[p3]=k
		v1[p1]=l

	if(p3 < p1 < p2 < p4):
		v1[p3]=i
		v1[p1]=j
		v1[p2]=k
		v1[p4]=l
	if(p3 < p1 < p4 < p2):
		v1[p3]=i
		v1[p1]=j
		v1[p4]=k
		v1[p2]=l
	if(p3 < p2 < p1 < p4):
		v1[p3]=i
		v1[p2]=j
		v1[p1]=k
		v1[p4]=l
	if(p3 < p2 < p4 < p1):
		v1[p3]=i
		v1[p2]=j
		v1[p4]=k
		v1[p1]=l
	if(p3 < p4 < p1 < p2):
		v1[p3]=i
		v1[p4]=j
		v1[p1]=k
		v1[p2]=l
	if(p3 < p4 < p2 < p1):
		v1[p3]=i
		v1[p4]=j
		v1[p2]=k
		v1[p1]=l

	if(p4 < p1 < p2 < p3):
		v1[p4]=i
		v1[p1]=j
		v1[p2]=k
		v1[p3]=l
	if(p4 < p1 < p3 < p2):
		v1[p4]=i
		v1[p1]=j
		v1[p3]=k
		v1[p2]=l
	if(p4 < p2 < p1 < p3):
		v1[p4]=i
		v1[p2]=j
		v1[p1]=k
		v1[p3]=l
	if(p4 < p2 < p3 < p1):
		v1[p4]=i
		v1[p2]=j
		v1[p3]=k
		v1[p1]=l
	if(p4 < p3 < p1 < p2):
		v1[p4]=i
		v1[p3]=j
		v1[p1]=k
		v1[p2]=l
	if(p4 < p3 < p2 < p1):
		v1[p4]=i
		v1[p3]=j
		v1[p2]=k
		v1[p1]=l
	return v1

#comb = permutations(v1, len(v1)) 
#for i in comb:
#print(i)
def mutacion_heuristica(v1):
	v1 = np.array([0, 0, 0, 1, 1, 0])
	L = random.randint(5) #Lambda=Numero de alhelos a cambiar de lugar
	if(L==0): #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		print("No hay mutacion: ")
		print("Sin cambios: ", v1)
	elif(L==1): #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		print("No hay mutacion: ")
		print("Sin cambios: ", v1)
	elif(L==2): #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		while True:
			p1 = random.randint(len(v1))
			p2 = random.randint(len(v1))
			if (p1!=p2):
				break
		print("Antes: ", v1)
		print("Punto 1: ", p1)
		print("Punto 2: ", p2)

		if(v1[p1]==0 and v1[p2]==0): #00
			print("Despues: ", v1)
		elif(v1[p1]==1 and v1[p2]==1): #11
			print("Despues: ", v1)
		elif((v1[p1]==1 and v1[p2]==0) or (v1[p1]==0 and v1[p2]==1)): #10
			if(p1 < p2):
				v1[p1] = 1
				v1[p2] = 0
			elif(p2 < p1):
				v1[p2] = 1
				v1[p1] = 0
			print("Despues: ", v1)
	elif(L==3): #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		while True:
			p1 = random.randint(len(v1))
			p2 = random.randint(len(v1))
			p3 = random.randint(len(v1))
			if ((p1!=p2) and (p1!=p3) and (p2!=p3)):
				break
		print("Antes: ", v1)
		print("Punto 1: ", p1)
		print("Punto 2: ", p2)
		print("Punto 3: ", p3)
	 
		if(v1[p1]==0 and v1[p2]==0 and v1[p3]==0): #000
			print("Despues: ", v1)
		elif(v1[p1]==1 and v1[p2]==1 and v1[p3]==1): #111
			print("Despues: ", v1)
		elif((v1[p1]==1 and v1[p2]==0 and v1[p3]==0) or \
			(v1[p1]==0 and v1[p2]==1 and v1[p3]==0) or \
			(v1[p1]==0 and v1[p2]==0 and v1[p3]==1)): #100
			v1 = L3_(v1, p1, p2, p3, 1)
			print("Despues: ", v1)
		elif((v1[p1]==1 and v1[p2]==1 and v1[p3]==0) or \
			(v1[p1]==1 and v1[p2]==0 and v1[p3]==1) or \
			(v1[p1]==0 and v1[p2]==1 and v1[p3]==1)): #110
			v1 = L3_(v1, p1, p2, p3, 2)
			print("Despues: ", v1)

	elif(L==4): #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		while True:
			p1 = random.randint(len(v1))
			p2 = random.randint(len(v1))
			p3 = random.randint(len(v1))
			p4 = random.randint(len(v1))
			if ((p1!=p2) and (p1!=p3) and (p1!=p4) and (p2!=p3) and (p2!=p4) and (p3!=p4)):
				break
		print("Antes: ", v1)
		print("Punto 1: ", p1)
		print("Punto 2: ", p2)
		print("Punto 3: ", p3)
		print("Punto 4: ", p4)
	 
		if(v1[p1]==0 and v1[p2]==0 and v1[p3]==0 and v1[p4]==0): #0000
			print("Despues: ", v1)
		elif(v1[p1]==1 and v1[p2]==1 and v1[p3]==1 and v1[p4]==1): #1111
			print("Despues: ", v1)
		elif((v1[p1]==1 and v1[p2]==0 and v1[p3]==0 and v1[p4]==0) or \
			(v1[p1]==0 and v1[p2]==1 and v1[p3]==0 and v1[p4]==0) or \
			(v1[p1]==0 and v1[p2]==0 and v1[p3]==1 and v1[p4]==0) or \
			(v1[p1]==0 and v1[p2]==0 and v1[p3]==0 and v1[p4]==1)): #1000
			v1 = L4_(v1, p1, p2, p3, p4, 1)
			print("Despues: ", v1)
		elif((v1[p1]==1 and v1[p2]==1 and v1[p3]==0 and v1[p4]==0) or \
			(v1[p1]==1 and v1[p2]==0 and v1[p3]==1 and v1[p4]==0) or \
			(v1[p1]==1 and v1[p2]==0 and v1[p3]==0 and v1[p4]==1) or \
			(v1[p1]==0 and v1[p2]==1 and v1[p3]==1 and v1[p4]==0) or \
			(v1[p1]==0 and v1[p2]==1 and v1[p3]==0 and v1[p4]==1) or \
			(v1[p1]==0 and v1[p2]==0 and v1[p3]==1 and v1[p4]==1)): #1100
			v1 = L4_(v1, p1, p2, p3, p4, 2)
			print("Despues: ", v1)
		elif((v1[p1]==1 and v1[p2]==1 and v1[p3]==1 and v1[p4]==0) or \
			(v1[p1]==1 and v1[p2]==1 and v1[p3]==0 and v1[p4]==1) or \
			(v1[p1]==1 and v1[p2]==0 and v1[p3]==1 and v1[p4]==1) or \
			(v1[p1]==0 and v1[p2]==1 and v1[p3]==1 and v1[p4]==1)): #1110
			v1 = L4_(v1, p1, p2, p3, p4, 3)
			print("Despues: ", v1)
