preco = float(input('Qual o preço do produto?\nR$'))
desc = int(input('Qual a porcentagem de desconto?\n> '))
pdesc = preco - ((preco * desc) / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}'.format(preco, desc, pdesc))