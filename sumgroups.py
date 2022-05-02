import os
def check_string(s):
    """Checks if string is number"""
    if not type(s) == str:
        raise TypeError("Input is not a string")
    try:
        return int(remove_all_spaces(s))
    except ValueError:
        print("Input is not a number")

def remove_all_spaces(string):
    """Removes all spaces from string"""
    return string.replace(" ", "")

def remove_spaces(string):
    """Removes spaces from string except space between numbers"""
    while 1:
        if string.find("  ") == -1:
            break
        string = string.replace("  ", " ")
    return string


def split_string_to_list(string):
    """Splits string to list of strings"""
    x = remove_spaces(string).split(" ")
    map(check_string, x) # check if all elements are numbers
    return list(map(int, x))

def sum_group(group):
    """Sums numbers in group"""
    return sum(group)

def create_file(file_name):
    """Creates file"""
    check_file_exists(file_name)
    while 1:
        answer = input("File not  exists. Overwrite? (y/n) ")
        if answer == "y":
            break
        elif answer == "n":
            return "no"
    file_name = open(file_name, "w")
    file_name.close()

def check_file_exists(file_name):
    """Checks if file exists"""
    if not os.path.exists(file_name):
        return False
    return True

def check_files_exists_if_not_overwrite(src, dest):
    """Checks if files exists and if not overwrite"""
    f, f2 = None, None
    if not check_file_exists(src):
        f = create_file(src)
    if not check_file_exists(dest):
        f2 = create_file(dest)
    if f == "no" or f2 == "no":
        print("Nothing to do here")
        return False
    return True

def sum_group_numbers():
    """"Sums numbers in groups in src and writes result to dest"""
    src = input(str("Enter source file name: "))
    dest = input(str("Enter destination file name: "))
    correct = check_files_exists_if_not_overwrite(src, dest)
    if not correct:
        print("Nothing to do here")
        return
    file_src = open(src)
    try:
        file_dest = open(dest, "w")
        try:
            line = file_src.readline()
            while line != "":
                if line != '\n':
                    line = split_string_to_list(line)
                    file_dest.write(str(sum_group(line)) + "\n")
                line = file_src.readline()
        finally:
            file_dest.close()
    finally:
        file_src.close()

sum_group_numbers()