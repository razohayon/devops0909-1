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
            usr_num = input("Please Enter 2 digits num: ")
    return usr_num


def calc_num_sum():
    user_num = get_num_from_user()
    c_sum = 0
    num_list = [int(a) for a in str(user_num)]
    print(num_list)
    for num in user_num:
        c_sum = c_sum + int(num)
    return c_sum


print(calc_num_sum())

