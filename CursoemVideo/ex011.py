largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
lxa = largura * altura
print('Sua parede tem dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, lxa))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(lxa / 2))
