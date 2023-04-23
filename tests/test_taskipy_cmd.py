"""
This test suite is a basic set of sanity tests to ensure that the integration
of the taskipy command with poetry is working as expected. It is not intended
to be an exhaustive test suite for the taskipy CLI itself.
"""
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


PYPROJECT_CONTENT = """\
[tool.poetry]
name = "taskipy"
version = "0.1.0"
authors = ["Taskipy Team"]
description = "tasks runner for python projects"

[tool.taskipy.tasks]
test_echo = "echo 'test'"
"""


def test_taskipy_known_task(execute_task, project_factory):
    poetry = project_factory(name="task", pyproject_content=PYPROJECT_CONTENT)

    with as_cwd(poetry.file.path.parent):
        result = execute_task("test_echo")
        assert result.status_code == 0


def test_taskipy_known_task_with_args_passed_to_subcommand(
    execute_task, project_factory
):
    poetry = project_factory(name="task", pyproject_content=PYPROJECT_CONTENT)

    with as_cwd(poetry.file.path.parent):
        result = execute_task("test_echo test2 test3 test4")
        assert result.status_code == 0


def test_taskipy_unknown_task(execute_task, project_factory):
    poetry = project_factory(name="task", pyproject_content=PYPROJECT_CONTENT)

    with as_cwd(poetry.file.path.parent):
        result = execute_task("unknown")
        assert result.status_code == 127


def test_taskipy_list(execute_task, project_factory):
    poetry = project_factory(name="task", pyproject_content=PYPROJECT_CONTENT)

    with as_cwd(poetry.file.path.parent):
        result = execute_task("--list")
        assert result.status_code == 0


def test_utilizing_global_poetry_cwd_flag(execute_task, project_factory):
    """
    Ensure that when we utilize the global poetry flag to change the
    current working directory, we should now get an error because taskipy
    can't find a pyproject.toml file.
    """
    poetry = project_factory(name="task", pyproject_content=PYPROJECT_CONTENT)

    with as_cwd(poetry.file.path.parent):
        result = execute_task(f"--directory {poetry.file.path.parent.parent} test_echo")
        assert result.status_code == 1
