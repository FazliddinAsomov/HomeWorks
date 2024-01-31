# Koshi
import math

a, b = map(int, input().split())

o_rta_arifmetik = (a + b) / 2
o_rta_geometrik = math.sqrt(a * b)

if o_rta_arifmetik > o_rta_geometrik:
    print(">")
elif o_rta_arifmetik < o_rta_geometrik:
    print("<")
else:
    print('=')