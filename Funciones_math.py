import math
import matplotlib.pyplot as plt
from Individuo import * 

def funcion1(num):
    return num**2

def funcion2(num):
    return abs((num-5)/(2+math.sin(num)))

def funcion3(num):
    return ((math.exp(num) - math.exp(-num)))


def graficar(poblacion):
    
     arreglo_y = [ind.aptitud for ind in poblacion]
     arreglo_x = [i for i in range(1,len(poblacion)+1)]

     plt.stem(arreglo_x, arreglo_y)
     plt.show()

