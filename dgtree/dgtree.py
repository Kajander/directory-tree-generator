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
        dirs_over = ''

        if len(directory.parents) > self.depth:
            dirs_over = '..'

        self._tree.append(f"{prefix}{connector}{Colors.FOLDER}{Icons.FOLDER_OPEN}{directory.name}{os.sep}{dirs_over}{Colors.END}")

        if index != entries_count - 1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX

        self._tree_body(directory=directory, prefix=prefix)
        #self._tree.append(prefix.rstrip()) # creates huge gaps between directories


    def _add_file(self, file, prefix, connector):

        match Path(file).suffix.lower():
            case '.py':     # Pytohn
                self._tree.append(f"{prefix}{connector}{Colors.PYTHON_YELLOW}{Icons.PYTHON}{Colors.WHITE}{file.name}{Colors.END}")
            case '.md':     # Markdown
                self._tree.append(f"{prefix}{connector}{Colors.MARKDOWN}{Icons.MARKDOWN}{Colors.WHITE}{file.name}{Colors.END}")
            case '.json':   # JSON
                self._tree.append(f"{prefix}{connector}{Colors.JSON}{Icons.JSON}{Colors.WHITE}{file.name}{Colors.END}")
            case '.html':   # HTML
                self._tree.append(f"{prefix}{connector}{Colors.HTML}{Icons.HTML}{Colors.WHITE}{file.name}{Colors.END}")
            case '.css':    # CSS
                self._tree.append(f"{prefix}{connector}{Colors.CSS}{Icons.CSS}{Colors.WHITE}{file.name}{Colors.END}")
            case '.cs':     # C#
                self._tree.append(f"{prefix}{connector}{Colors.C_SHARP}{Icons.C_SHARP}{Colors.WHITE}{file.name}{Colors.END}")
            case '.java':   # JAVA
                self._tree.append(f"{prefix}{connector}{Colors.JAVA_ORANGE}{Icons.JAVA}{Colors.WHITE}{file.name}{Colors.END}")
            case '.js':     # JavaScript
                self._tree.append(f"{prefix}{connector}{Colors.JAVASCRIPT_YELLOW}{Icons.JAVASCRIPT}{Colors.WHITE}{file.name}{Colors.END}")
            case '.c':      # C
                self._tree.append(f"{prefix}{connector}{Colors.CEE}{Icons.CEE}{Colors.WHITE}{file.name}{Colors.END}")
            case '.cpp':    # C++
                self._tree.append(f"{prefix}{connector}{Colors.C_PLUS_PLUS}{Icons.C_PLUS_PLUS}{Colors.WHITE}{file.name}{Colors.END}")
            case '.php':    # PHP
                self._tree.append(f"{prefix}{connector}{Colors.PHP}{Icons.PHP}{Colors.WHITE}{file.name}{Colors.END}")
            case '.swift':  # Swift
                self._tree.append(f"{prefix}{connector}{Colors.SWIFT}{Icons.SWIFT}{Colors.WHITE}{file.name}{Colors.END}")
            case '.r':      # R
                self._tree.append(f"{prefix}{connector}{Colors.R_LANG}{Icons.R_LANG}{Colors.WHITE}{file.name}{Colors.END}")
            case '.go':     # GO
                self._tree.append(f"{prefix}{connector}{Colors.GO}{Icons.GO}{Colors.WHITE}{file.name}{Colors.END}")
            case '.ts':     # TypeScript
                self._tree.append(f"{prefix}{connector}{Colors.TYPESCRIPT}{Icons.TYPESCRIPT}{Colors.WHITE}{file.name}{Colors.END}")
            case '.sc':     # Scala
                self._tree.append(f"{prefix}{connector}{Colors.SCALA}{Icons.SCALA}{Colors.WHITE}{file.name}{Colors.END}")
            case '.pl':     # Perl
                self._tree.append(f"{prefix}{connector}{Colors.PERL}{Icons.PERL}{Colors.WHITE}{file.name}{Colors.END}")
            case '.hs':     # Haskell
                self._tree.append(f"{prefix}{connector}{Colors.HASKELL}{Icons.HASKELL}{Colors.WHITE}{file.name}{Colors.END}")
            case '.net':    # .NET
                self._tree.append(f"{prefix}{connector}{Colors.DOTNET}{Icons.DOTNET}{Colors.WHITE}{file.name}{Colors.END}")
            case '.xml':    # XML
                self._tree.append(f"{prefix}{connector}{Colors.XML}{Icons.XML}{Colors.WHITE}{file.name}{Colors.END}")
            case '.rb':     # Ruby
                self._tree.append(f"{prefix}{connector}{Colors.RUBY}{Icons.RUBY}{Colors.WHITE}{file.name}{Colors.END}")
            case '.rs':     # Rust
                self._tree.append(f"{prefix}{connector}{Colors.RUST}{Icons.RUST}{Colors.WHITE}{file.name}{Colors.END}")
            case '.lua':    # Lua
                self._tree.append(f"{prefix}{connector}{Colors.LUA}{Icons.LUA}{Colors.WHITE}{file.name}{Colors.END}")
            case '.sqlite': # SQLite
                self._tree.append(f"{prefix}{connector}{Colors.SQLITE}{Icons.SQLITE}{Colors.WHITE}{file.name}{Colors.END}")
            case '.sql':    # SQL
                self._tree.append(f"{prefix}{connector}{Colors.MYSQL_BEER}{Icons.MYSQL}{Colors.WHITE}{file.name}{Colors.END}")
            case '.psql':   # PostgreSQL
                self._tree.append(f"{prefix}{connector}{Colors.POSTGRESQL}{Icons.POSTGRESQL}{Colors.WHITE}{file.name}{Colors.END}")
            case _:         # Other
                self._tree.append(f"{prefix}{connector}{Colors.FILE}{Icons.FILE}{Colors.WHITE}{file.name}{Colors.END}")