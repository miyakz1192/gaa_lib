
import os

def change_file_ext(file_name, new_ext):
    dir_name = os.path.dirname(file_name)
    basename = os.path.basename(file_name)

    file_name = os.path.splitext(basename)[0]
    ext_name  = os.path.splitext(basename)[1]

    if not dir_name:
        output_file_name = file_name + new_ext
    else:
        output_file_name = dir_name + "/" + file_name + new_ext

    return output_file_name

def remove_file_ext(file_name):
    return change_file_ext(file_name, "")
