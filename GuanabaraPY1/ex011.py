larg = float(input('Largura da parade: '))
alt = float(input('Altura da parede: '))
area = larg * alt
litros = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(litros))