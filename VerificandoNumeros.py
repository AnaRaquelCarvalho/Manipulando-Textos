print('\n','='*6,' Verificando as primeiras letras de um texto ','='*6)
city = str(input('Em que cidade você nasceu? ')).strip()
print(city[:5].upper == 'SANTO','\n') 

print('\n','='*6, 'Procurando uma String dentro da outra' ,'='*6)
nome = str(input('Informe seu nome completo: '))
print('Este nome contém Silva nele? {}'.format('SILVA' in nome.upper()))
print('='*52)


