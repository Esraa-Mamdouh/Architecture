# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 23:55:26 2018

@author: Esraa
"""
class Instructions():
    def __init__(self,instruction,noOf_Operands):
        self.instruction=instruction
        self.noOf_Operands=noOf_Operands
       # self.code=code
       def set_Code(self,code):
           self.code=code
class Register():
    def __init__(self,registerName):
        self.registerName=registerName
       def set_Code(self,code):
           self.code=code