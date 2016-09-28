## Exercício 1 ##
## Faz a classificação de um usuário, com base em algumas perguntas. ##
'''
perguntas = ['Telefonou para a vítima?',
             'Esteve no local do crime?',
             'Mora perto da vítima?',
             'Devia para a vítima?',
             'Já trabalhou com a vítima?']

soma_sim = 0

for contador in range(5):

    print(perguntas[contador])

    resposta = input('Responda, Sim ou Não: ')

    if resposta == 'sim' or resposta == 'SIM' or resposta == 'Sim':
        soma_sim = soma_sim + 1

if soma_sim == 2:
    print('Você é considerado Suspeito')

elif soma_sim == 3 or soma_sim == 4:
    print('Você é considerado Cumplice')

elif soma_sim == 5:
    print('Você é considerado Assassino')

else:
    print('Você é considerado Inocente')
'''

## Exercício 2 ##
## Informa se o número é par ou ímpar, mostrando na tela os números digitados, os pares e ímpares. ##
'''
numeros = []
num_par = []
num_impar = []


for contador in range(20):
    numero = int(input('Digite um Número: '))
    numeros.append(numero)

    if numero % 2 == 0:
        num_par.append(numero)
    else:
        num_impar.append(numero)

print('Números digitados: ',numeros)
print('Números pares: ',num_par)
print('Números Ímpares: ',num_impar)
'''

## Eercício 3 ##
## Mostra na tela os números digitados, a soma e multiplicação dos mesmos. ##
'''
numeros = []

soma = 0
mult = 1

for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    mult = mult * numero
    soma = soma + numero

print('O resultado da soma dos números eh: ',soma)
print('O resultado da multiplicação dos números eh: ',mult)
print('Números digitados pelo o usuário: ',numeros)
'''

## Exercício 4 ##
## Faz uma clasificação de um usuário, com relação do uso do computador. ##
'''
perguntas = ['Sabe ligar o computador? ',
             'Já trabalhou com o Windows 3.5? ',
             'Já usou disquete? ',
             'Sabe ligar o computador? ',
             'Sabe programar em python? ']


soma_sim = 0

for contador in range(5):
    print(perguntas[contador])
    resposta = input('Responda, Sim ou Não: ')

    if resposta == 'sim' or resposta == 'SIM' or resposta == 'Sim':
        soma_sim = soma_sim + 1

if soma_sim == 5:
    print('Você é um Hacker!')
elif soma_sim == 3 or soma_sim == 4:
    print('Sabe alguma coisa!')
elif soma_sim == 2:
    print('Tá aprendendo!')
elif soma_sim == 1:
    print('Sabe de nada inocente!')
else:
    print('Opção Inválida! Responda Sim ou Não')
'''














