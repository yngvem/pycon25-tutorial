# Package extras
Package extras or optional dependencies, previously often called dependency groups (but now dependency groups is a specific thing we'll discuss later), is a way to group the dependencies of our project.
They are commonly used if you have optional features that not every user of your package needs.
For example, if you use the artificial intelligence library *Huggingface Transformers*, then you might also want to use the parts of the Transformers library that require *PyTorch*.
One way to install both Transformers and a compatible version of PyTorch simultaneously is by installing `transformers[torch]`, which specifies that you want the `torch`-package extras when you install Transformers.
While package extras are meant to add optional dependencies to your projects, they can also be used to define development dependencies, e.g. running the unit tests or creating the documentation.

## Exercises
1. Add `rich` as an optional dependency in the group `rich` by running `uv add rich --optional pretty`. Can you find the `rich`-dependency in the `pyproject.toml`-file?
2. Try to run the `get_charlas.py` script again. Did anything change?
2. Sync the uv environment again with `uv sync`.
3. Run the `get_charlas.py` script again. Did you still get the nice colours?
4. Install the package with the `dev`-extras again by writing `uv sync --extra pretty`
5. Run the `get_charlas.py` script again to check that you got the nice colours back.
6. When do you think it makes sense to use optional dependencies?

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection
We have now added `rich` as an optional dependency to our package.
This means that when we later publish our code to PyPI, people can install it both with and without the `rich`-dependency.
This is very useful when our code has some functionality that not all users of our code are interested in.
By making the dependencies for that code optional, we reduce the number of indirect dependencies for users of our package, which again makes their lives easier.

A prime example is if we make a cli application.
Then, we may want to include a specific version of [Typer](https://typer.tiangolo.com) to get a nice CLI interface.
However, if we pin the Typer version, and someone else wants to use our code as a component in their own CLI, then they would be locked to the same Typer version as we are using.
Instead, if we make the CLI-dependencies into optional dependencies, then this is unproblematic.
Users who want to install the CLI can install `{PACKAGE_NAME}[cli]`, while those who only want the library features can simply install `{PACKAGE_NAME}`.

Moreover, since optional dependencies aren't installed by default by users, uv will also not include them when you sync your project.
However, if you either add an optional dependency to a group, then uv will include that group until the next time you run `uv sync` (unless you also include the `--extra` argument to explicitly include optional groups.)
An important thing to realise here, is that this means that it's a big difference between running `uv add {package} --optional {group-name}` and manually updating the `pyproject.toml`-file and running `uv sync`.
In fact, `uv add {package} --optional {group-name} ` is equivalent to manually updating the `pyproject.toml` file and running `uv sync --extra {group-name}`.

So we have optional dependencies, but what about PyTest? Should that be a project dependency?
No, we use it for development, so it should probably be listed as such, which is why the next part of this tutorial is about development dependencies.

## Next up
[Development dependencies](./08-dev-dependencies.md)
