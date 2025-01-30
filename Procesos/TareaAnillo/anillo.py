"""
Este es un ejemplo de uso de MPI4PY para el anillo.
Cuenta: ppd_lcc_24
Directorio: [ppd_lcc_24@login MPI]$
"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if size < 2:
    print("Se requieren al menos dos procesos.")
    exit()

mensaje = f"Hola, soy el proceso {rank}, un saludo desde {rank - 1 if rank > 0 else size - 1}"

comm.send(mensaje, dest=(rank + 1)% size, tag=9)

mensaje_recibido = comm.recv(source=(rank - 1) % size, tag=9)
print(f"Soy el proceso {rank}, recibí el mensaje => {mensaje_recibido}")

