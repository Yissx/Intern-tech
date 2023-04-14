# Intern-tech
Problema que obtiene el mayor palíndromo dada una cadena de números y un número determinado de movimientos posibles sobre esta

Elegí este problema porque fue el que me hizo sentir más familiar / cómoda, pues los problemas que suelo resolver más fácilmente se adaptan mejor a una solución lineal y sin necesidad de manejar estructuras de datos más complejas, como un árbol o grafo.

¿Cómo resolví el problema?:
*** Dados n, k, s.
1. Determinar si la longitud de la cadena s es par o impar.
    1.1 Con base en lo anterior se obtienen dos subcadenas (inicio y final) que corresponden a la cadena s dividida a la mitad.
    1.2 En caso de ser de longitud impar, se asigna a una variable el valor de la cadena s que se encuentra justo a la mitad y las sublistas inicio y final corresponderían entonces a los extremos sobrantes de la lista.
2. Definir variables auxiliares.
    2.1 cadena_nueva[] = estructura en donde se almacenará elemento a elemento el posible palíndromo
    2.2 cambios_hechos = cuántas veces no ha coincido un valor de la sublista inicio con la sublista final (es para cersiorarnos de no realizar más cambios en la cadena s de los permitidos).
3. Obtener un palíndromo:
    3.1 Recorrer las sublistas inicio (de derecha a izquierda) y final (izquierda a derecha) para comparar los elementos que se suponen deben ser iguales.
    3.2 Si el valor de algún elemento de la sublista inicio es diferente al elemento de la sublista final (siendo que estos tienen que ser iguales para cumplirse la condición de palíndromo):
          3.2.1 Se selecciona el elemento de mayor valor y se agrega a la nueva_cadena
          3.2.2 cambios_hechos se incrementa en 1 
    3.3 Si los elementos son iguales no es necesario realizar ningún cambio en cambios_hechos y a la nueva_cadena se le agrega el elemento sin modificaciones.
    *** El punto 3 se realiza mientras los cambios_hechos no superen el valor k y las subcadenas no hayan sido recorridas por completo.
4. Tal vez el punto 3 fue interrumpido porque ya se realizó la cantidad de cambios permitidos, pero eso no significa que un palíndromo no pueda ser formado ya, por lo que se siguen comparando elemento a elemento las dos sublistas, pero esta vez sin tolerancia: si hay alguna diferencia se determina inmediatamente que no existe solución; en caso contrario a nueva_cadena se le agrega el resto de elementos de la sublista inicio.
5. El punto 3 fue interrumpido porque las sublistas fueron recorridos en su totalidad. Ahora se intentará (con la cantidad de cambios que aún hay disponibles) incrementar el valor del palíndromo formado:
    5.1 Con ayuda de la cadena s se determina si un elemento de la nueva_cadena fue modificado o no en el paso 3.2.1
    5.2 Si lo fue, este elemento cambia su valor a 9 y cambios_hechos se incrementa en 1. 
    *** En caso contrario, y de ser posible, se cambia a 9 y cambios_hechos se incrementa en 2.
6. Finalmente:
    6.1 Se agrega a cadena_nueva el elemento que corresponde al valor de enmedio de la cadena s (en caso de existir).
    6.2 Si quedan cambios disponibles este elemento cambia su valor por 9.
    6.3 A cadena_nueva se le concatena cadena_nueva.reversa, pero sin el último valor agregado (valor de enmedio).
