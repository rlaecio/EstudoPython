# encoding: utf-8
'''
Created on 11 de jul de 2017

@author: rsouza
'''

n = int(raw_input('Digite o número a ser testado: '))
teste = 0
for i in range(1,n):
    if n % i == 0:
        teste = teste+i
if teste == n:
    print n, 'é um numero perfeito'
else:
    print n,'não é um numero perfeito'