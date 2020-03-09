
import sys
def add(x, y):
	return x+y

if __name__=="__main__":
	if ( len(sys.argv) > 3 ):
		print ("Erreur! Entrez que 2 valeurs")
	elif ( len(sys.argv) == 1 ):
		print ("Error! Entrez deux valeurs")
		x = input("premier valeur: ")
		y = input("deuxieme valeur: ")
		x = int(x)
		y = int(y)
		print( add(x, y) )
	elif ( len(sys.argv) == 2 ):
		print ("Erreur! Entrez encore une valeur")
		y = input("deuxieme valeur: ")
		x = int( sys.argv[1] )
		y = int(y)
		print( add(x, y) )
	else:
		x = int( sys.argv[1] )
		y = int( sys.argv[2] )
		print( add(x, y) )


