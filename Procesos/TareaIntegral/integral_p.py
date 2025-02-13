from mpi4py import MPI
import sys
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def f(x):
    return x*x

def calcular_integral(a,b,n):
    dx = (b-a)/n
    suma_local = 0.0
    x = a + rank * (n // size) * dx

    for i in range(rank * (n // size), (rank+1) * (n // size)):
        suma_local += f(x)
        x += dx

    return suma_local

if __name__ == '__main__':

    if len(sys.argv) != 4:
        if rank == 0:
            print("Uso: python integral_mpi.py a b n")
        sys.exit()

    a = float(sys.argv[1])
    b = float(sys.argv[2])
    n = int(sys.argv[3])

    integral_local = calcular_integral(a,b,n)

    integral_total = comm.reduce(integral_local, op=MPI.SUM, root=0)

    if rank == 0:
        print("Integral de f(x) entre {} y {} es {}".format(a,b,integral_total))



