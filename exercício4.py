#Faça um Programa que pergunte quanto você ganha por hora e o número de
#horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
#mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8%
#para o INSS e 5% para o sindicato, faça um programa que nos dê:
#• salário bruto.
#• quanto pagou ao INSS.
#• quanto pagou ao sindicato.
#• o salário líquido.
#• calcule os descontos e o salário líquido, conforme a tabela abaixo:
#o IR (11%) : R$ o INSS
#(8%) : R$ o Sindicato (
#5%) : R$ o Salário
#Líquido : R$

gh = float(input('Digite o quanto você ganha por hora: R$'))
ht = int(input('Quantas horas você trabalha por mês?: '))
total = gh * ht
imp = (total*11)/100
inss = (total*8)/100
sindi = (total*5)/100
descont = imp+inss+sindi
liqui = total-descont
print('O seu salário bruto (sem descontos) é de: R${:.2f}'.format(total))
print('Você pagará R${:.2f} ao INSS.'.format(inss))
print('Você pagará R${:.2f} ao sindicato.'.format(sindi))
print('Seu salário líquido será de R${:.2f}'.format(liqui))
