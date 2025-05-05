print('-'*12)
print('Operadores aritméticos (soma, subtração, multiplicação, divisão)')
a = 10
b = 3
print('Soma', a + b)
print('Potência', a ** b)
print('Resto da divisão', a % b)

print('-'*12)
print('\n')
print('Operadores relacionais \n')
print("a é igual a b?", a == b)
print("a é maior que b?", a > b)

print('-'*12)
print('\n')
print('Operadores lógicos \n')
tem_cafe = True
tem_leite = False
print("Vai ter café com leite?", tem_cafe and tem_leite)
print("Tem alguma coisa pra beber?", tem_cafe or tem_leite)
print("Não tem leite?", not tem_leite)