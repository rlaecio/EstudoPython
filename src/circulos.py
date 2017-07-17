'''
Created on 11 de jul de 2017

@author: rsouza
'''
def perimetro(r):
    """Esta funcao calcula o perimetro de um circulo de raio r"""
    try:
        r = float(r)
        return 2 * 3.14 * r
    except:
        print 'O argumento da funcao deve ser um numero'

def area(r):
    """Esta funcao calcula a area de um circulo de raio r."""
    try:
        r = float(r)
        return 3.14*(r**2)
    except:
        print 'O argumento da funcao deve ser um numero.'
        
def potencia(x, y=2):
    """potencia(x, y) eleva x a potencia y. Default: y=2."""
    try:
        return x**y 
    except:
        print 'Argumentos invalidos'
    
    
def nada():
    """Esta funcao nao faz nada"""
    pass