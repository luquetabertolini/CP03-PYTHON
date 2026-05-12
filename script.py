temperaturas = [[28, 31, 34, 33],
                [25, 27, 29, 28],
                [32, 35, 36, 34],
                [24, 26, 25, 27]]

sala_mais_critica = 0
num_sala = 1
max_criticos = 0

for sala in range(len(temperaturas)):
    print(f" Sala: {sala}")

    soma = 0
    qtd_criticos = 0
    for temp in temperaturas[sala]:
       soma += temp
       if temp >= 33:
           qtd_criticos += 1



    print(f' Media: {soma / 4}')
    print(f" Registros críticos {qtd_criticos}\n")

    if qtd_criticos > max_criticos:
        max_criticos = qtd_criticos
        sala_mais_critica = num_sala
    num_sala +=1
print(f" Sala com mais registros críticos: {sala_mais_critica}")

