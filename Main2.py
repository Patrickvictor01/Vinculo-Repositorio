#Calcular IMC com Numpy
import numpy as np

altura = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
peso = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

#Criando Array na lista
np_altura = np.array(altura)
np_peso = np.array(peso)

#Cálculo IMC
IMC = np_altura/np_peso **2
print(IMC)


