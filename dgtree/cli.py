"""This module provides the DG Tree CLI."""
# cli.py

import argparse
from ast import arg
from pathlib import Path
import sys

from . import __version__
from .dgtree import DirectoryTree

def main():
    args = parse_cmd_line_arguments()
    root_dir = Path(args.root_dir)

    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()

    tree = DirectoryTree(root_dir, args.depth, dir_only=args.dir_only)
    tree.generate()


def parse_cmd_line_arguments():

    parser = argparse.ArgumentParser(
        prog="tree",
        description="DG Tree, a directory tree generator",
        epilog="Thanks for using DG Tree!"
    )

    parser.version = f"DG Tree v{__version__}"

    parser.add_argument(
        "-v", "--version",
        action="version"
    )

    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting at ROOT_DIR"
    )

    parser.add_argument(
        "-d",
        "--depth",
        metavar="",
        action="store",
        type=int,
        default=3,
        help="How deep do you want the generator to go"
    )
    
    parser.add_argument(
        "-f",
        "--dir-only",
        action="store_true",
        help="Generate a directory-only tree"
    )

    


    return parser.parse_args()

   