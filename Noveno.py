#!/usr/bin/env python3
import sys

def fib_sequence(n):
	a, b = 0, 1
	seq = []
	for _ in range(n):
		seq.append(a)
		a, b = b, a + b
	return seq

def main():
	if len(sys.argv) > 1:
		try:
			n = int(sys.argv[1])
		except ValueError:
			print("Argumento inválido. Use: python Noveno.py <n> o ingrese n en la entrada.")
			return
	else:
		try:
			n = int(input("Ingrese el número de términos (entero >= 1): ").strip())
		except ValueError:
			print("Entrada inválida. Se requiere un entero.")
			return

	if n < 1:
		print("Se requiere un entero mayor o igual a 1.")
		return

	seq = fib_sequence(n)
	print(f"Secuencia de Fibonacci ({n} términos):")
	print(", ".join(str(x) for x in seq))

if __name__ == "__main__":
	main()

