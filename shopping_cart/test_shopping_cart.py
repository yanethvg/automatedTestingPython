import unittest
from shopping_cart import Item, ShoppingCart

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
		self.assertEqual(self.jugo.name,"Jugo")

	def test_contiene_productos(self):
		self.assertTrue(self.shopping_cart.contains_items())

	def test_no_contiene_productos(self):
		self.shopping_cart.remove_item(self.pan)
		self.assertFalse(self.shopping_cart.contains_items())

if __name__ == '__main__':
	unittest.main()