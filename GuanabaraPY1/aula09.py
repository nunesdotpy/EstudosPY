frase = "   Aprenda Python  "
print(frase.strip()) # Remove todos os espaços INUTEIS
print(frase.rstrip()) # Remove somente os espaços do final - RIGHT
print(frase.lstrip()) # Remove somente os espaços do inicio - LEFT
frase = "Curso em Video Python"
print(frase[9::3])
print(len(frase)) # Mostrar tamanho da frase
print(frase.count('o')) # Conta quantas vezes a letra O aparece
print(frase.count('o',0,13)) # Conta quantas vezes a letra O aparece apartir da posição 0 até a 12
print(frase.find('deo')) # Encontra e mostra em que posição a frase começa
print(frase.find('Android')) # Se a palavra nao existir na frase, ele retorna o valor -1
print('Curso' in frase) # Se existir, retorna true, se não retorna false
print(frase.replace('Python', 'Android')) # trocar a palavra Python por Android
print(frase.upper()) # Deixa todas as letras em CAPS
print(frase.lower()) # Deixa todas as letras em minusculo
print(frase.capitalize()) # Vai capitalizar a primeira letra apenas
print(frase.title()) # Vai capitalizar todo inicio de palavra
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.split()) # Divide todas as palavras, cria novas indexações e cria uma lista com elas
frase = frase.split()
print('-'.join(frase)) # Junta todas as palavras splitadas com o caracter desejado, nesse caso '-'

