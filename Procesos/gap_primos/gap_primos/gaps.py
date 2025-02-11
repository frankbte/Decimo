from mpi4py import MPI
import sys
import math
from sortValues import BLOCK_LOW,BLOCK_HIGH,BLOCK_SIZE
from numFunctions import get_gaps,get_primes

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    root = 0

    # Obtener el valor de n desde la línea de comandos
    if rank == root:
        if len(sys.argv) != 2:
            print("Uso: mpiexec -n <num_procesos> python3 script.py <n>")
            sys.exit(1)
        n = int(sys.argv[1])
    else:
        n = None

    # Broadcast el valor de n a todos los procesos
    n = comm.bcast(n, root=root)

    # Dividir el rango de números entre los procesos
    inicio = BLOCK_LOW(rank, size, n) + 1
    fin = BLOCK_HIGH(rank, size, n) + 1

    # Distribuir las listas a cada proceso
    local_numbers = [i for i in range(inicio, fin + 1)]

    # Obtener los números primos locales
    local_primes = get_primes(local_numbers)

    # Inicializar max_diff
    max_diff = 0

    if rank == root:
        if local_primes:  # Verificar si local_primes no está vacío
            #Mandar el ultimo primo al siguiente proceso
            comm.send(local_primes[-1], dest=rank + 1, tag=11)
            #Mandar la lista de primos al root
            comm.send(local_primes[:-1],dest=root,tag=11)

        local_twin_primes_num, max_local_gaps, max_diff = get_gaps(local_primes)
        comm.send(max_local_gaps,dest=root, tag=12)

    if rank != root and rank != size - 1:
        mensaje = comm.recv(source=rank - 1, tag=11)
        local_primes.insert(0, mensaje)
        if local_primes:  # Verificar si local_primes no está vacío
            #Mandar el ultimo primo al siguiente proceso
            comm.send(local_primes[-1], dest=rank + 1, tag=11)
            #Mandar la lista de primos menos el ultimo al root (para evitar repetidos)
            comm.send(local_primes[:-1],dest=root,tag=11)
        #Obtener los gaps, el numero de primos
        local_twin_primes_num, max_local_gaps, max_diff = get_gaps(local_primes)
        comm.send(max_local_gaps,dest=root, tag=12)


    elif rank == size - 1:
        mensaje = comm.recv(source=rank - 1, tag=11)
        local_primes.insert(0, mensaje)

        #Mandar la lista de primos al root
        comm.send(local_primes,dest=root,tag=11)
        local_twin_primes_num, max_local_gaps, max_diff = get_gaps(local_primes)
        comm.send(max_local_gaps,dest=root, tag=12)


    # Usar MPI.MAX y MPI.SUM para encontrar el gap máximo global y el numero de primos gemelos
    max_global_gap = comm.reduce(max_diff, op=MPI.MAX, root=root)
    global_twin_primes_num = comm.reduce(local_twin_primes_num, op=MPI.SUM, root=root)

    if rank == root:
        all_primes = []
        keys=[]
        #Reciviendo 
        for message in range(size):
            rank_primes = comm.recv(source=message, tag=11)
            keys.append(comm.recv(source=message, tag=12)) #Recibir los gaps maximos locales y añadirlas a la lista total 
            all_primes.extend(rank_primes) #Recibir lista de primos y añadirlas a la lista total 
        all_primes = sorted(list(set(all_primes)))
        
        #Sacar los primos donde hubo el gap maximo
        max_prime_gap = []
        for dic in keys:
            if max_global_gap in dic:
                max_prime_gap.append(dic[max_global_gap])
        
        print("---------------------------------------------------------")
        print(f"El numero total de primos es: {len(all_primes)}")
        print(f"La lista total de primos es: {all_primes}")
        print("---------------------------------------------------------")
        print(f"El gap máximo entre todos los procesos fue: {max_global_gap}, entre los primos {max_prime_gap}")
        print("---------------------------------------------------------")
        print(f"El numero total de numeros primos gemelos es: {global_twin_primes_num}")
        print("---------------------------------------------------------")


if __name__ == "__main__":
    main()