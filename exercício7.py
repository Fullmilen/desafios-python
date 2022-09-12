#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
#número inteiro entre 1 a 10. O usuário deve informar de qual número ele
#deseja ver a tabuada.

val = int(input('Digite um valor: '))

for count in range (10):
    print('{} X {} = {}'.format(val, count+1, val*(count+1)))


