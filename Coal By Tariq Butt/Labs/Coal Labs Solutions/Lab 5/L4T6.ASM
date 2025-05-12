.MODEL SMALL
.STACK 100H

.DATA
    arr1 DB 49,50,51,52,53,54,55,56
    arr2 DB 56,55,54,53,52,51,50,49
    sum DB  8 dup(00)

.CODE
printarray PROC
    MOV AH, 02H
    mov cx,8
    until:
    mov dx,[si]
    INT 21H
    inc si
    dec cx
    jnz until
    RET                 
printarray ENDP

addingProc proc
mov cx,8
untill:
mov al,[si]
add al,[bx]
sub al,30h
mov [di],al
inc si
inc bx
inc di
dec cx
jnz untill
RET
addingProc endp


MAIN PROC
    MOV AX, @DATA       
    MOV DS, AX

    LEA si, arr1
    CALL printarray
    
    MOV AH,02H
    MOV DX,0AH
    INT 21H


    LEA si, arr2
    CALL printarray

    MOV AH,02H
    MOV DX,0AH
    INT 21H

    LEA si,arr1
    LEA bx,arr2
    LEA di,sum
    CALL addingProc

    LEA si,sum
    call printarray

    MOV AH, 4CH         
    INT 21H             
MAIN ENDP

END MAIN
