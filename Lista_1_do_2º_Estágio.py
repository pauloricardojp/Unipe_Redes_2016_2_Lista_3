## Exercício 1 ##
## Faz a classificação de um usuário, com base em algumas perguntas. ##
'''
for i in range(10):

    contador_sim = 0
    contador_nao = 0

    respostas = [input("Telefonou para a vítima? "),
                 input("Esteve no local do crime? "),
                 input("Mora perto da vítima? "),
                 input("Devia para a vítima? "),
                 input("Já trabalhou com a vítima? ")]

    for resposta in respostas:
        if resposta == 'sim' or resposta == 'SIM' or resposta == 'Sim':
            contador_sim = contador_sim + 1
        else:
            contador_nao = contador_nao + 1

    if contador_sim == 5:
        print('Você é considerado ASSASSINO')
        break
    elif contador_sim == 3 or contador_sim == 4:
        print('Você é considerado CUMPLICE')
    elif contador_sim == 2:
        print('Você é considerado SUSPEITO')
    else:
        print('Você é considerado INOCENTE')
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
for i in range(5):

    contador_sim = 0
    contador_nao = 0

    respostas = [input('Sabe ligar o computador? '),
                 input('Já trabalhou com o Windows 3.5? '),
                 input('Já usou disquete? '),
                 input('Sabe ligar o computador? '),
                 input('Sabe programar em python? ')]

    for resposta in respostas:
        if resposta == 'Sim' or resposta == 'SIM' or resposta == 'sim':
            contador_sim = contador_sim + 1
        else:
            contador_nao = contador_nao + 1

    if contador_sim == 5:
        print('Você é um Hacker!')
        break
    elif contador_sim == 3 or contador_sim == 4:
         print('Sabe alguma coisa!')
    elif contador_sim == 2:
        print('Tá aprendendo!')
    else:
        print('Sabe de nada inocente!')
'''















