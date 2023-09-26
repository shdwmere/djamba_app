import random

onze_chars = random.randint(11111111111, 99999999999)
doze_chars = random.randint(111111111111, 999999999999)

id_pedido = '#' + str(onze_chars)
codigo_rastreio = 'BR' + str(doze_chars)

print('ID do pedido: \033[4;32m{}\033[0m'.format(id_pedido))
print('Código de rastreio: \033[4;32m{}\033[0m'.format(codigo_rastreio))