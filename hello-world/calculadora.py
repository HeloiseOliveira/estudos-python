#Receber um número
#Receber um operador
#Receber outro número
#Mostrar o resultado


import operator

dict_operadores ={
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

print("Digite um número")
numero1 = int(input())

print("Digite um operador")
operador = input()

print("Digite um segundo número")
numero2 = int(input())

print(dict_operadores[operador](numero1, numero2))