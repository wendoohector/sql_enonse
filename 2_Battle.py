def Ranplase(w):
    a = list(w)  

    for i in range(1, len(w)):
        if w[i].lower() in 'aeiouy' and w[i - 1] != ' ':
            a[i - 1] = 'X'

    return ''.join(a)


egzanp = "Wendel gen yon pitit"
a = Ranplase(egzanp)
print(a)
