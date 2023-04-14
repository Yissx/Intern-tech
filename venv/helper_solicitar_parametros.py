def solicitar_k():
    while True:
        print("Introducir k")
        k = input()
        longitud_k = len(k)
        if k.isdigit() and longitud_k >= 0 and longitud_k <= 100000:
            return int(k)
        print("k debe ser numérico. Se debe cumplir 0 <= k <= 10^5")

def solicitar_parámetros():
    while True:
        print("Introduzca una cadena numérica s")
        palindromo = input()
        n = len(palindromo)
        if palindromo.isdigit() and n > 0 and n <= 100000:
            k = solicitar_k()
            return palindromo, k, n
        print("s debe consistir de solo números, además su longitud (n) debe cumplir con  0 < n <= 10^5")