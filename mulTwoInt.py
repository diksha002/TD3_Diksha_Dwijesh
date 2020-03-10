import sys
def mul(a,b):
    multiply= a * b
    return multiply

if __name__=="__main__":
	if ( len(sys.argv) > 3 ):
		print ("Erreur! Entrez que deux valeurs")
	elif ( len(sys.argv) == 1 ):
		print ("Erreur! Entrez deux valeurs")
		a = input("premier valeur: ")
		b = input("deuxieme valeur: ")
		a = int(a)
		b = int(b)
		print ( mul(a,b) )
	elif ( len(sys.argv) == 2 ):
		print ("Erreur! Entrez encore une valeur")
		y = input("entrez la deuxieme valeur: ")
		x = int( sys.argv[1] )
		y = int(y)
		print ( mul(a,b) )
	else:
		x = int( sys.argv[1] )
		y = int( sys.argv[2] )
		print ( mul(a,b) )
