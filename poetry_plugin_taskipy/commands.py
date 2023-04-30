import pathlib

from cleo.commands.command import Command
from cleo.helpers import argument, option
from taskipy import cli as taskipy_cli


class TaskipyCommand(Command):
    name = "task"
    description = "Run a taskipy task."
    options = [option("list", "l", "Show list of available tasks.")]
    arguments = [
        argument("name", "Name of the task.", optional=True),
        argument(
            "args",
            "Arguments to pass to the task.",
            optional=True,
            multiple=True,
            default=[],
        ),
    ]

    def handle(self) -> int:
        arguments = []

        cwd = pathlib.Path.cwd()
        if self.option("directory"):
            cwd = pathlib.Path(self.option("directory")).resolve()

        if self.option("list"):
            arguments.append("--list")

        if self.argument("name"):
            arguments.append(self.argument("name"))

        if self.argument("args"):
            arguments.extend(self.argument("args"))

        return taskipy_cli.run(arguments, cwd=cwd)
