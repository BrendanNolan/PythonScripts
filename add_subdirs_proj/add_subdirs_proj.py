#! /usr/bin/env python
from argparse import ArgumentParser
from utils import is_string_blank, create_dir_if_not_existing, create_file_if_not_existing


def run(args):
    #  Open file for reading and writing, placing the pointer at the beginning of the file.
    top_project_file = open(args.top_proj_path, "r")

    create_dir_if_not_existing(args.new_proj_path)
    create_file_if_not_existing(args.new_proj_path + "/" + args.name_of_new_pro_file + ".pro")

    lines = top_project_file.readlines()

    subdirs_line_index = 0
    subdirs_found = False
    for line in lines:
        if line.lstrip().startswith("SUBDIRS"):
            subdirs_found = True
            break
        subdirs_line_index += 1

    if subdirs_found:
        i = subdirs_line_index
        while i < len(lines) and not is_string_blank(lines[i]):
            i += 1
        prev_line = lines[i - 1].rstrip()
        if prev_line[-1] != "\\":
            lines[i - 1] = prev_line + " \\"
        lines.insert(i, "\n    " + args.new_proj_path)
    else:
        lines.append("\n\nSUBDIRS = " + args.new_proj_path)

    #  Make sure top .pro file ends with blank line
    if not is_string_blank(lines[-1]):
        lines.append("\n")

    top_project_file = open(args.top_proj_path, "w")
    top_project_file.writelines(lines)
    top_project_file.close()


def main():
    parser = ArgumentParser(description="Add new project")
    parser.add_argument(
        "--top_proj_path",
        help="Path to top .pro file (the one with \"TEMPLATE = subdirs\")",
        dest="top_proj_path",
        type=str,
        required=True)
    parser.add_argument(
        "--new_proj_path",
        help="Path to dir containing new .pro file",
        dest="new_proj_path",
        type=str,
        required=True)
    parser.add_argument(
        "--name_of_new_pro_file",
        help="The name of the new .pro file, without \".pro\" extension",
        dest="name_of_new_pro_file",
        type=str,
        required=True)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()