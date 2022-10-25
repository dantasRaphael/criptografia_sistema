

def display_msg():
    texto = ""

def cripto(frase) :
    tradutor = ""
    for letra in frase:
        if letra in "Aa": tradutor = tradutor + "@"
        elif letra in "Bb": tradutor = tradutor + "%"
        elif letra in "Cc": tradutor = tradutor + "!"
        elif letra in "Dd": tradutor = tradutor + "*"
        elif letra in "Ee": tradutor = tradutor + "?"
        elif letra in "Ff": tradutor = tradutor + "/"
        elif letra in "Ge": tradutor = tradutor + "+"
        elif letra in "Hh": tradutor = tradutor + ";"
        elif letra in "Ii": tradutor = tradutor + "7"
        elif letra in "Jj": tradutor = tradutor + "8"
        elif letra in "Kk": tradutor = tradutor + "9"
        elif letra in "Ll": tradutor = tradutor + "&"
        elif letra in "Mm": tradutor = tradutor + "^"
        elif letra in "Nn": tradutor = tradutor + "~"
        elif letra in "Oo": tradutor = tradutor + "#"
        elif letra in "Pp": tradutor = tradutor + "="
        elif letra in "Qq": tradutor = tradutor + "$"
        elif letra in "Rr": tradutor = tradutor + "¨"
        elif letra in "Ss": tradutor = tradutor + "0"
        elif letra in "Tt": tradutor = tradutor + "₢"
        elif letra in "Uu": tradutor = tradutor + "_"
        elif letra in "Vv": tradutor = tradutor + "5"
        elif letra in "Ww": tradutor = tradutor + "4"
        elif letra in "Yy": tradutor = tradutor + "3"
        elif letra in "Xx": tradutor = tradutor + "2"
        elif letra in "Zz": tradutor = tradutor + "1"
        else: tradutor = tradutor + letra
    return tradutor



print(cripto(input("Digite sua frase: ")))

