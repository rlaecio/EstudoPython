#encoding UTF-8
'''
Created on 11 de jul de 2017

@author: rsouza
'''
arquivo = open('tabela.txt','w')
for i in range(100):
    arquivo.write('%i euros valem %.2f reais \n' %(i, i*3.64))
arquivo.close()

