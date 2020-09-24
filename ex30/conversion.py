def fahrenheit_to_celcius(fahrenheit):
    assert fahrenheit >= -459.67, fahrenheit
    return (fahrenheit - 32) * (5/9)

def celcius_to_fahrenheit(celcius):
    assert celcius >= -273.15, celcius
    return (9/5) * celcius + 32

def isalmost(n, m, d=1):
    return abs(m-n) <= d

assert isalmost(fahrenheit_to_celcius(-459.67), -273.15, 1e-13)        