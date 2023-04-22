from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_taskipy.commands import TaskipyCommand


class TaskipyPlugin(ApplicationPlugin):
    @property
    def commands(self):
        return [TaskipyCommand]
