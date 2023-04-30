"""
This test suite is a basic set of sanity tests to ensure that the integration
of the taskipy command with poetry is working as expected. It is not intended
to be an exhaustive test suite for the taskipy CLI itself.
"""
from tests.utils import as_cwd


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
    poetry = project_factory(PYPROJECT_CONTENT)

    with as_cwd(poetry.file.path.parent):
        process = execute_task("test_echo")

    assert process.returncode == 0
    assert process.stdout.read() == b"test\n"
    assert process.stderr.read() == b""


def test_taskipy_known_task_with_args_passed_to_subcommand(
    execute_task, project_factory
):
    poetry = project_factory(PYPROJECT_CONTENT)

    with as_cwd(poetry.file.path.parent):
        process = execute_task("test_echo test2 test3 test4")

    assert process.returncode == 0
    assert process.stdout.read() == b"test test2 test3 test4\n"
    assert process.stderr.read() == b""


def test_taskipy_unknown_task(execute_task, project_factory):
    poetry = project_factory(PYPROJECT_CONTENT)

    with as_cwd(poetry.file.path.parent):
        process = execute_task("unknown")

    assert process.returncode == 127
    assert process.stdout.read() == b'could not find task "unknown"\n'
    assert process.stderr.read() == b""


def test_taskipy_list(execute_task, project_factory):
    poetry = project_factory(PYPROJECT_CONTENT)

    with as_cwd(poetry.file.path.parent):
        process = execute_task("--list")

    assert process.returncode == 0
    assert process.stdout.read() == b"test_echo echo 'test'\n"
    assert process.stderr.read() == b""


def test_utilizing_global_poetry_cwd_flag(execute_task, project_factory):
    """
    Ensure that when we utilize the global poetry flag to change the
    current working directory, we should now get an error because taskipy
    can't find a pyproject.toml file.
    """
    poetry = project_factory(PYPROJECT_CONTENT)

    with as_cwd(poetry.file.path.parent):
        process = execute_task(
            f"--directory {poetry.file.path.parent.parent} test_echo"
        )

    assert process.returncode == 1
    assert (
        process.stdout.read()
        == b"no pyproject.toml file found in this directory or parent directories\n"
    )
    assert process.stderr.read() == b""
