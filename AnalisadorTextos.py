print('='*10, 'Analisador de Textos - Exemplo 1' ,'='*10)
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))

#=====================================================================================

print('\n','='*10, 'Analisador de Textos - Exemplo 2' ,'='*10)
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))

# Strip() - Remove os espaços
# lean() - Comprimento da Frase
# Count() - Contar número de palavras
# Find() - Quantas vezes encontrou (nome)
# ==================================================================================


