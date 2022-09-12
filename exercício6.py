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
