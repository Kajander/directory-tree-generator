# dgtree.py

"""This module provides DG Tree main module."""

import os
from pathlib import Path

from .colors import Colors
from .icons import Icons

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class DirectoryTree:
    def __init__(self, root_dir, depth, dir_only=False):
        self.depth = depth
        self._generator = _TreeGenerator(root_dir, self.depth, dir_only)

    def generate(self):
        tree = self._generator.build_tree()
        for entry in tree:
            print(entry)

class _TreeGenerator:
    def __init__(self, root_dir, depth, dir_only=False):
        self._root_dir = Path(root_dir)
        self.depth = depth
        self._dir_only = dir_only
        self._tree = []
 
    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree

    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)

    def _tree_body(self, directory, prefix=""):

        if len(directory.parents) > self.depth:
            pass
            # TODO: 
            # calculate how many folders left
            # add a number after the /

        else:
       
            entries = self._prepare_entries(directory)
            entries_count = len(entries)

            for index, entry in enumerate(entries):
                connector = ELBOW if index == entries_count - 1 else TEE

                if entry.is_dir():
                    self._add_directory(entry, index, entries_count, prefix, connector)
                else:
                    self._add_file(entry, prefix, connector)
    
    def _prepare_entries(self, directory):
        entries = directory.iterdir()
        
        if self._dir_only:
            entries = [entry for entry in entries if entry.is_dir()]
            return entries
        entries = sorted(entries, key=lambda entry: entry.is_file())
        return entries

    def _add_directory(self, directory, index, entries_count, prefix, connector):

        self._tree.append(f"{prefix}{connector}{Colors.FOLDER}{Icons.FOLDER_OPEN}{directory.name}{os.sep}{Colors.END}")

        if index != entries_count - 1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX

        self._tree_body(directory=directory, prefix=prefix)
        #self._tree.append(prefix.rstrip()) # creates huge gaps between directories

    def _add_file(self, file, prefix, connector):

        match Path(file).suffix.lower():
            case '.py':
                self._tree.append(f"{prefix}{connector}{Colors.PYTHON_YELLOW}{Icons.PYTHON}{Colors.WHITE}{file.name}{Colors.END}")
            case '.md':
                self._tree.append(f"{prefix}{connector}{Colors.MARKDOWN}{Icons.MARKDOWN}{Colors.WHITE}{file.name}{Colors.END}")
            case '.json':
                self._tree.append(f"{prefix}{connector}{Colors.MARKDOWN}{Icons.JSON}{file.name}{Colors.END}")
            case '.html':
                self._tree.append(f"{prefix}{connector}{Colors.HTML}{Icons.HTML}{Colors.WHITE}{file.name}{Colors.END}")
            case '.css':
                self._tree.append(f"{prefix}{connector}{Colors.CSS}{Icons.CSS}{Colors.WHITE}{file.name}{Colors.END}")
            case '.cs':
                self._tree.append(f"{prefix}{connector}{Colors.C_SHARP}{Icons.C_SHARP}{Colors.WHITE}{file.name}{Colors.END}")
            case '.java':
                self._tree.append(f"{prefix}{connector}{Colors.JAVA_ORANGE}{Icons.JAVA}{Colors.WHITE}{file.name}{Colors.END}")
            case '.js':
                self._tree.append(f"{prefix}{connector}{Colors.JAVASCRIPT_YELLOW}{Icons.JAVASCRIPT}{Colors.WHITE}{file.name}{Colors.END}")
            case '.c':
                self._tree.append(f"{prefix}{connector}{Colors.CEE}{Icons.CEE}{Colors.WHITE}{file.name}{Colors.END}")
            case '.cpp':
                self._tree.append(f"{prefix}{connector}{Colors.C_PLUS_PLUS}{Icons.C_PLUS_PLUS}{Colors.WHITE}{file.name}{Colors.END}")
            case '.php':
                self._tree.append(f"{prefix}{connector}{Colors.PHP}{Icons.PHP}{Colors.WHITE}{file.name}{Colors.END}")
            case '.swift':
                self._tree.append(f"{prefix}{connector}{Colors.SWIFT}{Icons.SWIFT}{Colors.WHITE}{file.name}{Colors.END}")
            case '.r':
                self._tree.append(f"{prefix}{connector}{Colors.R_LANG}{Icons.R_LANG}{Colors.WHITE}{file.name}{Colors.END}")
            case '.go':
                self._tree.append(f"{prefix}{connector}{Colors.GO}{Icons.GO}{Colors.WHITE}{file.name}{Colors.END}")
            case '.ts':
                self._tree.append(f"{prefix}{connector}{Colors.TYPESCRIPT}{Icons.TYPESCRIPT}{Colors.WHITE}{file.name}{Colors.END}")
            case '.sc':
                self._tree.append(f"{prefix}{connector}{Colors.SCALA}{Icons.SCALA}{Colors.WHITE}{file.name}{Colors.END}")
            case '.pl':
                self._tree.append(f"{prefix}{connector}{Colors.MARKDOWN}{Icons.PERL}{Colors.WHITE}{file.name}{Colors.END}")
            case '.hs':
                self._tree.append(f"{prefix}{connector}{Colors.HASKELL}{Icons.HASKELL}{Colors.WHITE}{file.name}{Colors.END}")
            case '.net':
                self._tree.append(f"{prefix}{connector}{Colors.DOTNET}{Icons.DOTNET}{Colors.WHITE}{file.name}{Colors.END}")
            case '.xml':
                self._tree.append(f"{prefix}{connector}{Colors.MARKDOWN}{Icons.XML}{Colors.WHITE}{file.name}{Colors.END}")
            case '.rb':
                self._tree.append(f"{prefix}{connector}{Colors.MARKDOWN}{Icons.RUBY}{Colors.WHITE}{file.name}{Colors.END}")
            case '.rs':
                self._tree.append(f"{prefix}{connector}{Colors.MARKDOWN}{Icons.RUST}{Colors.WHITE}{file.name}{Colors.END}")
            case '.lua':
                self._tree.append(f"{prefix}{connector}{Colors.MARKDOWN}{Icons.LUA}{Colors.WHITE}{file.name}{Colors.END}")
            case '.groovy':
                self._tree.append(f"{prefix}{connector}{Colors.MARKDOWN}{Icons.GROOVY}{Colors.WHITE}{file.name}{Colors.END}")
            case '.sqlite':
                self._tree.append(f"{prefix}{connector}{Colors.MARKDOWN}{Icons.SQLITE}{Colors.WHITE}{file.name}{Colors.END}")
            case '.sql':
                self._tree.append(f"{prefix}{connector}{Colors.MARKDOWN}{Icons.MYSQL}{Colors.WHITE}{file.name}{Colors.END}")
            case '.psql':
                self._tree.append(f"{prefix}{connector}{Colors.POSTGRESQL}{Icons.POSTGRESQL}{Colors.WHITE}{file.name}{Colors.END}")
            case _:
                self._tree.append(f"{prefix}{connector}{Colors.FILE}{Icons.FILE}{Colors.WHITE}{file.name}{Colors.END}")