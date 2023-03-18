# Ejercicio 1: Calcular el maximo comin divisor de dos numeros

def mcd(x, y):
    mcd = 1

    if x % y == 0:
        return y
    
    for k in range(int (y/2), 0, -1):
        if x % k == 0 and y % k == 0 :
            mcd = k
            break


    return mcd


print(mcd(13,7))
print(mcd(16, 8))

