import contextlib
import os
import pathlib
from typing import Iterator


@contextlib.contextmanager
def as_cwd(path: pathlib.Path) -> Iterator[pathlib.Path]:
    old_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield path
    finally:
        os.chdir(old_cwd)
