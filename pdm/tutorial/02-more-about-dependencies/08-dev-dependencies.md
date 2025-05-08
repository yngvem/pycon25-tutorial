# Development dependencies
Development dependency groups is a recently added standardised feature specifically for dependencies that shouldn't be published to PyPI as optional dependencies.
When you run PDM install, all development dependencies are installed by default, but you can choose to skip them.

**Note:** the standardisation of dependency groups happened in [PEP753](https://peps.python.org/pep-0735/), which was accepted during the autumn of 2024.
If you haven't updated PDM since then, then you can still use development dependencies, but they will not be specified according to the standard.

## Exercises
1. Use `pdm add --dev pytest` to add pytest as a development dependency.
2. Open the `pyproject.toml`-file and locate the lines regarding the `dev` optional dependencies and the development dependencies. Why is one of the sections in the `pyproject.toml` named `[dependency-groups]` while the other parts start with `[project]` or `[project.optional-dependencies]`?
3. Delete the lines related to the `dev` optional dependencies, but NOT the development dependency group and run `pdm install` again. Did anything change in your environment?
4. Discuss with your neighbour: When do you think you should use development dependencies, and when do you think you should use optional dependencies?

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection
We have now added development dependencies to our code.
We need these dependencies for development, but we don't want consumers of our code to install them.
We store these dependencies in the `dependency-groups`-table to ensure that that PDM knows to install the dependencies during development, but people installing our code will not accidentally end up with all of our development dependencies.
After all, our development dependencies may clash with their dependencies.
For example, we may want a particular version of pytest for our code, but we don't want libraries that depend on our code to have to use the same version of pytest.

This table summarises when to use the different types of dependencies.

| Dependency type | Placement                                    | Description                                 |
|-----------------|----------------------------------------------|---------------------------------------------|
| Mandatory       | `project.dependencies`                       | Minimal dependencies for using your code    |
| Optional        | `project.optional-dependencies.{group_name}` | Special features/platforms                  |
| Development     | `dependency-groups.{group_name}`             | Developing the code, but not for running it |

## Exercises
1. Use `pdm add --dev pytest-cov pytest-randomly` to add [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) and [pytest-randomly](https://pypi.org/project/pytest-randomly/)
2. Run pytest again, did you notice any difference?
3. Run pytest again, this time with the command `pdm run pytest --cov src`. What happened?
4. What do you think happens if you run `pdm run pytest --randomly-seed=last`?

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection
Now that we know how to specify development dependencies, we have added a couple of extra very useful pytest plugins as development dependencies: `pytest-cov` and `pytest-randomly`.
Pytest-randomly does two extremely useful things for testing: It sets random seeds for `random`, `numpy`, `faker` and more, ensuring reproducible tests, and it randomises the order of our tests to help us detect state leakage in our test suite.
Pytest-cov on the other hands is a thin wrapper around [`Coverage.py`](https://coverage.readthedocs.io/), which monitors what code lines in a given directory are run when we run our tests, which is extremely useful to find parts of our code that haven't been tested.

## Next up
[Static code checkers](./09-static-code-checkers.md)
