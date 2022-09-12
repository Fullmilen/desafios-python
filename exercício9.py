salarios = [200, 250, 320, 413, 516, 680, 791, 877, 999, 1000, 2000, 3000]
contagemsala = [0] * 9
for salario in salarios:
    indice = salario // 100 -2
    indicemax = len(contagemsala) - 1
    indice = min(indice, indicemax)
contagemsala[indice] += 1
print(contagemsala)