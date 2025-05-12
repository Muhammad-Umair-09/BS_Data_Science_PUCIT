.MODEL SMALL  
.STACK
.386
.DATA
	msg_input_format DB "Enter input  format (b/d/h): $"
	msg_output_format DB "Enter output format (b/d/h): $"
	msg_num_1 DB "Enter n1: $"
	msg_num_2 DB "Enter n2: $"
	msg_operator DB "Enter operator (+, - , /, *): $"	
	msg_sum DB "Sum: $"
	msg_difference DB "Difference: $"
	msg_product DB "Product: $"
	msg_quotient DB "Quotient: $"
	msg_remainder DB "Remainder: $"
	msg_invalid_input DB "Invalid input, Enter again: $"
	msg_invalid_format DB "Invalid format, Enter again (b/d/h): $"
	msg_invalid_operator DB "Invalid operator, Enter again (+, - , /, *): $"
	input_format DB 0
	output_format DB 0
	num_1 DW 0
	num_2 DW 0
	
.CODE
MAIN PROC
	MOV AX, @DATA
	MOV DS, AX
	
	MOV DX, offset msg_input_format
	MOV AH, 09
	INT 21h
	CALL format 
	MOV input_format, CL
	CALL newline	
	
	MOV DX, offset msg_output_format
	MOV AH, 09
	INT 21h
	CALL format 
	MOV output_format, CL
	CALL newline

	MOV DX, offset msg_num_1
	MOV AH, 09
	INT 21h
	MOV CL, input_format
	CALL input
	MOV num_1, DX	
	
	MOV DX, offset msg_num_2
	MOV AH, 09
	INT 21h
	MOV CL, input_format
	CALL input
	MOV num_2, DX	
	
	MOV DX, offset msg_operator
	MOV AH, 09
	INT 21h
	CALL calculation_and_output_result		
	exit:
		MOV AH, 4Ch
		INT 21h
MAIN ENDP

input PROC    ;returns input in DX  ;takes input format in CL
		PUSH AX
		PUSH BX
		PUSH CX
	try_again:
		XOR BX,BX
	start:	
		MOV Ah,01
		INT 21h
		CMP AL, 0Dh  ;ASCII of Carriage Return=13
		JE return
		;Checking validity of input, allowing both upper and lower case alphabets for HEX input
		CMP AL,30h   ;ASCII of '0' ==> 48
		JB invalid_input
		CMP AL, 39h  ;ASCII of '9' ==> 57
		JBE number
		CMP AL, 41h  ;ASCII of 'A' ==> 65
		JB invalid_input
		CMP AL, 46h  ;ASCII of 'F' ==> 70
		JBE upper_case
		CMP AL, 61h  ;ASCII of 'a' ==> 97
		JB invalid_input
		CMP AL, 66h  ;ASCII of 'f' ==> 102
		JBE lower_case
		JMP invalid_input
	number:
		SUB AL, 30h  ;SUB AL, 48
		JMP update
	upper_case:
		SUB AL, 37h  ;SUB AL,55  ; 65-55 = 41h-37h = 10 = 0Ah ; ASCII of A ==> 65=41h
		JMP update
	lower_case:
		SUB AL, 57h  ;SUB AL, 87 ; 97-87 = 61h-57h = 10 = 0Ah ; ASCII of A ==> 65=41h

	update:
		CMP Al, Cl
		JAE invalid_input
		XOR AH, AH  ;MOV AH,0
		PUSH AX
		MOV AX, CX
		MUL BX
		POP BX      ;new input digit
		ADD BX, AX
		JMP start
	invalid_input:
		CALL newline
		MOV DX, offset msg_invalid_input
		MOV AH, 09
		INT 21h
		JMP try_again
	return:	
		MOV DX, BX   ;PROC returns input in DX
		POP CX
		POP BX
		POP AX
		RET
input ENDP 
 
