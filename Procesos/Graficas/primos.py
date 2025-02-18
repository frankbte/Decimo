import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

num_Procs = 10
tiempo_secuencial = 0.00015377998352050784
tiempo_ideal = np.zeros(num_Procs)

for i in range(num_Procs):
    tiempo_ideal[i] = tiempo_secuencial / (i + 1)

df1 = pd.read_csv("tiempos_par_py.dat", sep=",")

plt.plot(1, tiempo_secuencial, color='r',marker='*',markersize=20)
plt.text(1.5, tiempo_secuencial,'<--- secuencial',color='r')

plt.plot(df1['np'], df1['tiempo'],color='k',marker='.',label='V1',linestyle='dashed')

plt.xlabel("Número de procesos")
plt.ylabel("Tiempo (segs)")
plt.legend()
plt.title("Contar el número de primos menores a 5000 en COLAB")
plt.show()