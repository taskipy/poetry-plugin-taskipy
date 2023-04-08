from poetry.console.commands.command import Command
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_taskipy.commands import TaskipyCommand


class TaskipyPlugin(ApplicationPlugin):
    @property
    def commands(self) -> list[type[Command]]:
        return [TaskipyCommand]
