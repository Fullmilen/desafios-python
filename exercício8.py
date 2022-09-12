#Faça um programa que leia um número indeterminado de valores,
#correspondentes a notas, encerrando a entrada de dados quando for
#informado um valor igual a -1 (que não deve ser armazenado). Após esta
#entrada de dados, faça: o Mostre a quantidade de valores que foram lidos;
#o Exiba todos os valores na ordem em que foram informados, um ao
#lado do outro;
#o Exiba todos os valores na ordem inversa à que foram informados, um
#abaixo do outro;
#o Calcule e mostre a soma dos valores; o Calcule e mostre a média dos
#valores;
#o Calcule e mostre a quantidade de valores acima da média calculada;
#o Calcule e mostre a quantidade de valores abaixo de sete; o Encerre o
#programa com uma mensagem;

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
