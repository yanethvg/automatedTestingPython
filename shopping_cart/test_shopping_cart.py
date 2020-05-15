import unittest
from shopping_cart import Item, ShoppingCart,NotExistsItemError

class TestShoppingCart(unittest.TestCase):
	#realizar acciones antes de realizar la prueba unitaria

	#conectarse a una base de datos, consumir una api, leer variables de entorno,escribir sobre un archivo

	#metodo que se ejecuta antes de cada una de las pruebas
	def setUp(self):
		#print("Método setUp antes de la prueba")
		self.pan = Item("Pan",7.0)
		self.jugo = Item("Jugo",5.0)

		self.shopping_cart = ShoppingCart()
		self.shopping_cart.add_item(self.pan)

	#metodo que se ejecuta despues de cada una de las pruebas unitarias
	def tearDown(self):
		#print("Método tearDown despues de la prueba")
		pass

	# a cada prueba le corresponde un mensaje de setUp y tearDown
	def test_cinco_mas_cinco_igual_diez(self):
		assert 5 + 5 == 10

	"""def test_nombre_producto_igual_manzana(self):
		item = Item("Manzana",12.0)
		self.assertEqual(item.name,"Manzana")

	def test_nombre_producto_diferente_manzana(self):
		item = Item("Pan Blanco",15.0)
		self.assertNotEqual(item.name,"Manzana")
	"""
	def test_nombre_producto_igual_pan(self):
		self.assertEqual(self.pan.name,"Pan")

	def test_nombre_producto_igual_jugo(self):
		#compara dos valores
		self.assertEqual(self.jugo.name,"Jugo") # == 

	def test_contiene_productos(self):
		self.assertTrue(self.shopping_cart.contains_items())

	def test_no_contiene_productos(self):
		self.shopping_cart.remove_item(self.pan)
		self.assertFalse(self.shopping_cart.contains_items())

	#comprobar si dos objetos son el mismo
	def test_obtener_producto_pan(self):
		item = self.shopping_cart.get_item(self.pan)
		# se puede utilizar dos en una misma funcion
		#compara dos objetos 
		# se puede colocar mas de un assert
		self.assertIs(item,self.pan) # is evaluamos un objeto
		self.assertIsNot(item,self.jugo)

	def test_exception_al_obtener_jugo(self):
		# con with y assertRaises se puede agregar la excepcion creada
		with self.assertRaises(NotExistsItemError):
			item = self.shopping_cart.get_item(self.jugo)

	def test_total_con_un_producto(self):
		total = self.shopping_cart.total()
		# sea mayor
		self.assertGreater(total,0)
		# sea menor
		self.assertLess(total,self.pan.price + 1.0)
		# es igual a lo que debe de ser
		self.assertEqual(total, self.pan.price)

	def test_codigo_pan(self):
		# revisa si contiene el nombre del producto
		#self.assertRegex(self.pan.code(),self.pan.name) este python 3.7 
		self.assertRegexpMatches(self.pan.code(),self.pan.name) #python 2.7

	#validar de forma manual utilizando el metodo fail
	def test_fail(self):
		if 2 > 3:
			self.fail("Dos no es mayor a tres!")
	"""
	salida si falla
		....F.....
	======================================================================
	FAIL: test_fail (__main__.TestShoppingCart)
	----------------------------------------------------------------------
	Traceback (most recent call last):
	  File "shopping_cart/test_shopping_cart.py", line 79, in test_fail
	    self.fail("Dos no es mayor a tres")
	AssertionError: Dos no es mayor a tres

	----------------------------------------------------------------------
	Ran 10 tests in 0.004s

	FAILED (failures=1)
	"""

	#saltar una prueba para que no se ocupe
	#desarrollador conoce
	@unittest.skip("Colocamos nuestros motivos")
	def test_prueba_skip(self):
		pass
	"""
	.........s.
	----------------------------------------------------------------------
	Ran 11 tests in 0.003s

	OK (skipped=1)
	para tener mas informacion colocar al final la bandera -v
	"""
	#cuando el desarrollador desconoce puede o no puede ejecutarse
	#True la prueba se salta False la prueba se ejecuta
	#@unittest.skipIf(True,"Colocamos nuestros motivos")
	#evaluando a falso si es false no se ejecuta si es True no se salta
	@unittest.skipUnless(False,"Colocamos nuestros motivos")
	def test_prueba_skip2(self):
		pass


if __name__ == '__main__':
	unittest.main()