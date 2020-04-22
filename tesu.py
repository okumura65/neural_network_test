import numpy as np
import sympy as sym

x=[[] for _ in range(5)]
for i in range(5):
    x[i]=sym.symbols("x"+str("[")+str(i)+str("]"))
f=sym.tanh(x[0])
print(sym.diff(f,x[0]))
