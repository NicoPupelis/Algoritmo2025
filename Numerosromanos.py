romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def convertirromanoadecimal(nroromano):
    total = 0
    anterior = 0
    for letra in nroromano[::-1]:
        actual = romanos[letra.upper()]
        if actual >= anterior:
            total += actual
        else:
            total -= actual
        anterior = actual
    return total

print(convertirromanoadecimal("lxviiixx"))
print(convertirromanoadecimal("ivcc"))
print(convertirromanoadecimal("xvm"))