import sys
import math
import time


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

# -------------------------------

t1 = time.time()

m = int(sys.argv[1])
numPrimos = 0

for x in range (2, m+1):
  if EsPrimo(x) == 1:
    numPrimos = numPrimos + 1

print(str(time.time()-t1))
print("Hay ", numPrimos, " primos <=",m)