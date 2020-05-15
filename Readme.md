# Comando para ejecutar Doctest
```
	python -m doctest nombre.extension
```

# Comando para ver mas detalle Doctest
```
	python -m doctest -v nombre.py
```
# Para evitar el comando doctest 

Se puede agregar esta validacion en el archivo

```
	if __name__ == '__main__':
		import doctest
		doctest.testmod()
```

Despues solo ejecutar
```
	python nombre.py
```

Siempre para poder ver mas información

```
	python algoritmos.py -v
```