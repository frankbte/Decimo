from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()  
size = comm.Get_size()  

numExperimentos = 5000
n = 5000
localExperimentos = numExperimentos // size  
mediaPi_local = 0

for i in range(localExperimentos):
    valor = 0
    X = np.random.uniform(0, 1, n)
    Y = np.random.uniform(0, 1, n)
    for j in range(n):
        Z = np.sqrt(X[j] * X[j] + Y[j] * Y[j])
        if Z <= 1:
            valor += 1

    valorAproxPi = valor * 4.0 / n
    mediaPi_local += valorAproxPi

mediaPi_global = comm.reduce(mediaPi_local, op=MPI.SUM, root=0)

if rank == 0:
    piFinal = mediaPi_global / numExperimentos
    print("Valor aproximado de PI = {0:.10f}".format(piFinal))
