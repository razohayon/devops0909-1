import requests


# try:
#     my_var = int(input("Enter num: "))
#     ny_sec_var = int(input("Enter other num: "))
#     result = my_var / ny_sec_var
#     print(result)
# except ZeroDivisionError as e:
#     print("Could not dvide by zero")
# except ValueError as e:
#     print("enter normal num")
# except BaseException as e:
#     print(e.args)
# try:
#     requests.get("htpps://github.com")
# except BaseException as e:
#     print("something when wrong" + str(e.args))
def get_user_age():
    input_from_user = int(input("enter your age: "))
    if input_from_user < 0:
        raise ValueError("Age cant be negative")
get_user_age()