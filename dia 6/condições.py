peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

print('Seu imc é: {}'.format(imc))

if imc < 18.5:
 print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
 print('Você está no peso normal')
elif 25 <= imc <30:
 print('Você está acima do peso normal')
else:
 print('Você está obeso')