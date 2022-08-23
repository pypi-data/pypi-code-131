# Copyright 2021 Agnostiq Inc.
#
# This file is part of Covalent.
#
# Licensed under the GNU Affero General Public License 3.0 (the "License").
# A copy of the License may be obtained with this software package or at
#
#      https://www.gnu.org/licenses/agpl-3.0.en.html
#
# Use of this file is prohibited except in compliance with the License. Any
# modifications or derivative works of this file must retain this copyright
# notice, and modified files must contain a notice indicating that they have
# been altered from the originals.
#
# Covalent is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the License for more details.
#
# Relief from the License may be granted by purchasing a commercial license.

"""Lattice file module mapper"""

from enum import Enum


class Filetype(str, Enum):
    """Map module for mapping file module to their
    corresponding file extensions"""

    RESULT = "result.pkl"
    OUTPUT = "output"
    FUNCTION_STRING = "function_string.txt"
    INPUTS = "inputs.pkl"
    ERROR = "error.log"
    EXECUTOR = "executor.pkl"
    RESULTS = "results.pkl"


class FileMapper(str, Enum):
    """Map module for mapping file module to their
    corresponding result from database"""

    ERROR = 3
    FUNCTION_STRING = 4
    EXECUTOR = 5
    INPUTS = 6
    RESULT = 7


class FileExtension(Enum):
    """Extension enum"""

    TXT = ".txt"
    PKL = ".pkl"
