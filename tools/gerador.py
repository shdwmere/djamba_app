import random



for _ in range(2):
    onze_chars = random.randint(11111111111, 99999999999)
    doze_chars = random.randint(111111111111, 999999999999)

    id_pedido = '#' + str(onze_chars)
    codigo_rastreio = 'BR' + str(doze_chars)

    # Imprima os valores para cada repetição
    print('Código de rastreio: \033[4;32m{}\033[0m'.format(codigo_rastreio))
    #print('ID do pedido: \033[4;32m{}\033[0m'.format(id_pedido))