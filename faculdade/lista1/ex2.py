#Dado um ano d.C. (depois de Cristo), identifique se este é um ano bissexto ou não. Considere que, para o ano ser bissexto, basta que seja divisível por 400. Caso não seja, este precisará ser divisível por 4 e não ser divisível por 100.

ano = int(input('Ano:\n> '))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))