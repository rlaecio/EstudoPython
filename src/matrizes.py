'''
Created on 16 de jul de 2017

@author: rsouza
'''
ordem = int(raw_input('Ordem da matriz: '))
matriz = []
print 'Digite os termos da matriz A'
for i in range(ordem):
    matriz.append([])
    for j in range(ordem):
        termo = 'A'+str(i+1)+str(j+1)
        matriz[i].append(float(raw_input('Termo'+termo+': ')))
    print '\n'
print ' Matriz A \n'
for k in range(ordem):
    for w in range(ordem):
        print '%8.2f' %matriz[k][w],
    print '\n'
    