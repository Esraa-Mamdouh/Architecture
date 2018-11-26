# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 00:16:07 2018

@author: WIN  10
"""

from Classes import *
from Data import *



def main():
   
    add()
    
    #for i in range(len(instructionsArr)):
        #print(instructionsArr[i].code)
    #print(instructionsArr[0].code)
    
    print(Process('output01.txt'))
    #-----------------------------------------------#
    
    
    

 


def Process(filepath):
    
    Lines=[]
    inputFile = open(filepath,'r')

    lines = inputFile.readlines()
    
    for i in range(len(lines)):
        
        line = lines[i] #read line
        Str = line.split()
        length= len(Str)
        
        if(length > 0):
            
            instr = searchInstruction(Str[0]) #return obj instr
            length -=1
            
            if(instr != None): 
                
                #TODO remove comments before this step
                if(instr.noOf_Operands != length):
                    return "syntax error: Expected no operand get more"
                
                if instr.noOf_Operands == 0:
                    Lines.append(instr.code)
                    Lines.append('\n')
                    
                if instr.types == "branch":
                    Branch(Str[1])
                    
                elif instr.types == "instruction":
                    if instr.noOf_Operands == 0:
                        opr1(Str[1])

                    elif instr.noOf_Operands == 1:
                        opr2(Str[2])
                        
                    
                    
                
                
                
                
                
                
                
                
                    
                # else:
                        
                    
        #     op1 = search(Str[1])
        #     length -=1
            
        #     if(op1 != None):
                
        #         if(length>0):
                    
        #             if(instr.noOf_Operands ==1):
        #                 return "syntax error: Expected one operand get more"
        #             elif (instr.noOf_Operands ==2):
        #                     op2 = search(Str[2])
        #                     length -=1
        #                     if(length>0):
        #                         return "syntax error: Expected two operands get more"
        #                     else:
        #                         print(type(instr))
        #                         print(instr.code)
                                
        #                         Lines.append(instr.code)
        #                         Lines.append(' ')
        #                         Lines.append(op1.code)
        #                         Lines.append(' ')
        #                         Lines.append(op2.code)
        #                         Lines.append('\n')
        #             else:
        #                 Lines.append(instr.code)
        #                 Lines.append(' ')
        #                 Lines.append(op1.code)
        #                 Lines.append('\n')
        #     else: 
        #         return "syntax error: Expected operand get zero"
        # elif (instr.noOf_Operands ==2):
        #         if(length >0):
        #             return instr.instruction
        #         else: 
        #             return "syntax error: Expected two operands get one"
    
    return Lines


def search(str):
    Reg = searchRegister(str)
    if(Reg != None):
        return Reg
    else:
        var = searchVariables(str)
        if(var != None):
            return var
        else:
            modes = searchModes(str)
            if(modes != None):
                return modes
            else:
                indexd= searchIndexed(str)
                if(indexed != None):
                    return indexed
                else:
                    lab=searchLable(str)
                    if(lab != None):
                        return lab
                
    
    return None


def opr1(opp):
    #in progress

def opr2(opp):
    
    #in progress

def searchIndexed (mod):
    for i in range (len(indexedModeArr)) :
        if(mod == indexedModeArr[i].mode):
            return indexedModeArr[i]
    return None


def searchModes (mod):
    for i in range (len(modesArr)) :
        if(mod == modesArr[i].mode):
            return modesArr[i]
    return None

def lookUpTable():
    pass
    ####################
    #---------Lables Array--------------#
def appendLabel(name):           #send name
    labelsArr.append(Lables(name))
    
    
#----------------------#
def appendVariable(name):           #send name
    variablesArr.append(variables(name))
    
    
#-------------------#
def searchVariables(str):
    if(len(variablesArr)<=0):
        return  None  ###
    for i in range (len(variablesArr)):
        if(str == variablesArr[i].name):
            return variablesArr[i]
    return None


 #----------------------------#   
def searchLables(str):
    if(len(labelsArr)<=0):
        return None
    for i in range (len(labelsArr)):
        if(str == labelsArr[i].name):
            return labelsArr[i]
    return None

def searchInstruction(inst):
    for i in range (len(instructionsArr)):
        if( inst == instructionsArr[i].instruction):
            return instructionsArr[i]
    return None


def searchRegister(Reg):
    for i in range (len(registersArr)):
        if(Reg == registersArr[i].registerName):
            return registersArr[i]   
    return None
    ####################
       
        



