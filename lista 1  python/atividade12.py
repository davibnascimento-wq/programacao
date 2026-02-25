salario = float(input("digite o salario atual"))
x = salario * 0.15
aumento = salario + x 
imposto = aumento * 0.08
salariofinal = aumento - imposto 
print("o salario sem aumento era: ",salario)
print("o salario coom aumento ficou: ",aumento)
print("o salario final ficou de: ",salariofinal)
