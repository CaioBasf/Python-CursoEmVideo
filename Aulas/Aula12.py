nome = str(input('Qual é seu nome '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome femiminino')
else:
    print('Seu nome é bem normal.')

print(f'Tenha um bom dia {nome}')

'''
Essa é uma estutura condicional aninhada
aninhada = pois está em formato de ninho,
uma coisa dentro da outra
'''