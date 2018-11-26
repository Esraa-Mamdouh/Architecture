# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 00:16:07 2018

@author: WIN  10
"""

from Classes import *
def main():
    global instructionsArr=[]
    global registersArr=[]
    #-----------------------------------------# 9
    #search for ","
    instructionArr.append(Instructions("MOV",2))
    instructionsArr.append(Instructions("ADD",2))
    instructionsArr.append(Instructions("ADC",2)) #add with carry
    instructionsArr.append(Instructions("SUB",2))
    instructionsArr.append(Instructions("SBC",2))#sub with carry
    instructionsArr.append(Instructions("AND",2))
    instructionsArr.append(Instructions("OR",2))
    instructionsArr.append(Instructions("XNOR",2))
    instructionsArr.append(Instructions("CMP",2))#zero flag
    #--------------------------------------------# 11
    instructionsArr.append(Instructions("INC",1)) #=1
    instructionsArr.append(Instructions("DEC",1)) #-1
    instructionsArr.append(Instructions("CLR",1))
    instructionsArr.append(Instructions("INV",1))
    instructionsArr.append(Instructions("LSR",1))
    instructionsArr.append(Instructions("ROR",1))
    instructionsArr.append(Instructions("RRC",1))
    instructionsArr.append(Instructions("ASR",1))
    instructionsArr.append(Instructions("LSL",1))
    instructionsArr.append(Instructions("ROL",1))
    instructionsArr.append(Instructions("RLC",1))
    #---------------------------------------------# 9
    #if branch instruction read branch name and search in look up table to get address
    instructionsArr.append(Instructions("BR",1))
    instructionsArr.append(Instructions("BEQ",1))
    instructionsArr.append(Instructions("BNE",1))
    instructionsArr.append(Instructions("BLO",1))
    instructionsArr.append(Instructions("BLS",1))
    instructionsArr.append(Instructions("BHI",1))
    instructionsArr.append(Instructions("BHS",1))
    #---------------------------------------------# 2
    instructionsArr.append(Instructions("HLT",0))
    instructionsArr.append(Instructions("NOP",0))
    #---------------------------------------------# 4
    instructionsArr.append(Instructions("JSR",0))
    instructionsArr.append(Instructions("RTS",0))
    instructionsArr.append(Instructions("INTERRUPT",0))
    instructionsArr.append(Instructions("IRET",0))
    #-------------REGISTERS-------------------------#
    registersArr.append(Register("R0"))
    registersArr.append(Register("R1"))
    registersArr.append(Register("R2"))
    registersArr.append(Register("R3"))
    registersArr.append(Register("R4"))
    registersArr.append(Register("R5"))
    registersArr.append(Register("R6"))    #PC
    registersArr.append(Register("R7"))     #SP
    #-----------------------------------------------#
def searchInstruction(inst):
    for i in range len(instructionsArr):
        if( inst == instructionsArr[i].instruction):
            return instructionsArr[i]
def searchRegister():
    for i in range len(registersArr):
        if(inst == registersArr[i].registerName):
            return registersArr[i]   
def lookUpTable():
    ####################
    


if __name__ == "__main__":
    main()
