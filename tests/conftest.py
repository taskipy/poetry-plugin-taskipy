import uuid
import subprocess
from pathlib import Path
from typing import Callable

import pytest
from poetry.factory import Factory
from poetry.poetry import Poetry


@pytest.fixture
def execute_task() -> Callable[[str], subprocess.Popen]:
    def _execute_task(args: str):
        process = subprocess.Popen(
            f"poetry task {args}",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        process.wait()
        return process

    return _execute_task


@pytest.fixture
def project_factory(tmp_path: Path):
    def _factory(pyproject_content: str) -> Poetry:
        project_dir = tmp_path / f"poetry-fixture-{uuid.uuid4()}"
        project_dir.mkdir(parents=True, exist_ok=True)
        with project_dir.joinpath("pyproject.toml").open("w", encoding="utf-8") as f:
            f.write(pyproject_content)

        poetry = Factory().create_poetry(project_dir)
        return poetry

    return _factory
