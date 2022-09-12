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
