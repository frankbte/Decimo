from mpi4py import MPI
import sys
import math

def EsPrimo(num):
  if(num==1):
    return 0
  if(num<=3):
    return 1;
  if(num%2==0 or num%3==0):
    return 0;
  i=5;
  while(i*i<=num):
    if(num%i==0 or num%(i+2)==0):
      return 0;
    i=i+6;
  return 1;

def es_primo( num ):
  ind = 1 # es primo mientras no se demuestre lo contrario

  for i in range(2, int(math.sqrt(num)) + 1 ):
    if( num % i == 0 ):
      ind = 0; # se encontró un divisor, es decir, no es primo
      break;

  return ind;

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

t1 = MPI.Wtime()

m = int(sys.argv[1])
inicio = math.floor((rank) * (m/size))
if rank==0:
  inicio = 2

fin = math.floor((rank+1) * (m/size))

numPrimos = 0

for x in range (inicio, fin):
  if EsPrimo(x) == 1:
    numPrimos = numPrimos + 1

if ( rank != 0 ):
  comm.send( numPrimos, dest = 0, tag = 9 )

if(rank == 0):
  sumaPrimos = numPrimos
  for y in range( 1, size ):
    n_primos = int(comm.recv(source = y, tag=9))
    sumaPrimos = sumaPrimos + n_primos

  print(f"{size:3},{sumaPrimos},{str(MPI.Wtime()-t1):12.10}" )