from random import randrange 
compteur = 0
nombrealeatoire = randrange(150)
choixutil= -1
while choixutil != nombrealeatoire : 
	choixutil = int(input("choisi un nombre entre 0 et 150\n"))
	compteur = compteur+1 
	if nombrealeatoire == choixutil :
		print("gg tu as trouver en ", compteur)
	elif nombrealeatoire > choixutil :
		print("plus grand")
	else:
		print("moins grand")
