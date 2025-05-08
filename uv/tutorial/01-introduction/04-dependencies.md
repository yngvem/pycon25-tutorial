# Our first installable module

We are now ready to start developing our package.
To start with, we'll add a runnable module inside our package (we'll soon have a better way of testing whether our code works).
Specifically, we'll add a Python module that fetches the PyCon US programme, parses it and prints out the immediate next sessions (which it does to help us check if the code works, later, we'll look at unit tests for a better way to check this.)

## Exercises
1. Create a file `pycon.py` in the `src/{{package name}}` directory (replace `package name` with the name of your package) and copy the contents of [`code/packaging-tutorial/src/packaging_tutorial/pycon.py`](../../code/packaging-tutorial/src/packaging_tutorial/pycon.py) into it. You do not need to understand the code - this is just an example to show how we can package our code.
2. Run the command `uv sync` in the same terminal window you used to run `uv init --lib`. You should get a few lines of output, among them the line `Creating virtual environment at: .venv`.
3. Run the file you created by typing `uv run python src/{{package_name}}/pycon.py` in your terminal emulator (replace `{{package name}}` with the name of your package). What happened?

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection

When we tried to run the script above, we got an `ImportError` because we hadn't installed HTTPX first.
This is great since we want to have full control over what packages we need to install to run our code.
Otherwise, it would be very difficult for others to use it!
We should have all this information about what we need to run our code in the `pyproject.toml`-file and let uv take care of installing and managing the dependencies.
We could manually add the dependencies to the `pyproject.toml`-file.
However, uv has a handy way to add dependencies and install them simultaneously: `uv add`.

## Exercises
1. Add httpx as a dependency to your project by running `uv add httpx`
2. Open the `pyproject.toml` file. Can you find httpx anywhere in that file?
3. Try to run the `pycon.py` file again

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection
When you ran `uv add httpx`, three things happened: uv checked if you could add HTTPX as a dependency, then it updated the `pyproject.toml` file before it installed HTTPX in the virtual environment for your project.
You could do all of this manually as well.

Before we move on, we can make a little script to check if we can install our library.

## Exercises

1. Create a new folder in your project root (i.e. outside of `src`) called `scripts`, and create a new file `get_charlas.py` into it. Copy the contents of [`code/packaging-tutorial/get_charlas.py`](../../code/packaging-tutorial/scripts/get_charlas.py) into it (you may need to modify the `import packaging_tutorial.pycon`-import, replacing `packaging_tutorial` with the name of the directory inside `src`) and run it. What did it do?
2. Discuss with your neighbour: why do you think the import in the `get_charlas.py`-script worked?

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />


