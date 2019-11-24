#! /usr/bin/env python

from argparse import ArgumentParser
from utils import create_dir_if_not_existing, create_file_if_not_existing, append_blank_line_if_necessary, append_to_line_and_insert_following_line


def run(args):

    if exists(args.new_proj_dir_name) or exists (args.new_proj_dir_name + "/" + args.name_of_new_pro_file + ".pro"):
        raise Exception("Project may already exist.")
    # At some point I should change these to just create_dir and create_file
    # which are probably just built-in functions
    create_dir_if_not_existing(args.new_proj_dir_name)
    create_file_if_not_existing(args.new_proj_dir_name + "/" + args.name_of_new_pro_file + ".pro")

    append_to_line_and_insert_following_line(args.top_proj_path, "SUBDIRS += \\", " \\", args.new_proj_dir_name)
    append_blank_line_if_necessary(args.top_proj_path)


def main():
    parser = ArgumentParser(description="Add new project")
    parser.add_argument(
        "--top_proj_path",
        help="Path to top .pro file (the one with \"TEMPLATE = subdirs\")",
        dest="top_proj_path",
        type=str,
        required=True)
    parser.add_argument(
        "--new_proj_dir_name",
        help="dir containing new .pro file",
        dest="new_proj_dir_name",
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
