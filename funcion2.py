# Crear una función que se llame reemplazarCaracteres que reciba 
# una cadena de caracteres como primer parámetro, 
# un carácter como segundo y otro carácter  como tercero,  
# la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero 
# y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena

def reemplazarCaracteres(cadena:str, primer_caracter:str, segundo_caracter:str):
    cant_remplazos = cadena.count(primer_caracter)
    remplazo = cadena.replace(primer_caracter, segundo_caracter)
    print(remplazo)
    print(cant_remplazos)


reemplazarCaracteres("hola","o","u")
