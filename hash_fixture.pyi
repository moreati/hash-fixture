# SPDX-FileCopyrightText: 2025 Alex Willmer <alex@moreati.org.uk>
# SPDX-License-Identifier: MIT

import typing as t

__version__: str
FORMAT_VERSION: int
SRI_ALGORITHMS: t.Tuple[str, ...]

class DEFAULTS:
    ALGORITHM: str
    LABEL: str
    LINE_COUNT: int

def lines(
    algorithm: str = ..., label: str = ..., line_count: int = ...
) -> t.Generator[bytes]: ...
def main() -> t.NoReturn: ...
