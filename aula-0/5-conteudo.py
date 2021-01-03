# Dicionários, são mutáveis

lista = {
	"sorvete": 5, 
	"chocolate": 3,
	"creme": 1,
	"outros": ["creme dental", "sabão", "caixa"]
}

#acessa a chave "sorvete"
print(lista["sorvete"]) 

lista2 = {
	"nome": "Vitor",
	"sobrenome": "Oliveira",
	"cego": False,
	"parentes": ["Roberto", "Paula", "Fernando"]
}

# Altera a chave "cego" para true
# lista2["cego"] = True

# Exclui a chave "cego"
# lista2.pop("cego")

# Exlcui a chave "parentes"
# del lista2["parentes"]

# Limpa o dicionário
# lista2.clear()

# Retorna uma lista com as tuplas, contento a chave e o valor
#lista2.items() # retorna [ ('nome', 'Vitor'), ('sobrenome', 'Oliveira'), ('cego', False), ('parentes', ['Roberto', 'Paula', 'Fernando']) ]

# Pega todas as chaves do dicionário
# print(lista2.keys())

# Pega todos os valores do dicionário
# print(lista2.values())
