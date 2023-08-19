import random

def genere_pseudos(prenon, non):
    pseudos = []
    

    inisyal = prenon[0].upper() + non[0].upper()
    pseudo1 = inisyal
    pseudos.append(pseudo1)
    
    
    pseudo2 = prenon[0].upper() + non.lower()
    pseudos.append(pseudo2)
    
    
    non_kout = non if len(non) < len(prenon) else prenon
    non_reyaje = non_kout[1:] + non_kout[0]
    nimewo_random = str(random.randint(100, 1000))
    pseudo3 = non_reyaje.capitalize() + nimewo_random
    pseudos.append(pseudo3)
    
    return pseudos

def meni():
    prenon = input("Antre non ou : ")
    non = input("Antre non ou : ")
    
    pseudos = genere_pseudos(prenon, non)
    print(f"Bonjou {non} {prenon}, nou rekoni nan sèvis nou an.")
    for i, pseudo in enumerate(pseudos, start=1):
        print(f"{i}) {pseudo}")
    
    chwa = random.choice(pseudos)
    print("\nNon itilizatè a chwazi pou rezo sosyal la se :", chwa)
    
    
    with open("database.txt", "a") as fichye:
        fichye.write(chwa + ",")
    
    
    with open("database.txt", "r") as fichye:
        kontni = fichye.read()
        non_kreye = kontni.split(",")
        kantite = len(non_kreye) - 1  
    
    print(f"\nKantite non total kreye jiska kounye a : {kantite}")

if __name__ == "__main__":
    meni()
