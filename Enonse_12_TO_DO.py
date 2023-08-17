todo_list = []

def add_task(deskripsyon):
    todo_list.append(deskripsyon)

def display_tasks():
    for i, task in enumerate(todo_list, start=1):
        print(f"{i}. {task}")

def mark_task_done(task_index):
    try:
        del todo_list[task_index - 1]
        print("Tach la te fini.")
    except IndexError:
        print("Endis tach sa a pa egziste nan lis la.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in todo_list:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            todo_list = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Nou pa jwenn fiche a.")

def main():
    while True:
        print("\Meni:")
        print("1. Ajoute tach")
        print("2. Afiche tach yo")
        print("3. Fini yon tach")
        print("4. Anrejistre epi fèmen")

        choice = input("Chwazi yon opsyon: ")

        if choice == "1":
            deskripsyon = input("Antre deskripsyon tach la: ")
            add_task(deskripsyon)
        elif choice == "2":
            print("Tach yo nan lis la:")
            display_tasks()
        elif choice == "3":
            task_index = int(input("Antre nonb ki endike tach fini a: "))
            mark_task_done(task_index)
        elif choice == "4":
            save_tasks()
            break
        else:
            print("Opsyon pa korek. Chwazi yon opsyon ant 1 ak 4 sèlman.")

if __name__ == "__main__":
    main()
