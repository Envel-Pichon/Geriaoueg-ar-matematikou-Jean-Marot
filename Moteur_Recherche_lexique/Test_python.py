import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
import string
l = int(input())
h = int(input())
t = input()
longueur = len(t)
lettres = [ [""]*l for j in range(longueur)]
positions = [string.ascii_lowercase.index(t[i].lower()) for i in range(len(t))]
print(lettres)
print(positions)
for i in range(h):
    row = input()
  
for k in range(l):
    lettres[0] = lettres[0] + row[k+4*positions[1]][0]
    #    lettres[1] = lettres[1] + row[k+4*position(1)][0]
    print(lettres[0])
# Write an answer using print