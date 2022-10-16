i = 0

while i <= 10:
    print(i)
    i += 1

'''
no python, diferente do php, o incremento i++ não é utilizado.
sendo asssim, i += 1 é uma das formas para incrementação
'''

x = 1

'''
Tabuada do 2
'''

while x <= 10:
    print (2 * x)
    x+=1    
    
'''
Potência de 2
'''
y = 1
while y <= 10:
    print(2**y)
    y+=1
    

'''
calculador de valores de entrada até ser encerrado pelo zero
exemplo: 
'''

valor = 1
soma = 0


while valor != 0:
    valor = int(input("Digite um valor para somar ou zero para finalizar: "))
    soma = soma + valor
    
print("O resultado da soma é: ", soma)