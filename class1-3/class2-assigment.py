# A.
x = 9
y = 5
if x > y:
    print("BIG")
else:
    print("small")
# B.
for i in range(5):
    print(i + 1)

# C.
session = 1
if session == 1:
    print("summer")
elif session == 2:
    print("winter")
elif session == 3:
    print("fall")
else:
    print("spring")

# D
# 1. 10 times
# 2. 10

# E
my_age = 39
first_l_last_name = "o"
ils_2_usd = 3.46
flew_aboard = True
apartment_num = 9
print(my_age, first_l_last_name, ils_2_usd, flew_aboard, apartment_num)
print(float(my_age) + ils_2_usd)

# F
phone_num = input("Please enter your phone number: ")
print("phone number is: ", phone_num)


# G
def print_hello():
    print("hello")


def calculate():
    print(float(5) + 3.2)


# H
def print_name(name):
    print(name)


def div_2(num):
    print(float(num // 2))


print_name("Dvir")
div_2(5)


# I
def add_2_num(num1, num2):
    return num1 + num2


def add_space_to_strings(str1, str2):
    return str1 + " " + str2


print(add_2_num(2, 4))
print(add_space_to_strings("macabi", "haifa"))

# K
for i in range(5):
    for j in range(i):
        print("*", end="")
    print("")

# L
back_star = 7
for i in range(7):
    for j in range(7):
        if i == j or back_star == j + 1:
            print('*', end="")
        else:
            print(" ", end="")
    back_star -= 1
    print("")


# M
def validate_user_num(num):
    if int(num) < 10:
        print("You entered invalid num \n")
        return False
    else:
        return True


def get_num_from_user():
    usr_num = input("Please Enter 2 digits num: ")
    valid = False
    while not valid:
        valid = validate_user_num(usr_num)
        if valid is False:
            usr_num = input("Please Enter 2 or more digits num: ")
    return usr_num


def calc_num_sum():
    user_num = get_num_from_user()
    c_sum = 0
    num_list = [int(a) for a in str(user_num)]
    for num in num_list:
        c_sum = c_sum + int(num)
    return c_sum


print(calc_num_sum())

