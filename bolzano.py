# Bolzano Root Finder and Plotter
# Author: Richie Seputro

import numpy as np
import matplotlib.pyplot as plt

def f(x, c, n):
    res = 0
    for ci in c:
        res += ci * (x ** n)
        n -= 1
    return res

s = '''This is a program that approximates the roots of an equation using
<<Bolzano method>>'''
print(s)

deg = int(input("Enter the degree of your equation: "))
lbound = float(input("Enter the lower bound x-value: "))
ubound = float(input("Enter the upper bound x-value: "))
step = float(input("Enter the x-step value: "))
tolerance = float(input("Enter the tolerance value: "))
middle = lbound

i = deg
coeffs = []

while i >= 0:
    coeffs.append(float(input(f"Enter coefficient number {deg - i + 1}: ")))
    i -= 1

xlist = np.arange(lbound, ubound, step)
ylist = f(xlist, coeffs, deg)

while abs(f(middle, coeffs, deg)) > tolerance:
    middle = lbound/2 + ubound/2
    y = f(middle, coeffs, deg) * f(ubound, coeffs, deg)
    if y < 0:
        lbound = middle
    elif y > 0:
        ubound = middle
    else:
        break
print(f"Root: {middle}")

fig, ax = plt.subplots()
ax.plot(xlist, ylist)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.title("Function Plot")
plt.savefig('plot.png')
