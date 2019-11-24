#!/usr/bin/env python

from os import chdir
import glob
from os.path import exists 
from argparse import ArgumentParser
from utils import append_to_line_and_insert_following_line, append_blank_line_if_necessary


def run(args):
    if not exists(args.dir):
        print("The directory" + args.dir + "does not exist")
        return
    path_to_header = args.dir + "/" + args.name + ".h"
    path_to_source = args.dir + "/" + args.name + ".cpp"
    if not exists(path_to_header):
        file = open(path_to_header, "w")
        lines = []
        macro = args.name.upper() + "_H"
        lines.append("#ifndef " + macro + "\n")
        lines.append("#define " + macro + "\n\n")
        lines.append("class " + args.name + "\n")
        lines.append("{\n\n};\n\n")
        lines.append("#endif // " + macro + "\n")
        file.writelines(lines)
        file.close()
    if not exists(path_to_source):
        file = open(path_to_source, "w")
        file.writelines(["#include \"" + args.name + ".h\"\n"])
        file.close()

    chdir(args.dir)
    proj_file_path = glob.glob("*.pro")[0]
    append_to_line_and_insert_following_line(proj_file_path, "HEADERS += \\", " \\", args.name + ".h")
    append_to_line_and_insert_following_line(proj_file_path, "SOURCES += \\", " \\", args.name + ".cpp")
    append_blank_line_if_necessary(proj_file_path)


def main():
    parser = ArgumentParser(description="Add a new C++ class")
    parser.add_argument(
        "--dir",
        help="Directory in which to add .h and .cpp files",
        dest="dir",
        type=str,
        required=True)
    parser.add_argument(
        "--name",
        help="Name of class",
        dest="name",
        type=str,
        required=True)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
