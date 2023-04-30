# Poetry plugin for taskipy

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

## Usage

Once you've installed the taskipy poetry plugin, you'll now see a `task` subcommand on the base `poetry` CLI.

```
$ poetry
...

Available commands:
    ...
    task               Run a taskipy task.
    ...
```


If we assume the following basic `pyproject.toml` file in the current directory or a parent directory:

```toml
[tool.poetry]
name = "project"
version = "0.1.0"

[tool.taskipy.tasks]
test_echo = "echo 'test'"
```

We may then run:

```
$ poetry task test_echo
test
```

For more information, see the [taskipy documentation](https://github.com/taskipy/taskipy/blob/master/README.md).