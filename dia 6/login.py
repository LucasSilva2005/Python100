usuario_correto = 'admin'
senha_correta = '1234'
usuario = input('Digite o usuário: ')
senha = input('Digite a senha: ')

if usuario == usuario_correto and senha == senha_correta:
 print('Acesso permitido')
else:
 print('Acesso negado')