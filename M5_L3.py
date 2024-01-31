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
# Isfandiyor algebra darsida
def calculate_f(n):
    result = n**5 + 8*n**4 - 5*n**3 + 3*n**2 + n - 12
    return result
with open('input.txt', 'r') as input_file:
    n = int(input_file.readline().strip())
with open('output.txt', 'w') as output_file:
    output_file.write(str(calculate_f(n)))