## Reflection
The reason the import in the `get_charlas.py`-script worked was that when we ran `uv sync` in exercise 2, our package was installed into our virtual environment (more about virtual environments later).
This means we can import the code as any other package you have installed!
Importantly, when you set up a project with uv, it is installed in a way so any change in `src/{{package_name}}` is automatically included in the imported code.
This is called an *editable install*, and the process was standardised in [PEP 660](https://peps.python.org/pep-0660/) and is described well in the [Setuptools documentation](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).

Now that we have tested that we can import our code, we are ready to add a couple of dependencies and improve it a little bit further.

## Exercises

1. Open the `pyproject.toml` file and manually add `pydantic` to the dependencies.
2. Replace the code in your `pycon.py`-file with the code from the [`code/packaging-tutorial/src/packaging_tutorial/validated_pycon.py`](../../code/packaging-tutorial/src/packaging_tutorial/validated_pycon.py) file from this repository and run the code with `uv run --no-sync python scripts/get_charlas.py`. What happened, and why did this happen?
3. Try again, but this time by running `uv run python scripts/get_charlas.py`. What happened now? 

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection
So we see that we can add dependencies to the `pyproject.toml` file manually, which is very useful when we want to set up a template for others to use.
If you do this, then uv will install all dependencies automatically next time you use `uv run` unless you specifically add the `--no-sync`-flag.
This is a bit different from other tools, which usually don't sync dependency when you run the code.
However, uv syncs dependencies very fast (since does a lot of smart caching), so it's able to re-sync almost instantly and will therefore do so each time you run code through it.

Still, we recommend that you use `uv add` in most cases.
It's a one-step process that ensures that you get a compatible set of dependencies.
Note that uv will try to add the latest version of a given dependency that is compatible with the rest of your dependencies, which means that the order in which you add dependencies can matter (but 99% of the time, it won't matter).

## Next up
[Virtual environments](./05-virtual-environments.md), or, if you want to look at the bonus reading: [runnable scripts](./0x-bonus-scripts.md).

# Optional reading: Dependency compatibility

## Exercises

1. Remove the `pydantic` dependency by running `uv remove pydantic`
2. Use whichever method you prefer to add dependencies to your project and try to add and install the following two dependencies (remember the versions!):

  * `"pydantic<2"`
  * `"pydantic-settings>=1"`

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection
As you may have noticed, uv took a little bit longer this time, before failing with the message

```raw
  × No solution found when resolving dependencies:
  ╰─▶ Because only the following versions of pydantic-settings are available:
  [...]

      And because your project depends on pydantic<2 and pydantic-settings>=1, we can conclude that your project's requirements are unsatisfiable.

      hint: Pre-releases are available for `pydantic-settings` in the requested range (e.g., 2.0b2), but pre-releases weren't enabled (try: `--prerelease=allow`)
  help: If you want to add the package regardless of the failed resolution, provide the `--frozen` flag to skip locking and syncing.
```

This means that you have two dependencies that are *incompatible*.
Specifically, you want to add [Pydantic](https://docs.pydantic.dev/latest/) with a version less than 2.0.0.
However, all versions of [Pydantic settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) with version greater than or equal to 1.0 requires Pydantic version 2 or greater.
This will clearly not work: you cannot have both have a Pydantic version less than 2 and Pydantic version greater than or equal to 2!

A nice feature of uv is that it will check this for us so we don't accidentally end up with incompatible dependencies for our project.
If you use `uv add`, it takes it one step further and tries to find a compatible dependency to add to your project.
So when you tried to run `"uv add pydantic<2" "pydantic-settings>=1"`, uv tried to find versions of the dependencies that were compatible (with each other and already existing dependencies.)
This was not possible for `"pydantic-settings>=1"` and `"pydantic<2"`.
Luckily though, we don't rely on any outdated Pydantic features, so we can upgrade to Pydantic 2

## Exercises
1. Remove the pydantic and pydantic-settings dependencies from the `pyproject.toml` file. Add them again by typing `uv add pydantic pydantic-settings`.
2. Replace the code in your `pycon.py`-file with the code from the [`code/packaging-tutorial/src/packaging_tutorial/validated_pycon_with_config.py`](../../code/packaging-tutorial/src/packaging_tutorial/validated_pycon_with_config.py). How does this file differ from the original `pycon.py`-file?
3. Test that the code works by running the `get_charlas`-script with `uv run python scripts/get_charlas.py`

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection

The easiest way to resolve dependency problems is to try to delete all of your clashing dependencies and add them again.
This can work because uv will try to find the latest compatible version of your dependencies.
Thus, if you don't have any special requirements for your dependencies, then this approach can work.
However, if you for some reason absolutely MUST have a specific version of your dependencies, then you might be out of luck.

## Aside: dependencies in libraries and applications
Dependency compatibility is tricky business.
Generally, you want your *applications* to have completely fixed versions in the listed dependencies and your *libraries* to have as unconstrained versions as possible in the listed dependencies.
The reason for this difference is that we we want full control over the libraries we use in applications we develop (e.g. to avoid supply chain attacks) but we don't want to mandate which versions consumers of our libraries should use.
Managing versions is easier for dependencies that strictly adhers to [*semantic versioning (semver)*](https://semver.org/).
In those cases, you can change the dependencies in the `pyproject.toml`-file from `library==X.Y.Z` to `library>=X.Y,<X+1` (e.g. `httpx>=0.26,<1`).
However, strictly adhering to semver is difficult, and most libraries don't do this.
In this case, you can just removethe version pin altogether in the dependency list (or use `>=`-pins).
For example, you may use `httpx` or `httpx>=0.26.0` instead of `httpx==0.26.0`.
