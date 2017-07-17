# encoding: utf-8
'''
Created on 11 de jul de 2017

@author: rsouza
'''
lst = []
for i in range(3):
    while 1:
        try:
            lst.append(int(raw_input('Digite um valor: ')));
            break
        except:
            print 'Digite somente números!!!';
            break