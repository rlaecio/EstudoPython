'''
Created on 11 de jul de 2017

@author: rsouza
'''
n = int(raw_input('Numero a testar: '))
for i in range(2,n):
    if n % i == 0: 
        print 'Numero nao primo';
        break