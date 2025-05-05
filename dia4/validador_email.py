while True:

 email = input('Digite o seu email: ').lower()
 if '@' in email or '.com' in email:
     print('Tem @ ou .com :)')
 else:
     print('Não tem nada de interessante :(')

 repetir = input('Rodar novamente?? (s/n)').lower()
 if repetir != 's':
     print('Fechando programa... bye')
     break
