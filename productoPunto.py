import multiprocessing

def producto(x, y):
	return x * y

def productoPunto(a, b):
	if len(a) != len(b):
		print("Los vectores deben tener la misma longitud")
		return None

	with multiprocessing.Pool() as pool:
		return sum(pool.starmap(producto, zip(a, b)))
	
if __name__ == '__main__':
	N = 5_000_000
	a = [i for i in range(N)]
	b = [i for i in range(N)]
	print(productoPunto(a, b))

	# print(sum([i * j for i, j in zip(a, b)]))