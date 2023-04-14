def solicitar_n_k():
    while True:
        n, k = input("Introducir n, k ").split(" ")
        if k.isdigit() and int(k) >= 0 and int(k) <= 100000 and int(n) > 0 and int(n) < 100000:
            return int(n), int(k)
        print("k y n deben ser numéricos. Se debe cumplir 0 <= k, n <= 10^5")
        print("Nota introducir n, seguido de un espacio y k")

def solicitar_s(n):
    while True:
        palindromo = input(f"Introduzca una cadena numérica s de tamaño {n} ")
        if int(n) == len(palindromo):
            return  palindromo

def solicitar_parámetros():
    n, k = solicitar_n_k()
    s = solicitar_s(n)
    return n, k, s