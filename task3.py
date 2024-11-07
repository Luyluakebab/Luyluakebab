def task3():
    """Произвести по формуле расчет функции f(x)=2**(-x)-(cos(x)+sin(2*x)**1/2)"""

from math import cos, sin

x = float(input("Введите значение переменной x: "))

f = 2**(-x) - (cos(x) + sin(2*x)**1/2)

print(f"Полученно значение функции f(x)={f}")
