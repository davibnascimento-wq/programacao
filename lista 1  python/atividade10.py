
x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))

diferença_x = x2 - x1
diferença_y = x2 - y1

distancia = ((diferença_x ** 2) + (diferença_y ** 2)) **0.5

print(f"A distância entre os pontos é: {distancia:.2f}")