.MODEL SMALL
.STACK 100H

.DATA
    nameStr DB 'MUHAMMAD UMAIR$'
    ADDR DB 'GUJRANWALA$'

.CODE
printString PROC
    MOV AH, 09H         
    INT 21H             
    RET                 
printString ENDP

MAIN PROC
    MOV AX, @DATA       
    MOV DS, AX

    LEA DX, nameStr     
    CALL printString    
    
    MOV AH,02H
    MOV DX,0AH
    INT 21H
    MOV DX,0DH


    LEA DX, ADDR   
    CALL printString    


    MOV AH, 4CH         
    INT 21H             
MAIN ENDP

END MAIN
