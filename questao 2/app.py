

termo1 = 0
termo2 = 1
termo3 = 0

Valor = int(input('Digite um número: '))
while Valor > termo3:
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
if Valor == 0 or Valor == 1:
    print ('O número faz parte da sequência de Fibonacci.')
elif Valor == termo3:
    print ('O número faz parte da sequência de Fibonacci.')
else:
    print ('O número digitado não faz parte da sequência de Fibonacci.')
