# Bonus content: Package scripts

You may have noticed that some Python projects also create executables.
For example, you can run Pytest by just running the command `pytest`.
This is done through something called *[executable scripts](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#creating-executable-scripts)* or entry points.

## Exercises

1. Open the `pyproject.toml` file and update it so it has a block that says

```toml
[project.scripts]
{PACKAGE_NAME} = "{PACKAGE_NAME}.pycon:main"
```

2. Run `pdm install`. What do you think will happen when you run `pdm run {PACKAGE_NAME}` now?
3. Update the `{PACKAGE_NAME} = "{PACKAGE_NAME}.pycon:main` so it says `pycon_next_session = "{PACKAGE_NAME}.pycon:main` and run `pdm install`. What do you think will happen when you run `pdm run pycon_next_session`?

## Reflection

We have now seen how we can create executables with Python, and this is how tools like `pytest` and `pre-commit` registers executables on your system.
Specifically, you let `pip`, `pipx`, `pdm`, etc. create the executable when you install the tool, and they will just run the function specified in the `project.scripts` table.

Thus, after solving exercise 3, running `pdm run pycon_next_session` will be the same as running the following Python script:
```python
from {PACKAGE_NAME}.pycon import main
main()
```

However, this is not the only way to make your code runnable!
We can also make executable modules.

## Exercises

1. Try to run `pdm run python -m {PACKAGE_NAME}.pycon`. What do you think happened?
2. Try to run `pdm run python -m {PACKAGE_NAME}`. What do you think will happen now?
3. Add the file `__main__.py` into your `src/{PACKAGE_NAME}` directory. The file should have the following contents
```python
from {PACKAGE_NAME}.pycon import main
main()
```
4. Try to run `pdm run python -m {PACKAGE_NAME}` again. Discuss with your neighbour: Why do you think this worked now?
5. Discuss with your neighbour: What do you think the benefit of using `python -m {module}` compared to just running `python {path_to_script}`?


## Reflection

We have now seen the other way of making executable Python modules: The `python -m`-method.
This works a little bit differently from the `project.scripts`-method.
With the executable scripts, we specify a function we want to run, while with the `python -m`-method we specify a module.
This means that running `pdm run python -m {PACKAGE_NAME}.pycon` will be the same as running `pdm run python src/{PACKAGE_NAME}/pycon.py`.

The benefit of using the `python -m` method compared to just running Python files with `python {path_to_script}` is that we can run any importable module, even if you don't know its path.
You can test this yourself by e.g. running `pdm run python -m calendar`.
This will be the same as running the builtin calendar module in Python!

If you want to see a full list of all runnable modules that come built-in with Python, then Trey Hunner has written about it [here](https://www.pythonmorsels.com/cli-tools/).

## Next up
[Virtual environments](./05-virtual-environments.md)
