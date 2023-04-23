# Poetry Plugin for Taskipy

This package is a plugin for the Poetry CLI that directly integrates [taskipy](https://github.com/taskipy/taskipy)
into it. With this plugin installed, you may then use a `task` subcommand on the Poetry
CLI to run your regular taskipy tasks.

## Installation

There are multiple ways to install this plugin and the way you should install it depends on
how you've installed Poetry itself.

### With Poetry installed via the official installer

With the official installer, you can use the Poetry CLI itself to install the plugin.

```
$ poetry self add poetry-plugin-taskipy
```

### With Poetry installed via Pipx

If you installed Poetry via Pipx, you'll want to utilize the `inject` command.

```
$ pipx inject poetry poetry-plugin-taskipy
```

### With Poetry installed via Pip

If you installed Poetry via Pip, you can install the plugin in that same environment.

```
$ pip install poetry-plugin-taskipy
```
