def lis_pwodwi(products):
    print("List pwodwi disponib:")
    for kle_pwodwi, vale_pwodwi in products.items():
        print(f"{kle_pwodwi}: {vale_pwodwi['name']} - {vale_pwodwi['price']} goud")

def ajoute_pwodwi(cart, product):
    cart.append(product)
    print(f"{product['name']} ajoute nan panye a.")

def calcul_total(cart):
    total = sum(product['price'] for product in cart)
    return total

def pri_cart(cart):
    print("Panye ou genyen:")
    for product in cart:
        print(f"{product['name']} - {product['price']} goud")
    total = calcul_total(cart)
    print(f"Pri total la se {total} goud.")

def main_menu():
    print("1. Afiche mesaj byenvini")
    print("2. Chache pwodwi")
    print("3. Wè panye a ak tout pri total la")
    print("4. Fèmen")

if __name__ == "__main__":
    products_list = {
        "pwodwi1": {"name": "Mayi", "price": 10, "quantity": 5},
        "pwodwi2": {"name": "Diri", "price": 20, "quantity": 10},
        "pwodwi3": {"name": "Pwa", "price": 15, "quantity": 8},
    }
    cart = []

    while True:
        main_menu()
        choice = input("Chwazi yon opsyon: ")

        if choice == "1":
            print("Byenvini nan magazen nou!")
        elif choice == "2":
            lis_pwodwi(products_list)
            chwa_pwodwi = input("Chwazi yon pwodwi pa non li savledi pwodwi 1 oubyen 2 oubyen 3: ")
            if chwa_pwodwi in products_list:
                ajoute_pwodwi(cart, products_list[chwa_pwodwi])
            else:
                print("Pwodwi a pa disponib.")
        elif choice == "3":
            pri_cart(cart)
        elif choice == "4":
            print("Mèsi! ou ka retounen.")
            break
        else:
            print("Opsiyon pa valab.")
