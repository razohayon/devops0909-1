import io
ַ
# my_file = open("read_my_content.txt", "r")
# contents = my_file.readlines()
# for line in contents:
#     print(line, end='')
# my_file.close()
# my_file = open("names.txt", "w")
# for i in range(3):
#     current_name = input("Write your name: ")
#     my_file.write(current_name + "\n")
# my_file.close()
# my_file = open("names.txt", "r")
# for line in my_file.readlines():
#     print("Hello ", line, end='')
# my_file.close()


try:
    my_file = open("read_my_content1.txt", "r")
    my_file.write("eee77")
except io.UnsupportedOperation as e:
    print("File is opened for reading only")
except PermissionError as e:
    print(e.args)
except FileNotFoundError as e:
    print(e.args)