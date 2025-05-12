.MODEL SMALL
.STACK 100H
.386
.DATA
To_Decrypt db 0,'~','}','|','{','z','y','x','w','v'
DB 'u','t','s','r','q','p','o','n','m','l'
DB 'k','j','i','h','g','f','e','d','c','b'
DB 'a','`','_','^',']','\','[','Z','Y','X'
DB 'W','V','U','T','S','R','Q','P','O','N'
DB 'M','L','K','J','I','H','G','F','E','D'
DB 'C','B','A','@','?','>','=','<',';',':'
DB 57,56,55,54,53,52,51,50,49,48
DB '/','.','-',',','+','*',')','(',39,'&'
DB '%','$','#','"','!',32,96,97,98,99
DB 100,101,102,103,104,105,106,107,108,109
DB 110,111,15,14,114,115,11,117,118,'8'
DB 120,121,122,123,124,125,126,127


To_Encrypt db 127,126,125,124,123,122,121,120,119,118
DB 117,116,115,114,113,112,111,110,109,108
DB 107,106,105,104,103,102,101,100,99,98
DB 97,96,95,94,93,92,91,90,89,88
DB 87,86,85,84,83,82,81,80,79,78
DB 77,76,75,74,73,72,71,70,69,68
DB 67,66,65,64,63,62,61,60,59,58
DB 57,56,55,54,53,52,51,50,49,48
DB 47,46,45,44,43,42,41,40,39,38
DB 37,36,35,34,33,32,31,30,29,28
DB 27,26,25,24,23,22,21,20,19,18
DB 17,16,15,14,13,12,11,10,9,8
DB 7,6,5,4,3,2,1,0


ENCRYPTED DB 128 DUP(?)

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    MOV ES, AX
	
	MOV CX,0
    
    MOV BX, OFFSET To_Encrypt  
    MOV DI, OFFSET ENCRYPTED 

INPUT_ENCRYPTION:
    MOV AH, 01H                
    INT 21H
    CMP AL, 13                 
    JE EXIT_ENCRYPTION
	CMP CX,127
	JE EXIT_ENCRYPTION
    XLAT                       
    INC CX
	STOSB              
    JMP INPUT_ENCRYPTION

EXIT_ENCRYPTION:

    PUSH CX
	MOV SI,OFFSET ENCRYPTED
	PRINT_ENCRYPTED_STR:
	CMP CX,0
	JE DATA_DECRYPTION
	MOV AH,02
	MOV DL,[SI]
	INT 21H
	INC SI
	DEC CX
	JMP PRINT_ENCRYPTED_STR
	
	
DATA_DECRYPTION:
	CALL NEWLINE
    POP CX
    MOV BX, OFFSET To_Decrypt  
	MOV SI,OFFSET ENCRYPTED
    MOV AH, 02H
LOOP1:
    CMP CX,0               
    JE END_PROGRAM
	MOV AL,[SI] 
    XLAT                       
    MOV DL, AL                 
    INT 21H
	INC SI
	DEC CX
    JMP LOOP1

END_PROGRAM:
    MOV AH, 4CH                
    INT 21H

MAIN ENDP

NEWLINE PROC
    ; Output newline
    PUSH AX
    PUSH DX
    MOV AH, 02H
    MOV DL, 0DH
    INT 21H
    MOV DL, 0AH
    INT 21H
    POP DX
    POP AX
    RET
NEWLINE ENDP

END MAIN