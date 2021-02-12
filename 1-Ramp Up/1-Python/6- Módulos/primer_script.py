# -*- coding: utf-8 -*-
"""
Ejemplo de un módulo Python. Contiene una variable llamada pi,
una función para calcular el área de un círculo de radio r
y una clase llamada Punto.

Created on Thu Feb 11 20:25:42 2021

@author: rzambrano
"""

import math

pi = math.pi

def area_circulo(radio):
    """
    Función que devuelve el área de un círculo de radio r
    """
    return pi*radio**2

class Punto:
    """
    Clase que instancia puntos en 2 dimensiones
    """
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def formato(self):
        '''
        Devuelve un string con el formato (x, y)
        '''
        txt = '(' + str(self.x) + ', ' + str(self.y) + ')'
        
        return txt
    
    def cuadrante(self):
        '''
        Devuelve el cuadrante donde se encuentra el punto
        '''
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        elif self.x != 0 and self.y == 0:
            return 'x'
        elif self.x == 0 and self.y != 0:
            return 'y'
        else:
            return 0
        
    def distancia(self,p):
        '''
        Calcula la distancia a otro punto p
        '''
        d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        return d
        
        
        
        
        
    
    
    
    
    
    
