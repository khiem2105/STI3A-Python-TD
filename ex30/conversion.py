def fahrenheit_to_celcius(fahrenheit):
    assert fahrenheit >= -459.67
    return (fahrenheit - 32) * (5/9)

def celcius_to_fahrenheit(celcius):
    assert celcius >= -273.15
    return (9/5) * celcius + 32

def isalmost(n, m, d=1):
    if abs(m-n) <= d:
        return True
    return False

assert isalmost(fahrenheit_to_celcius(-459.67), -273.15, 1e-13)        