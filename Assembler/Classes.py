# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 23:55:26 2018

@author: Esraa
"""
class Instructions():
    def __init__(self,instruction,noOf_Operands,types):
        self.instruction = instruction
        self.noOf_Operands=noOf_Operands
        self.types=types
        self.code = instruction
       # self.code=code
        
class Register():
    def __init__(self,registerName):
        self.registerName=registerName
        self.code = registerName
            
class addressingModes():
    
    def __init__(self,mode):
        self.mode = mode
        self.code = mode

class variables():
    def __init__(self,name,value):
        self.name=name
        self.value=value
        self.code = name

class Lables():
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.name
    