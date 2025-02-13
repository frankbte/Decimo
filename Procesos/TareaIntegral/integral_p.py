from mpi4py import MPI
import numpy as np
import sys
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def f(x):
    """ Función a integrar: f(x) = x^2 """
    return x * x

def calcular_integral_parcial(a, b, n):
    """ Calcula la parte de la integral correspondiente a cada proceso """
    dx = (b - a) / n
    suma_local = 0.0
    local_n = n // size  # Número de subintervalos
    local_a = a + rank * local_n * dx  # Límite inferior para este proceso

    for i in range(local_n):
        suma_local += f(local_a + i * dx) * dx

    return suma_local

if __name__ == "__main__":
    if len(sys.argv) != 4:
        if rank == 0:
            print("Uso: python integral_mpi.py a b n")
        sys.exit()

    a = float(sys.argv[1])
    b = float(sys.argv[2])
    n = int(sys.argv[3])

    if n <= 0 or a > b:
        if rank == 0:
            print("ERROR: Los límites del intervalo o el número de particiones es incorrecto")
        sys.exit()

    comm.Barrier()  # Sincronizar todos los procesos antes de empezar a medir el tiempo
    start_time = time.time()

    # Calcular la integral parcial
    integral_local = calcular_integral_parcial(a, b, n)

    # Recolectar los resultados parciales en el proceso raíz
    integral_total = comm.reduce(integral_local, op=MPI.SUM, root=0)

    comm.Barrier()  # Sincronizar todos los procesos antes de medir el tiempo final
    end_time = time.time()

    # Mostrar resultados en el proceso raíz
    if rank == 0:
        tiempo_total = end_time - start_time
        
        # Imprimir resultados en formato de tabla
        print(f"{'Número de procesos':<20}{'Valor total de la integral':<30}{'Tiempo de ejecución (s)':<25}")
        print(f"{size:<20}{integral_total:<30.6f}{tiempo_total:<25.6f}")
