def get_name():
    name = input("Enter Name: ")
    return name


def save_name():
    name = get_name()
    file_names = open("names-func.txt", "a")
    file_names.write(name+"\n")
    file_names.close()


def show_name():
    file_names = open("names-func.txt", "r")
    print(file_names.read())
    file_names.close()


save_name()
show_name()
