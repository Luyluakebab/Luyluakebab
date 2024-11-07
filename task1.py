import math


def task1():
    """Произвести по формуле расчет функций а=2*sin*x+((|y|**1/2)/(1+ln*x)), b=ln(1+x)+(|y|**1/2)*(z**1/2)+y+z"""

from math import sin, log, fabs

x = float(input("Введите значение переменной x: "))
y = float(input("Введите значение переменной y: "))
z = float(input("Введите значение переменной z: "))

a = 2*sin(x) + (fabs(y)**1/2)/(1+log(x))
b = log(1+x) + (fabs(y)**1/2)*fabs(z) + y + z

print(f"Полученно значение функции a={a}")
print(f"Полученно значение функции b={b}")
