real = float(input('Quanto de dinheiro tens na carteira? R$'))
dolar = real / 4.81
euro = real / 5.15
libra = real / 6.04
iene = real / 0.38
print(f'Com R$ {real} você pode comprar US$ {dolar:.2f}')
print(f'Com R$ {real} você pode comprar € {euro:.2f}')
print(f'Com R$ {real} você pode comprar £ {libra:.2f}')
print(f'Com R$ {real} você pode comprar ¥ {iene:.2f}')
