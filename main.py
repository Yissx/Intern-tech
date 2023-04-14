from helper_solicitar_parametros import solicitar_parámetros

s, k, n = solicitar_parámetros()

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def contar_diferencias():
    return

def highestValuePalindrome(n, k, s):
    #Dividir a la mitad la cadena
    if n % 2 == 0:
        inicio = s[:round(n/2)]
        medio = None
    else:
        inicio = s[:round((n-1)/2)]
        medio = s[round(n/2) - 1]
    final = s[round(n/2):n]
    final = final[::-1]
    #Variables
    cambios_extra = k - (n / 2)
    cambios_hechos = 0
    digito = 0
    nueva_cadena = []
    #Empieza a haber cambios
    while cambios_hechos < k and digito < len(inicio):
        i = int(inicio[digito])
        f = int(final[digito])
        if i != f:
            if i < f:
                nueva_cadena.append(str(f))
            else:
                nueva_cadena.append(str(i))
            cambios_hechos += 1
        else:
            nueva_cadena.append(str(i))
        digito += 1
    #nueva_cadena = "".join(nueva_cadena)
    if digito < n / 2:   #No terminó de recorrerse el string
        while digito < len(inicio):
            i = inicio[digito]
            f = final[digito]
            if i != f:
                return -1
            digito += 1
        """camb = nueva_cadena
        nueva_cadena += s[digito:round(n/2)] #Completo la mitad de la cadena
        nueva_cadena += s[round(n/2):n-digito]
        nueva_cadena += camb[::-1] #Completo la parte final"""
    elif cambios_hechos < k: #Ya es un palíndromo pero aún se pueden hacer cambios
        digito = 0
        print(nueva_cadena, digito, cambios_hechos)
        while digito < len(inicio) and cambios_hechos < k:
            if int(nueva_cadena[digito]) < 9: #Si se puede cambiar
                if s[digito] != s[n-digito-1]: #Hubo un cambio en alguno de los dos dígitos
                    nueva_cadena[digito] = '9'
                    cambios_hechos += 1
                elif s[digito] == s[n-digito-1] and k - cambios_hechos >= 2: #No se había cambiado algún dígito, ya eran iguales
                    nueva_cadena[digito] = '9'
                    cambios_hechos += 2
            digito += 1
        print(nueva_cadena)
    nueva_cadena += nueva_cadena[::-1]
    nueva_cadena = "".join(nueva_cadena)
    return nueva_cadena

print(highestValuePalindrome(len(s), k, s))