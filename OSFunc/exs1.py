import platform
import os


def get_os():
    return platform.system() + " " + platform.release()


def get_cur_dir():
    return os.getcwd()


def get_files_in_dir(dir_name):
    try:
        return os.listdir(dir_name)
    except IOError:
        return "Can't read dir files"


def print_file(filename):
    try:
        f = open(filename, 'r')
        text = f.read()
        f.close()
        return print(text)
    except IOError:
        return print("can't read file")



print(get_os())
print(get_files_in_dir(get_cur_dir()))
print_file('README')

