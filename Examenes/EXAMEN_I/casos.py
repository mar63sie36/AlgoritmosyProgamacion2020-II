#Estas funciones reciben de entrada un numero n
# Y retornan el numero n-ésimo de la sucesión de
# Fibonacci
def caso1(n):

    if n < 2:
        return n
    else:
        return caso1(n-1) + caso1(n-2)
    
def caso2(n):
  if n < 2:
        return n
  else:
    a=0
    b=1
    for i in range(2,n+1):
      c=a+b
      a=b
      b=c
    return(c)