format PROC    ;returns format in CL
	aa:
		MOV AH, 01
		INT 21h
		CMP AL, 'b'
		JE binary
		CMP AL, 'B'
		JE binary
		CMP AL, 'd'
		JE decimal
		CMP AL, 'D'
		JE decimal
		CMP AL, 'h'
		JE hexadecimal
		CMP AL, 'H'
		JE hexadecimal
		CMP AL, 0Dh  ; ASCII of Enter Key
		JE decimal   ; default format is decimal
	invalid_format:
		CALL newline
		MOV DX, offset msg_invalid_format
		MOV AH, 09
		INT 21h
		JMP aa		
	binary:
		MOV CL, 2
		RET
	decimal:
		MOV CL, 10
		RET
	hexadecimal:
		MOV CL, 16
		RET
format ENDP

calculation_and_output_result PROC    ;uses num_1 & num_2 & output_format defined in DATA segment
	bb:
		MOV AH, 01
		INT 21h
		CMP AL, '+'
		JE addition
		CMP AL, '-'
		JE subtraction
		CMP AL, '/'
		JE division
		CMP AL, '*'
		JE multiplication
	
	invalid_operator:
		CALL newline
		MOV DX, offset msg_invalid_operator
		MOV AH, 09
		INT 21h
		JMP bb		
		
	addition:
		CALL newline
		MOV DX, offset msg_sum
		MOV AH, 09
		INT 21h
		MOV AX, num_1
		ADD AX, num_2
	
		MOV BX, 0
		MOV BL, output_format		
		CALL output  ;receives input in AX ; output format in BX
		RET
		
	subtraction:
		call newline
		MOV DX, offset msg_difference
		MOV AH, 09
		INT 21h
		
		MOV AX, num_1
		CMP AX, num_2
		JB swap
		SUB AX, num_2
		JMP display_diff

	swap:
		MOV Dl, '-'
		MOV AH, 02
		INT 21h
		MOV AX, num_2
		SUB AX, num_1
		
	display_diff:
		MOV BX, 0
		MOV BL, output_format		
		CALL output  ;receives input in AX ; output format in BX
		RET
		
	division:
		CALL newline
		MOV DX, offset msg_quotient
		MOV AH, 09
		INT 21h
		
		MOV DX, 0
		MOV AX, num_1
		DIV num_2   ;quotient in AX  ;remainder in DX
		
		MOv BX, 0
		MOV BL, output_format
		CALL output  ;displays Quotient
		CALL newline
		
		PUSH DX
		MOV DX, offset msg_remainder
		MOV AH, 09
		INT 21h
		POP AX
		CALL output  ;displays remainder
		
	multiplication:
		CALL newline
		MOV DX, offset msg_product
		MOV AH, 09
		INT 21h
		MOV AX, num_1
		MOV BX, num_2
		MUL BX  ;product in DX:AX
		
		MOV BX, 0
		MOV BL, output_format
		CALL output ;displays AX
	RET
calculation_and_output_result ENDP

output PROC  ;receives input in AX ; output format in BX
		PUSH AX
		PUSH BX
		PUSH CX
		PUSH DX
		MOV CX, 0
	again:
		MOV DX, 0     ;dividend ==> DX:AX
		DIV BX        ;quotient ==> AX  ;remainder ==> DX
		PUSH DX
		INC CX
		CMP AX, 0
		JE display
		JMP again
	display:
		POP DX
		CMP DX, 9
		JBE digit
		ADD DL, 37h
		JMP continue
	digit:
		ADD DL, 30h
	continue:
		MOV AH, 02
		INT 21h
		DEC CX
		JNZ display
		POP DX
		POP CX
		POP BX
		POP AX
		RET
output ENDP
 
newline PROC
	PUSH AX
	PUSH DX
	MOV AH, 02
	MOV DL, 0Dh  ;carriage return
	INT 21h
	MOV DL, 0Ah  ;line feed
	INT 21h
	POP DX
	POP AX
	RET
newline ENDP
END MAIN