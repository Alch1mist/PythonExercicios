# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule
# e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Comprimento do cateto oposto'))
ca = float(input('Comprimento do cateto adjacente'))
hi = hypot(co, ca)  #(co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai mediar {:.2f}'.format(hi))