import sys
from addTwoInt import add

if __name__=="__main__":
	print("Voulez vous additionner deux valeurs?")
	print("Inserez oui ou non")
	a = input()
	if (a == "oui"):
			if ( len(sys.argv) > 3 ):
				print("Erreur! Entrez que deux valeurs!")
			elif ( len(sys.argv) == 1 ):
				print("Erreur! Entrez deux valeurs ")
				x = int(input("premier valeur: "))
				y = int(input("deuxieme valeur: "))
				print(add(x,y))
			elif ( len(sys.argv) == 2):
				print("Erreur! Entrez encore une valeur")
				y = int(input("deuxieme valeur: "))
				x = int( sys.argv[1] )
				print(add(x,y))
			else:
				x = int( sys.argv[1] )
				y = int( sys.argv[2] )
				print(add(x,y))
	else:
		print("fin du programme")
