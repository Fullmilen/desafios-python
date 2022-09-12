nome: str = input('Informe o seu nome: ')
h = float(input('informe aqui a sua altura para ser calculado o seu peso ideal: '))
gen = input('informe o seu gênero, digitando (M) para masculino e (F) para feminino: ')
pesoM = float((72.7 * h) - 58)
pesoF = float((62.1 * h) - 44.7)
if gen == 'M':
    print('{},sua altura é {}, sendo homem, seu peso ideal é {:.2f}! '.format(nome, h, pesoM))
elif gen == 'F':
    print('{}, sua altura é {:.2f}, sendo mulher, seu peso ideal será {:.2f}!'.format(nome, h, pesoF))
