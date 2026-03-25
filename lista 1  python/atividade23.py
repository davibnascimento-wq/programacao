altura_pessoa = float(input("digite a altura do objeto conhecido"))
sombra_pessoa = float(input("digita o comprimento da sua sombra"))
sombra_predio = float(input("Digite a sombra do predio"))
altura_predio = (altura_pessoa / sombra_pessoa) * sombra_predio
print ("A altura do predio é", altura_predio) 