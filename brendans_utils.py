import glob
import os


def do_for_all_files(top_dir, action):
    for dirpath, subdirs, files in os.walk(top_dir, topdown=True):
        for file in files:
            action(os.path.join(dirpath, file))


def get_files_with_ext(top_dir, ext):
    ret = []
    for file in os.listdir(top_dir):
        if file.endswith(ext):
            ret.append(file)
    return ret


def is_string_blank(the_string):
    stripped = the_string.strip()
    return not stripped


def create_dir_if_not_existing(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_file_if_not_existing(path):
    if not os.path.exists(path):
        file = open(path, "w")
        file.close()


def append_blank_line_if_necessary(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            pass
        last_line = line
        if last_line.endswith('\n') or last_line.endswith('\r\n') or last_line.strip() == '':
            return
    with open(filepath, 'a') as f:
        f.write('\n')


def append_to_line_and_insert_following_line(filepath, line_of_interest, string_to_append, contents_to_insert_in_next_line):
    """This function searches the file with path `filepath` for the line 
    `line_of_interest`, appends `string_to_append` 
    to it, and adds a new line below it contaning 
    `contents_to_insert_in_next_line`."""
    file = open(filepath, 'r')
    lines = file.readlines()

    index_of_interest = 0
    line_found = False
    for line in lines:
        if line.strip() == line_of_interest:
            line_found = True
            break
        index_of_interest += 1

    if line_found:
        index_of_blank_line = index_of_interest
        while index_of_blank_line < len(lines) and not is_string_blank(lines[index_of_blank_line]):
            index_of_blank_line += 1
        prev_line = lines[index_of_blank_line - 1].rstrip()
        if not prev_line.endswith(string_to_append):
            lines[index_of_blank_line - 1] = prev_line + string_to_append
        lines.insert(index_of_blank_line, "\n    " + contents_to_insert_in_next_line + '\n')
    else:
        lines.append("\n\n")
        lines.append(line_of_interest)
        lines.append("\n    " + contents_to_insert_in_next_line + '\n')

    file.close()
    file = open(filepath, 'w')
    file.writelines(lines)
    file.close()
