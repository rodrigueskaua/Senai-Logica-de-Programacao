def fatorial(n):
	fat = 1
	for i in range(2, n+1):
		fat = fat * i
	return fat

def potencia(base, expoente):
	potencia = 1
	for i in range(1, expoente+1):
		potencia = potencia * base
	return potencia
