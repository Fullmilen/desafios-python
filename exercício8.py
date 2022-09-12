lida = 0
notaslidas = []
while lida != -1:
    lida = float(input('Digite uma nota a ser lida, caso queira encerrar, digite -1: '))
    if lida != -1:
        notaslidas.append(lida)
        print('a) Quantidade de valores que foram lidos: ', len(notaslidas))
#Valores ordem que foram informados, lado a lado
print('b) valores na ordem em que foram informados, lado a lado: ',notaslidas)
for nota in notaslidas:
    print(nota, end='')
#ordem inversa, um embaixo do outro
print('\nc) Ordem inversa: Um abaixo do outro: ')
for indice in range(len(notaslidas) -1, -1, -1) :
    print(notaslidas[indice])
#soma dos valores:
print('d) Soma dos valores:', sum(notaslidas))
#média:
soma = sum(notaslidas)
media = soma/len(notaslidas)
print('e) A média dos valores: {}'.format(media))
#valores acima da média:
print('f) Quantidade de valores acima da média:\n', end='')
acimedia = 0
int (acimedia)
for nota in notaslidas:
    if nota > media:
        acimedia +=1
        print(acimedia)
#valores abaixo de sete:
print('g) Quantidade de valores abaixo de sete:\n', end='')
abaixo7 = 0
for nota in notaslidas:
    if nota < 7:
        abaixo7 +=1
    print(abaixo7)
print('programa encerrado!')