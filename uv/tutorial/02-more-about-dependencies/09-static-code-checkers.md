# Static code checkers

In addition to tests, we also have tools that can analyse our code without running it.
Specifically, we have code formatters, which deal with the code layout, but not its content (the code is equivalent before and after formatting); linters, which detects issues with the code itself; and type checkers, which finds type issues in statically typed Python code.
Such tools are commonly used to ensure a high and consistent code quality in projects, and we highly recommend that you use such tools -- particularly linters and code formatters.

Previously, there were many linters and code formatters, like [flake8](https://flake8.pycqa.org/en/latest/), [autopep8](https://pypi.org/project/autopep8/), [Black](https://github.com/psf/black), [pylint](https://www.pylint.org)++.
However, these days, the main tool to use is [Ruff](https://astral.sh/ruff), which is lightning fast and does pretty much everything flit, isort, black and many other tools did before.

## Exercises

1. Add `ruff` as a uv development dependency and run it in your terminal by running `uv run ruff check .`. What happened?
2. You can customise what Ruff looks for in your `pyproject.toml`-file. Add the following lines to the bottom of your `pyproject.toml` file and run the ruff checks again. What changed, did any files have any issues, if so which?
```toml
[tool.ruff.lint]
select = ["I"]
```
3. Run `uv run ruff check --fix .` and look at your code file. What changed? What do you think will happen if you run `uv run ruff check` again?
4. Run `uv run ruff format .` and look at your code file. How is the `format` argument different from the `check` argument?

<img src="../../../assets/post_it_yellow.svg" alt="Illustraiton of a pink post it note" width="50px" />

## Reflection
By running `ruff check`, we used the linter functionality of Ruff to see if there are potential bugs or [code smells](https://en.wikipedia.org/wiki/Code_smell) that we should fix.
We also added more [linting rules](https://docs.astral.sh/ruff/rules/), and made it consider the [order of our imports](https://docs.astral.sh/ruff/rules/#isort-i).
This made our code fail the linter checks.
However, some of the linter checks can be solved safely automatically, like the import sorting, so by running `ruff check --fix .`, we ask Ruff to automatically resolve the issues it can resolve.

Ruff can also work as a code formatter, which is why we could run `ruff format .`.
When we ran that code it mostly added and removed whitespace, producing (nearly) equivalent code that should behave exactly like the original code, but that also follows the [PEP-8](https://peps.python.org/pep-0008/) style guide.

However, what Ruff doesn't do static type checking, which you will need either [MyPy](https://mypy-lang.org) or [PyRight](https://github.com/microsoft/pyright) for.
Still, Ruff's impressive speed, wide range of linting rules and almost perfect agreement with [Black](https://github.com/psf/black) formatted code has made it very popular in the Python ecosystem.

## Next up
[Locking and lock files](./10-lock-files.md)
