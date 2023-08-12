def Konte_vwayel(Teks):
    miniskil = "aeiou"
    konte = 0
    for let in Teks:
        if let.islower() and let in miniskil:
            konte += 1
    return konte

teks_ou_antre = input("Antre teks ou : ")
Kantite = Konte_vwayel(teks_ou_antre)

print(f"Nonb vwayel miniskil yo : {Kantite}")
