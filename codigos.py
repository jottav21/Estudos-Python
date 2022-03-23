#desafio001:escreva um programa que leia:'ola mundo'
print('ola mundo!')
#desafio002:faca um programa que leia o nome da pessoa e mostre uma mensagem de boas-vindas:
nome = input("Digite seu nome: ")
print(f'Olá {nome}! Seja bem-vindo!')
#desafio003: crie um programa que leia a soma entre dois numeros:
n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
s = n1 + n2
print(f'A soma entre {n1} e {n2} é igual a: {n1 + n2}')
#desfio004:faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo e todas as informações sobre ela:
a = input("digite algo:")
print('o tipo primitivo desse valor é',type(a))
print('so tem espaço?',a.isspece())
print('e um numero?',a.isnumerico())
print('e alfabetico?',a.isalpha())
print('e alfanumerico?',a.isalnum())
#desafio005:faça um programa que leia um numero intero e mostre seu sucessor e antecessor:
a = int(input('Digite um valor: ))   
print(f'Seu antecessor é {a-1} e seu sucessor é {a+1}!')
#desafo006:crie um algoritimo que leia mu numero e mostre o seu dobro,tripo e sua raiz quadrada:
n = int(input('Digite um número: '))
print(f'O dobro de {n} é {n*2}.\nO triplo é {n*3}\nA raiz quadrada é {n**(1/2):.2f}.')
#desafio007:desenvolva um progama que leia duas notas de um aluno, calcule e mostre a sua media.
n1 = int(input("Primeira nota do aluno: "))
n2 = int(input("Segunda nota do aluno: "))
media = (n1 + n2)/2
print(f"A Media entre {n1} e {n2} e igual a {(n1+n2)/2}") 
#desafio08:escreva um programa que leia um valor em metro e o  exiba convertido me centrimetros e melimitros
medida = float(input('Uma distancia em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('a media  de  {}m coresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))
#desafio009:faça um programa que leia um numero inteiro e mostre a sua tabuada:
num = int(input('Digite um número para saber sua tabuada: '))
print('A tabuada de {} é: '.format(num))
a = 0
for i in range(1,11):
    a = a+1
    print('{} x {} = ' .format(num,a), num*i)
#desafio010:crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quanto dolares ela pode comprar. considerando US$1,00 = R$3,27
real = float(input("Quanto de dinheiro você tem na conta? R$ "))
dolar = real / 5.07
print("Com R$ {:.2f} você pode comprar US {:.2f}".format(real, dolar))
#desafio011:faça um programa que leia a largura e a altura de uma parede em metros,calcule a sua area e a quantidade d tinta para pinta-la,sabendo que que cada litro de tita pinta uma area de 2m²:
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {largura*altura}m².')
print(f'Para pintar essa parede, você precisará de {largura*(altura / 2)}L de tinta.')
#desafio012:façaç um algoritimo que leia o preço e mostre seu novo preço com 5% de desconto.
preço = float(input("Qual é o preço do produto? "))
desconto = int(input("Qual o desconto do produto? "))
resultado = preço*desconto/100
print("O desconto será de {}".format(resultado))
#desafio013:faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario,com 15% de almento
n1 = float(input('Digite seu salário R$'))
s = n1 + (n1 * 15 / 100)
print(f'O novo salário será: R${s:.2f}')
#desafio014:: Escreva um programa que converta uma temperatura digitando em graus °c e converta para graus °F.
c = float(input('informe a tempratura em °c:'))
f = ((9 * c) / 5) + 32
print('a temperatura de {}°c corresponde a {}ºf!'.  format(c, f)) 
#desafio015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('quantos dias o carro foi alugado? '))
km = float(input('quantos km rodado? '))
pago = (dias * 60) + (km * 0.15 )
print('o total a pagar e de R$ {:.2f}'.format(pago))
#desafio016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
num = float(input('digite um valor:'))
print('o valor digitado foi {} e a sua porçao inteira e {}'.format(num, int(num)))
#desfio017:Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math 
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adijacente: '))
hi = math.hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))
#desafio018:: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import radians,sin,cos,tan
angulo = foat(input('dgite o angulo que vc deseja: '))
seno = sin(radians(angulo))
print('o angulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('o angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('o angulo de {} tem o tangente de {:.2f}'.format(angulo,tangente))
#desafio019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
n1 = (input('primeiro aluno:'))
n2 = (input('segundo aluno:'))
n3 = (input('rerceiro aluno:'))
n4 = (input('quarto aluno:'))
lista = [n1 ,n2 ,n3 ,n4]
escolhido = choice(lista)
print('o esclhido foi {}'.format(escolhido))
#desafio020:: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
p = input('Digite o nome do 1° aluno: ')
s = input('Digite o nome do 2° aluno: ')
t = input('Digite o nome do 3° aluno: ')
q = input('Digite o nome do 4° aluno: ')
lista = [p, s, t, q]
emb = shuffle(lista)
print('A ordem de apresentação dos alunos é: {}'.format(lista))
#desafio022:   Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas  letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = str(input('digite seu nome completo:')).strip()
print('ananlizando seu seu nome...')
print('seu nome em maiusculas e {}'.format(nome.upper()))
print('seu nome em minusculas e {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('seu primeiro nome tem {}letras'.format(nome.find(' ')))
#desafio023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
num = int(input('informe um numero: '))
n = str(num)
print('analizando o numero {}'.format(num))
print('unidade:{}'.format(n[3]))
print('dezena:{}'.format(n[2]))
print('centena:{}'.format(n[1]))
print('milhar:{}'.format(n[0]))
#desafio024:Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
nome=str(input("Introduza o nome da cidade:")).strip()
print("santo" in nome.lower())
#desafio025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Qual o seu nome? ')).strip()
print('Seu nome possui "SILVA"? {}'.format('SILVA' in nome.upper().split()))
#desafio026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
f = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes nessa frase'.format(f.count('A')))
print('A mesma letra aparece pela primeira vez na posição {}'
      ' e pela última na {}'.format(f.find('A')+1,f.rfind('A')+1))
#desafio027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Qual o seu nome completo? ')
m = nome.split()
print(f'Seu primeiro nome é {m[0]} e seu último nome é {m[-1]}')
#desafio028:Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
pc = random.randint(0, 5)
vc = int(input('Digite um número de 0 a 5:'))
if pc==vc:
    print('Você ganhou!!!')
else:
    print('O PC ganhou!!!')
#desafio029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Qual a velocidade atual do carro?'))
if vel <= 80:
    print('Tenha um bom dia!Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permetido que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format((vel - 80) * 7))
#desafio030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
número = int(input('me diga um número qualquer: '))
if número % 2 == 0:
    print(número,'é par.')
else:
    print(número,'é impar.')
#desafio031:: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = float(input('Qual a distância em (Km) você deseja percorrer? '))
if km <= 200:
    print('Sua passagem vai custar {} reais. '.format(km * 0.5))
else:
    print('Sua passagem vai custar {} reais. '.format(km * 0.45))
#desafio032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import calendar
ano = int(input('Digite o ano: '))
ano6 = calendar.isleap(ano)
if ano6 is True:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')
#desafio033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

print(f'O menor valor digitado foi {min(n1,n2,n3)}')
print(f'O maior valor digitado foi {max(n1,n2,n3)}')
#desafio034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o seu salário: '))
aumentom = (salario * (10/100)) + salario
aumentoM = (salario * (15/100)) + salario

if(salario > 1250):
    print(' Seu salário era R${:.2f} \n Com o aumento, seu salário passa a ser R${:.2f}'.format(salario, aumentom))
else:
    print(' Seu salário era R${:.2f} \n Com o aumento, seu salário passa a ser R${:.2f}'.format(salario, aumentoM))
#desafio035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
l1 = float(input("Digite a medida do lado 1 do triângulo: "))
l2 = float(input("Digite a medida do lado 2 do triângulo: "))
l3 = float(input("Digite a medida do lado 3 do triângulo: "))

if (l1 + l2 > l3) and (l2 + l3 > l1) and (l1 + l3 > l2):
    print("Com esses lados, é possivel formar um triângulo.")
else:
    print("Não é possível formar um triângulo.")




