import taskipy
from cleo.commands.command import Command
from cleo.helpers import argument, option


class TaskipyCommand(Command):
    name = "task"
    description = "taskipy - the complementary task runner for python"
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
        command = ""

        if self.argument("name"):
            command += self.argument("name")

        if self.argument("args"):
            command += " "
            command += " ".join(self.argument("args"))

        return taskipy.run(command)
