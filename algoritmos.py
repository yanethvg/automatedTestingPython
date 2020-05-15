"""
>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120

>>> recursivo.factorial(3)
6
"""

def fibonacci(number):
	if number == 0: return 0
	elif number == 1: return 1
	else: return fibonacci(number - 1) + fibonacci(number - 2)


def palindromo(sentece):
	""" Retorna verdadero si el parametro es un palindromo
	en caso contrario retorna falso

	sentence -->puede ser un String o un entero

	>>> palindromo("anita lava la tina")
	True

	>>> palindromo(12321)
	True

	>>> palindromo("CodigoFacilito")
	False
	"""
	sentence = str(sentece).lower().replace(" ","")
	return sentence == sentence[::-1]

class Recursivo:
	def factorial(self, number):
		if number == 0: return 1
		else: return number * self.factorial(number - 1)



if __name__ == '__main__':
	import doctest
	doctest.testmod()
	#para ejecutar pruebas de otro archivo
	doctest.testfile("testalg.txt")