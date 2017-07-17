'''
Created on 11 de jul de 2017

@author: rsouza
'''
import winsound 
import time
s = time.sleep
b=winsound.Beep

for i in range(1,4):
    for j in range(1,5):
        b(100*j*i,50)
        s(0.01)
    s(0.01)
