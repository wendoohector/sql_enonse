def calculer_moyenne(n):
    total = 0
    for i in range(n):
        note = float(input(f"Antre not {i+1}: "))
        total += note
    moyenne = total / n
    return moyenne

def afiche_notasyon(moyenne):
    if moyenne >= 90:
        return 'A'
    elif moyenne >= 80:
        return 'B'
    elif moyenne >= 70:
        return 'C'
    elif moyenne >= 60:
        return 'D'
    else:
        return 'F'

def main():
    kantite_not = int(input("Ki kantite not wap antre? "))
    moyenne = calculer_moyenne(kantite_not)
    w = afiche_notasyon(moyenne)
    
    print(f": {moyenne:.2f}")
    print(f"Afiche: {w}")

if __name__ == "__main__":
    main()

