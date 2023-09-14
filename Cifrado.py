cifrado = {
    'A': 'R', 'B': 'T', 'C': 'Q', 'D': 'W', 'E': 'Z',
    'F': 'U', 'G': 'O', 'H': 'S', 'I': 'N', 'J': 'Y',
    'K': 'P', 'L': 'X', 'M': 'V', 'N': 'A', 'O': 'C',
    'P': 'E', 'Q': 'D', 'R': 'B', 'S': 'H', 'T': 'M',
    'U': 'K', 'V': 'I', 'W': 'F', 'X': 'L', 'Y': 'G',
    'Z': 'J',
    'a': 'r', 'b': 't', 'c': 'q', 'd': 'w', 'e': 'z',
    'f': 'u', 'g': 'o', 'h': 's', 'i': 'n', 'j': 'y',
    'k': 'p', 'l': 'x', 'm': 'v', 'n': 'a', 'o': 'c',
    'p': 'e', 'q': 'd', 'r': 'b', 's': 'h', 't': 'm',
    'u': 'k', 'v': 'i', 'w': 'f', 'x': 'l', 'y': 'g',
    'z': 'j',
    '0': '5', '1': '6', '2': '7', '3': '8', '4': '9',
    '5': '0', '6': '1', '7': '2', '8': '3', '9': '4',
    '!': '@', '@': '#', '#': '$', '$': '%', '%': '&',
    '&': '*', '*': '!', ':': ';', ';': '.', '.': ',', 
    ',': '?', '?': '!'
}
opc = 's'
while opc == 's':
    print("¿Qué desea hacer?")
    print("1.- Cifrar")
    print("2.- Descifrar")
    opt = input("Seleccione una opción: ")

    if opt == '1':
        cadena = input("Inserta la cadena: ")

        cadena_cifrada = ''.join(cifrado.get(letra, letra) for letra in cadena)

        cadena_binaria = ' '.join(format(ord(letra), '08b') for letra in cadena_cifrada)
        print(f"Cadena original: {cadena}")
        print(f"Cadena cifrada: {cadena_cifrada}")
        print(f"Cadena cifrada binaria: {cadena_binaria}")
    elif opt == '2':
        cadena_binaria_cifrada = input("Ingrese la cadena binaria cifrada: ")

        cadena_cifrada = ''.join(chr(int(binario, 2)) for binario in cadena_binaria_cifrada.split())

        cifrado_inverso = {valor: clave for clave, valor in cifrado.items()}

        cadena_descifrada = ''.join(cifrado_inverso.get(letra, letra) for letra in cadena_cifrada)
        print(f"Cadena cifrada: {cadena_descifrada}")
    else:
        print("Valor no válido")
    opc = input("¿Desea continuar? (s/n): ").lower()
