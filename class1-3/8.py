def print_name(name):
    print("name is:", name)


def power_by_3(number):
    return number ** 3

name_input = input("Enter your name: ")
print_name(name_input)
number_input = input("Enter number to power by 3: ")
print(power_by_3(int(number_input)))
