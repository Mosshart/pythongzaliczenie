import math

def IsNumberPrime(number):
    if not isinstance(number, int): return 'Błędne dane'
    if number == 0 or number == 1:
        return 'Number is not prime'
    validationNumber = 2
    while validationNumber <= math.sqrt(number):
        if number % validationNumber < 1:
            return 'Number is not prime'
        validationNumber = validationNumber + 1
    return 'Number is prime'