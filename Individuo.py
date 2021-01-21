from Funciones_math import *

class Individuo:

    def __init__(self, genotipo = [], fenotipo=0,aptitud = 0 ,apto_cruza = False, prob = 0.0):
        self.genotipo = genotipo
        self.fenotipo = fenotipo
        self.aptitud = aptitud
        self.apto_cruza = apto_cruza
        self.prob = prob


    def Generar_fenotipo(self):
        str_bin = "".join(map(str, self.genotipo))
        self.fenotipo = int(str_bin,2)

    def Generar_Aptitud(self, opc):
        if opc == 1:
            self.aptitud = round(funcion1(self.fenotipo),2)
        if opc == 2:
            self.aptitud = round(funcion2(self.fenotipo),2)
        if opc == 3:
            self.aptitud = round(funcion3(self.fenotipo),2)
        


        
