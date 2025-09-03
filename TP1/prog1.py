import fonctions as f
print("Hello, World!")

while True:
	samy = input("entrez le premier nombre")
	raoul =input("entrez le deuxième nombre")
	samy, raoul= int(samy), int(raoul)
	res = (f.puissance(samy, raoul))
	print (res)

else:
	print("utilisez des nombre réel jeune homme")
