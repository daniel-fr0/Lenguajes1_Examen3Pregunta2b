import time
import multiprocessing

def productoPunto(a, b):
	return sum([i * j for i, j in zip(a, b)])

def productoPuntoConcurrente(a, b):
	if len(a) != len(b):
		print("Los vectores deben tener la misma longitud")
		return None
	
	chunks = multiprocessing.cpu_count()
	chunkSize = len(a) // chunks

	with multiprocessing.Pool(processes = chunks) as pool:
		result = pool.starmap(productoPunto, [(a[i:i + chunkSize], b[i:i + chunkSize]) for i in range(0, len(a), chunkSize)])
		return sum(result)

	
if __name__ == '__main__':
	N = 5_000_000
	a = [i for i in range(N)]
	b = [i for i in range(N)]

	start = time.time()
	productoPuntoConcurrente(a, b)
	end = time.time()
	print("Concurrente:\t", end - start)

	start = time.time()
	productoPunto(a, b)
	end = time.time()
	print("No concurrente:\t", end - start)