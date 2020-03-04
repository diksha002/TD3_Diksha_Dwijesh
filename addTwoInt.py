import sys
def add(x,y):
	return x+y

if __name__=="__main__":
	if (len(sys.argv) > 3):
		print("Error! Affichez que 2 variables")
	elif (len(sys.argv) < 3):
		print("Error! Affichez 2 variables")
	else:
		x =int( sys.argv[1] )
		y =int( sys.argv[2] )
		print(add(x,y))
