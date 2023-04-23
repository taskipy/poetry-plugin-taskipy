from pathlib import Path
from typing import Callable

import pytest
from cleo.io.null_io import NullIO
from cleo.testers.command_tester import CommandTester
from poetry.console.application import Application as PoetryApplication
from poetry.factory import Factory
from poetry.poetry import Poetry


@pytest.fixture
def command_tester_factory() -> Callable[[str], CommandTester]:
    def _tester(command: str) -> CommandTester:
        app = PoetryApplication()
        app._load_plugins(NullIO())
        cmd = app.find(command)
        tester = CommandTester(cmd)
        return tester

    return _tester


@pytest.fixture
def execute_task(
    command_tester_factory: Callable[[str], CommandTester]
) -> Callable[[str], CommandTester]:
    def _execute_task(args: str):
        tester = command_tester_factory("task")
        tester.execute(args=args)
        return tester

    return _execute_task


@pytest.fixture
def project_factory(tmp_path: Path):
    def _factory(
        name: str,
        pyproject_content: str,
    ) -> Poetry:
        project_dir = tmp_path / f"poetry-fixture-{name}"
        project_dir.mkdir(parents=True, exist_ok=True)
        with project_dir.joinpath("pyproject.toml").open("w", encoding="utf-8") as f:
            f.write(pyproject_content)

        poetry = Factory().create_poetry(project_dir)
        return poetry

    return _factory
