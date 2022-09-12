#As Organizações Tabajara resolveram dar um aumento de salário aos seus
#colaboradores e lhe contraram para desenvolver o programa que calculará os
#reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste
#segundo o seguinte critério, baseado no salário atual:
#o salários até R$ 280,00 (incluindo) : aumento de 20% o salários entre R$
#280,00 e R$ 700,00 : aumento de 15% o salários entre R$ 700,00 e R$
#1500,00 : aumento de 10% o salários de R$ 1500,00 em diante : aumento
#de 5% Após o aumento ser realizado, informe na tela: o o salário antes do
#reajuste; o o percentual de aumento aplicado; o o valor do aumento; o o
#novo salário, após o aumento.

salario = float(input('Informe o seu salário para ser calculado o reajuste: '))
au1 = (salario * 20) / 100
au2 = (salario * 15) / 100
au3 = (salario * 10) / 100
au4 = (salario * 5) / 100

if salario <=280:
    print('Seu salário é de R${} \nApós o reajuste de 20% (R${}) ficará R${}'.format(salario, au1, (salario+au1)))
elif 280 < salario <= 700:
    print('Seu salário é de R${} \nApós o reajuste de 15% (R${}), ficará R${}'.format(salario, au2, (salario+au2)))
elif 700 < salario <= 1500:
    print('Seu salário é de R${} \nApós o reajuste de 10% (R${}), ficará R${}'.format(salario, au3,  (salario+au3)))
elif 1500 < salario:
    print('Seu salário é de R${} \nApós o reajuste de 5% (R${}), ficará R${}'.format(salario, au4, (salario+au4)))
