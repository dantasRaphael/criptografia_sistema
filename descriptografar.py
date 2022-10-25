def descripto(frase) :
    tradutor = ""
    for letra in frase:
        if letra in "@": tradutor = tradutor + "a"
        elif letra in "%": tradutor = tradutor + "b"
        elif letra in "!": tradutor = tradutor + "c"
        elif letra in "*": tradutor = tradutor + "d"
        elif letra in "?": tradutor = tradutor + "e"
        elif letra in "/": tradutor = tradutor + "f"
        elif letra in "+": tradutor = tradutor + "g"
        elif letra in ";": tradutor = tradutor + "h"
        elif letra in "7": tradutor = tradutor + "i"
        elif letra in "8": tradutor = tradutor + "j"
        elif letra in "9": tradutor = tradutor + "k"
        elif letra in "&": tradutor = tradutor + "l"
        elif letra in "^": tradutor = tradutor + "m"
        elif letra in "~": tradutor = tradutor + "n"
        elif letra in "#": tradutor = tradutor + "o"
        elif letra in "=": tradutor = tradutor + "p"
        elif letra in "$": tradutor = tradutor + "q"
        elif letra in "¨": tradutor = tradutor + "r"
        elif letra in "0": tradutor = tradutor + "s"
        elif letra in "₢": tradutor = tradutor + "t"
        elif letra in "_": tradutor = tradutor + "u"
        elif letra in "5": tradutor = tradutor + "v"
        elif letra in "4": tradutor = tradutor + "w"
        elif letra in "3": tradutor = tradutor + "y"
        elif letra in "2": tradutor = tradutor + "x"
        elif letra in "1": tradutor = tradutor + "z"
        else: tradutor = tradutor + letra
    return tradutor

print(descripto(input("Digite sua Criptografada: ")))