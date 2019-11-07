import os


def recursively_get_files_with_ext(top_dir, ext):
    ret = []
    for file in os.listdir(top_dir):
        if file.endswith(ext):
            ret.append(file)
    return ret


def is_string_blank(string):
    stripped = string.strip()
    return not stripped


def create_dir_if_not_existing(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_file_if_not_existing(path):
    if not os.path.exists(path):
        file = open(path, "w")
        file.close()
