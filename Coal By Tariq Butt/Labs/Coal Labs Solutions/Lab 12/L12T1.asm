.MODEL SMALL
.STACK 100H
.DATA
string_1 db 'Hello, Muhammad Umair! $'
string_2 db 24 dup(?)

.CODE
MAIN PROC
mov ax,@DATA
mov ds,ax
mov es,ax

mov si,offset string_1
mov di,offset string_2

cld

mov cx,24
rep movsb

mov dx,offset string_2
mov ah,09
int 21h

mov ah,4ch
int 21h

MAIN ENDP

END MAIN