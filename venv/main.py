from helper_solicitar_parametros import solicitar_parámetros
n, k, s = solicitar_parámetros()

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
    cambios_hechos = 0
    digito = 0
    nueva_cadena = []
    longitud = len(inicio)
    #Convertir a palíndromo
    while cambios_hechos < k and digito < longitud:
        if inicio[digito] != final[digito]:
            if inicio[digito] < final[digito]:
                nueva_cadena.append(final[digito])
            else:
                nueva_cadena.append(inicio[digito])
            cambios_hechos += 1
        else:
            nueva_cadena.append(inicio[digito])
        digito += 1
    print(nueva_cadena)
    if digito < longitud:   #No terminó de recorrerse el string
        while digito < longitud:
            if inicio[digito] != final[digito]:
                return -1
            else:
                nueva_cadena.append(inicio[digito])
            digito += 1
    elif cambios_hechos < k: #Ya es un palíndromo pero aún se pueden hacer cambios
        digito = 0
        while digito < len(inicio) and cambios_hechos < k:
            if int(nueva_cadena[digito]) < 9: #Si se puede cambiar
                if s[digito] != s[n-digito-1]: #Hubo un cambio en alguno de los dos dígitos
                    nueva_cadena[digito] = '9'
                    cambios_hechos += 1
                elif s[digito] == s[n-digito-1] and k - cambios_hechos >= 2: #No se había cambiado algún dígito, ya eran iguales
                    nueva_cadena[digito] = '9'
                    cambios_hechos += 2
            digito += 1
    nueva_cadena += nueva_cadena[::-1]
    if medio is not None:
        if cambios_hechos < k: #Si queda un cambio para el valor de enmedio
            medio = '9'
        nueva_cadena.insert(round((n - 1) / 2), medio)
    nueva_cadena = "".join(nueva_cadena)
    return nueva_cadena

print(highestValuePalindrome(len(s), k, s))