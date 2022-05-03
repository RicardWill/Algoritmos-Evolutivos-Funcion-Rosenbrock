import numpy as np
import random as rnd
import math as mt


# Generar poblacion con seis genes
# Generate population with six genes

def generarPoblacion(m, n):
    poblacion = np.zeros((m, n))
    
    # Rosenbrock function optimization by adaptive coordinate descent from starting point -1.5 , +3
    
    for i in range(m):
        for j in range(n):
            poblacion[i][j] = rnd.uniform(-1.5, 3)
            # x = -1.5+rnd.random()*4.5

    print("Poblacion inicial // Initial population \n", poblacion)
    return poblacion


# Fitness Calculo
# Definición es la métrica que nos indica cómo de ajustado a la solución óptima está un individuo de la población.

# Fitness Calculation
# Definition is the metric that tells us how adjusted an individual in the population is to the optimal solution.

def calcularFitness(poblacion):
    fitness = np.zeros(len(poblacion))

    for i in range(len(poblacion)):
        suma = 0
        for j in range(len(poblacion) - 1):
        
            #Uso de la funcion de rosenbrock para hallar la solucion mas optima posible
            #Using Rosenbrock's function to find the best possible solution
            #Watch this url: https://wikimedia.org/api/rest_v1/media/math/render/svg/4793c1eb9633dd26a5b848f5b4c794cba19ccb18
            
            suma += mt.pow((1 - poblacion[i][j]), 2) + 100 * mt.pow((poblacion[i][j + 1] - mt.pow(poblacion[i][j], 2)),
                                                                    2)

        fitness[i] = suma

    print("Valor del fitness // Fitness Value \n", fitness)
    return fitness


def seleccionTorneo(poblacion, fitness):
    pobSeleccionada = np.zeros((len(poblacion), len(poblacion)))
    ind1, ind2 = 0, 0

    for i in range(len(poblacion)):
        ind1, ind2 = 0, 0
        while (ind1 == ind2):
            ind1 = rnd.randint(0, 5)
            ind2 = rnd.randint(0, 5)

        if (fitness[ind1] <= fitness[ind2]):
            pobSeleccionada[i][:] = poblacion[ind1][:]
        else:
            pobSeleccionada[i][:] = poblacion[ind2][:]

    print("Poblacion seleccionada // Selected population \n", pobSeleccionada)
    return pobSeleccionada


def cruza(poblacion):
    pobCruzada = np.zeros((len(poblacion), len(poblacion)))
    ptoCruza = 0
    index = 0
    #    int((len(poblacion)/2))

    for i in range(int((len(poblacion) / 2))):
        ind1, ind2 = 0, 0

        while (ind1 == ind2):
            ind1 = rnd.randint(0, 5)
            ind2 = rnd.randint(0, 5)

        ptoCruza = rnd.randint(0, 5)  # Punto de corte // Cut Point
        # Creación del primer hijo 
        # Create first child
        pobCruzada[index][0:ptoCruza] = poblacion[ind1][0:ptoCruza]
        pobCruzada[index][ptoCruza:6] = poblacion[ind2][ptoCruza:6]
        # Creación del segundo hijo
        # Create second child
        pobCruzada[index + 1][0:ptoCruza] = poblacion[ind2][0:ptoCruza]
        pobCruzada[index + 1][ptoCruza:6] = poblacion[ind1][ptoCruza:6]
        index += 2

    print("poblacion cruzada: // Cross population: \n", pobCruzada)
    return pobCruzada


def muta(poblacion):
    pobMutada = np.zeros((len(poblacion), len(poblacion)))
    #Existe una probabilidad que si se obtiene un valor menor al esperado el gen tiende a mutar
    #There is a probability that if a value lower than expected is obtained, the gene tends to mutate
    PrMuta = 0.1
    ptoMuta = 0

    for i in range(len(poblacion)):
        x = rnd.random()

        if (x < PrMuta):
            # El individuo se muta
            # Individual Changes
            ptoMuta = rnd.randint(0, 5)
            valor = rnd.uniform(-1.5, 3)
            pobMutada[i][:] = poblacion[i][:]
            pobMutada[i][ptoMuta] = valor
        else:
            # Storage without Change
            # Se almacena sin mutar
            pobMutada[i][:] = poblacion[i][:]

    print("Poblacion Mutada // Mutate population: \n", pobMutada)
    return pobMutada


# Seleccion de individuos
# Selection of individuals

def calcularNuevoFitness(poblacion):
    fitness = np.zeros(len(poblacion))

    for i in range(len(poblacion)):
        suma = 0
        for j in range(len(poblacion) - 1):
            suma += mt.pow((1 - poblacion[i][j]), 2) + 100 * mt.pow((poblacion[i][j + 1] - mt.pow(poblacion[i][j], 2)),
                                                                    2)

        fitness[i] = suma

    print("Nuevo Valor del Fitness // New Fitness Value: \n",fitness)
    return fitness


if __name__ == '__main__':
    poblacion = generarPoblacion(6, 6)
    i = 0
    #Numero de genes involucrados para probar la función 
    #Number of genes involved to test function
    nGen = 10
    while (i < nGen):
        fitness = calcularFitness(poblacion)
        poblacion_seleccionada = seleccionTorneo(poblacion, fitness)
        poblacion_cruzada = cruza(poblacion_seleccionada)
        poblacion_mutada = muta(poblacion_cruzada)

        #Nueva poblacion de la población mutada
        #New population of the mutated population
        calcularNuevoFitness(poblacion_mutada)
        i += 1