from Classes import *
#from main import *
instructionsArr=[]
registersArr=[]
modesArr=[]
indexedModeArr=[]
variablesArr=[]
labelsArr=[]
    
def add():  
  
    
    #-----------------------------------------# 9
    #search for ","
    instructionsArr.append(Instructions("MOV",2,"instruction"))
    instructionsArr.append(Instructions("ADD",2,"instruction"))
    instructionsArr.append(Instructions("ADC",2,"instruction")) #add with carry
    instructionsArr.append(Instructions("SUB",2,"instruction"))
    instructionsArr.append(Instructions("SBC",2,"instruction"))#sub with carry
    instructionsArr.append(Instructions("AND",2,"instruction"))
    instructionsArr.append(Instructions("OR",2,"instruction"))
    instructionsArr.append(Instructions("XNOR",2,"instruction"))
    instructionsArr.append(Instructions("CMP",2,"instruction"))#zero flag
    #--------------------------------------------# 11
    instructionsArr.append(Instructions("INC",1,"instruction")) #=1
    instructionsArr.append(Instructions("DEC",1,"instruction")) #-1
    instructionsArr.append(Instructions("CLR",1,"instruction"))
    instructionsArr.append(Instructions("INV",1,"instruction"))
    instructionsArr.append(Instructions("LSR",1,"instruction"))
    instructionsArr.append(Instructions("ROR",1,"instruction"))
    instructionsArr.append(Instructions("RRC",1,"instruction"))
    instructionsArr.append(Instructions("ASR",1,"instruction"))
    instructionsArr.append(Instructions("LSL",1,"instruction"))
    instructionsArr.append(Instructions("ROL",1,"instruction"))
    instructionsArr.append(Instructions("RLC",1,"instruction"))
    #---------------------------------------------# 9
    #if branch instruction read branch name and search in look up table to get address
    instructionsArr.append(Instructions("BR",1,"branch"))
    instructionsArr.append(Instructions("BEQ",1,"branch"))
    instructionsArr.append(Instructions("BNE",1,"branch"))
    instructionsArr.append(Instructions("BLO",1,"branch"))
    instructionsArr.append(Instructions("BLS",1,"branch"))
    instructionsArr.append(Instructions("BHI",1,"branch"))
    instructionsArr.append(Instructions("BHS",1,"branch"))
    #---------------------------------------------# 2
    instructionsArr.append(Instructions("HLT",0,"instruction"))
    instructionsArr.append(Instructions("NOP",0,"instruction"))
    #---------------------------------------------# 4
    instructionsArr.append(Instructions("JSR",0,"routine"))
    instructionsArr.append(Instructions("RTS",0,"routine"))
    instructionsArr.append(Instructions("INTERRUPT",0,"routine"))
    instructionsArr.append(Instructions("IRET",0,"routine"))
    #-------------REGISTERS-------------------------#
    registersArr.append(Register("R0"))
    registersArr.append(Register("R1"))
    registersArr.append(Register("R2"))
    registersArr.append(Register("R3"))
    registersArr.append(Register("R4"))
    registersArr.append(Register("R5"))
    registersArr.append(Register("R6"))    #PC
    registersArr.append(Register("R7"))     #SP
    #------------------------------------------------#
            #----Auto Increment------#
    modesArr.append(addressingModes("(R0)+"))
    modesArr.append(addressingModes("(R1)+"))
    modesArr.append(addressingModes("(R2)+"))
    modesArr.append(addressingModes("(R3)+"))
    modesArr.append(addressingModes("(R4)+"))
    modesArr.append(addressingModes("(R5)+"))
    modesArr.append(addressingModes("(R6)+"))
    modesArr.append(addressingModes("(R7)+"))
            #---------Auto decrement---------#
    modesArr.append(addressingModes("-(R0)"))   
    modesArr.append(addressingModes("-(R1)"))  
    modesArr.append(addressingModes("-(R2)"))  
    modesArr.append(addressingModes("-(R3)"))  
    modesArr.append(addressingModes("-(R4)"))  
    modesArr.append(addressingModes("-(R5)"))  
    modesArr.append(addressingModes("-(R6)"))  
    modesArr.append(addressingModes("-(R7)"))
           #----------Indirect---------#
    modesArr.append(addressingModes("@R0"))   
    modesArr.append(addressingModes("@R1"))
    modesArr.append(addressingModes("@R2"))
    modesArr.append(addressingModes("@R3"))
    modesArr.append(addressingModes("@R4"))
    modesArr.append(addressingModes("@R5"))
    modesArr.append(addressingModes("@R6"))
    modesArr.append(addressingModes("@R7")) 
        #---------Auto increment indirect----#
    modesArr.append(addressingModes("@(R0)+"))
    modesArr.append(addressingModes("@(R1)+")) 
    modesArr.append(addressingModes("@(R2)+")) 
    modesArr.append(addressingModes("@(R3)+"))  
    modesArr.append(addressingModes("@(R4)+")) 
    modesArr.append(addressingModes("@(R5)+")) 
    modesArr.append(addressingModes("@(R6)+")) 
    modesArr.append(addressingModes("@(R7)+")) 
       #------Auto decrement indirect-----#
    modesArr.append(addressingModes("@-(R0)")) 
    modesArr.append(addressingModes("@-(R1)")) 
    modesArr.append(addressingModes("@-(R2)")) 
    modesArr.append(addressingModes("@-(R3)")) 
    modesArr.append(addressingModes("@-(R4)")) 
    modesArr.append(addressingModes("@-(R5)")) 
    modesArr.append(addressingModes("@-(R6)")) 
    modesArr.append(addressingModes("@-(R7)"))
        #---------Indexed----------#
    indexedModeArr.append(addressingModes("(R0)")) 
    indexedModeArr.append(addressingModes("(R1)"))
    indexedModeArr.append(addressingModes("(R2)"))
    indexedModeArr.append(addressingModes("(R3)"))
    indexedModeArr.append(addressingModes("(R4)"))
    indexedModeArr.append(addressingModes("(R5)"))
    indexedModeArr.append(addressingModes("(R6)"))
    indexedModeArr.append(addressingModes("(R7)"))
    #----KDA FADEL INDEXED INCREMENT---#
    

    