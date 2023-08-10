#mini pwojè
while True:
    w = 1
    nonb = int(input('Antre nonb ou bezwen tab li a: '))
    print(f"Tab {nonb} se: ")

    while w < 11 :
        r = nonb*w
        print(f"{nonb}*{w} = {r}")
        w+=1

    e = input("ou vle kontinye? (Tape 'w' pou kontinye, n pou kanpe)")
    if e !='w':
        break
  
