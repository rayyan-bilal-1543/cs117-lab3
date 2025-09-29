section .data
    msg db 'Result: ', 0
    msgLen equ $ - msg

    result db 0

section .text
    global _start

_start:
    mov al, 2        ; first number
    mov bl, 3        ; second number

    add al, bl       ; AL = AL + BL

    ; Convert to ASCII (assuming result is <10)
    add al, '0'
    mov [result], al

    ; Print "Result: "
    mov eax, 4
    mov ebx, 1
    mov ecx, msg
    mov edx, msgLen
    int 0x80

    ; Print result digit
    mov eax, 4
    mov ebx, 1
    mov ecx, result
    mov edx, 1
    int 0x80

    ; Exit
    mov eax, 1
    mov ebx, 0
    int 0x80
