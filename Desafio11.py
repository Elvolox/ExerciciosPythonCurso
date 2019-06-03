base   = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))

area = base*altura
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².".format(base,altura,area))

tinta = area/2
print("Para pintar esssa parede, você precisará de {}l de tinta.".format(tinta))