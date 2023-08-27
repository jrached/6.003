#!/usr/bin/env python3

# This file is part of lib6003, software for use in MIT's 6.003
# Copyright (c) 2018-2019 by the 6.003 Staff <6.003-core@mit.edu>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <https://www.gnu.org/licenses/>.

import os

from setuptools import setup

from lib6003 import __version__ as VERSION


def main():
    with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), "r") as f:
        requirements = f.read().split("\n")

    with open(os.path.join(os.path.dirname(__file__), "README"), "r") as f:
        readme = f.read()

    setup(
        name="lib6003",
        version=VERSION,
        author="6.003 Staff",
        author_email="6.003-core@mit.edu",
        packages=["lib6003"],
        scripts=[],
        url="https://mit.edu/6.003",
        license="GPLv3+",
        description="Software for 6.003",
        long_description=readme,
        include_package_data=True,
        entry_points={},
        install_requires=requirements,
        package_dir={"lib6003": "lib6003"},
    )


if __name__ == "__main__":
    main()
