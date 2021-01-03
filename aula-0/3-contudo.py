# Operadores de Identidade, is, is not

x = ["a", "b"]
y = ["a", "b"]

print(x is y) # retorna false, pois não é o mesmo objeto

z = y

print(z is y) # retorna true, pois é o mesmo objeto