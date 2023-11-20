import math

def simplify(frac): #upraszczanie ułamka
    number = math.gcd(frac[0], frac[1])
    frac[0] //= number
    frac[1] //= number

def add_frac(frac1, frac2): #frac1 + frac2
    numerators = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    denominators = frac1[1] * frac2[1]
    operation = [numerators, denominators]
    simplify(operation) # upraszczanie ułamka
    return operation

def sub_frac(frac1, frac2):  #frac1 - frac2
    numerators = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    denominators = frac1[1] * frac2[1]
    operation = [numerators, denominators]
    simplify(operation)
    return operation

def mul_frac(frac1, frac2):  #frac1 * frac2
    numerators = frac1[0] * frac2[0]
    denominators = frac1[1] * frac2[1]
    operation = [numerators, denominators]
    simplify(operation)
    return operation

def div_frac(frac1, frac2):  #frac1 / frac2
    numerators = frac1[0] * frac2[1]
    denominators = frac1[1] * frac2[0]
    operation = [numerators, denominators]
    simplify(operation)
    return operation

def is_positive(frac):  #bool, czy dodatni
    operation = frac[0] * frac[1]
    return operation > 0

def is_zero(frac):  #bool, typu [0, x]
    return frac[0] == 0

def cmp_frac(frac1, frac2):  #-1 | 0 | +1
    operation = frac1[0] * frac2[1] - frac1[1] * frac2[0]
    absolute = abs(operation)
    if operation == 0:
        return 0
    else:
        return (operation // absolute) #dzielenie całkowite -> zwraca +1 - dodatnie lub -1 - ujemne

def frac2float(frac):  #konwersja do float
    return frac[0] / frac[1]



