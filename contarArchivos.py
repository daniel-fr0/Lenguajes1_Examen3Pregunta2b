import os
import threading

contador = 0

def contarArchivos(path):
	global contador

	if not os.path.exists(path):
		return contador

	for item in os.listdir(path):
		threads = []
		subPath = os.path.join(path, item)
		if os.path.isfile(subPath):
			contador += 1
		elif os.path.isdir(subPath):
			thread = threading.Thread(target=contarArchivos, args=(subPath,))
			thread.start()
			threads.append(thread)

	for thread in threads:
		thread.join()

	return contador

if __name__ == '__main__':
	print('Archivos encontrados:', contarArchivos('dir'))