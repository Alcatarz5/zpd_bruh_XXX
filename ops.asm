;char = 1 byte
;int = 4 bytes
;short = 2 bytes 
;Выравнивание по 4 байта

;Сложение: op1 (eax) + op2 (ebx) = ecx
mov	eax, $reg1/[ds:$op1_name]/$const1
mov 	ebx, $reg2/[ds:$op2_name]/$const2
mov 	ecx, eax
add 	ecx, ebx

;Вычитание: op1 (eax) - op2 (ebx) = ecx
mov	eax, $reg1/[ds:$op1_name]/$const1
mov 	ebx, $reg2/[ds:$op2_name]/$const2
mov	ecx, eax
sub 	ecx, ebx

;Деление: op1 (eax) / op2 (ebx) = ecx
mov	eax, $reg1/[ds:$op1_name]/$const1
mov 	ebx, $reg2/[ds:$op2_name]/$const2
idiv	ebx
mov	ecx, eax

;Остаток от деления: op1 (eax) % op2 (ebx) = ecx
mov	eax, $reg1/[ds:$op1_name]/$const1
mov 	ebx, $reg2/[ds:$op2_name]/$const2
xor	edx, edx
idiv	ebx
mov	ecx, edx

;Умножение: op1 (eax) * op2 (ebx) = ecx
mov	eax, $reg1/[ds:$op1_name]/$const1
mov 	ebx, $reg2/[ds:$op2_name]/$const2
imul	ebx
mov	ecx, eax

;Определение: Если стоит тип перед переменной
$var_name	dd	 0

;Присвоение: =
mov	dword [ds:$var_name], $const/$reg


