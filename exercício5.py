#Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar: o A
#mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#o A mensagem "Reprovado", se a média for menor do que sete; o A
#mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = float(input('Digite a primeira nota para ser calculada a sua média: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if 10> media >= 7:
    print('Sua média é {}. O aluno foi aprovado.'.format(media))
elif media < 7:
    print('Sua média é {}. O aluno foi reprovado.'.format(media))
elif media == 10:
    print('Sua média é igual a {}. O aluno foi aprovado com distinção!'.format(media))
    
