#!/usr/bin/env python

from os import makedirs
from os.path import exists 
from argparse import ArgumentParser


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
        lines.append("#endif\n")
        file.writelines(lines)
        file.close()
    if not exists(path_to_source):
        file = open(path_to_source, "w")
        file.writelines(["#include \"" + args.name + ".h\"\n"])
        file.close()

    


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
