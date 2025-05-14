# Lock files

An integral part of developing a Python package is keeping track of its dependencies, and, as we've already seen, making sure they are compatible.
The task of finding compatible set of dependencies, given the project requirements is called *locking*, and most major Python project management tools have a locking concept.

## Exercises
1. Open the `pdm.lock`-file. What does it contain? Can you find your dependencies here?
2. The `pdm.lock`-file contains many dependencies that you haven't explicitly added with `pdm add`. Why do you think this is?
3. Run `pdm export -o requirements.txt` and inspect the contents of the `requirements.txt`. What do you think it contains?
4. Delete the `requirements.txt`-file
5. Run `pdm list --tree` and inspect the terminal output. What does this represent?

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection
When you add dependencies to your project, you also need to install your dependencies' dependencies.
This is called indirect dependencies, and can be a source of much pain.
Whenever you add a dependency, you may add dozens of other dependencies you don't know about.
The lock file contains a full list of all these dependencies with information about what versions they require, and if PDM can successfully lock your project, you know that there exists a compatible set of dependencies -- even among all the indirect ones.

In fact, a very common type of lock file used to be the `requirements.txt`-file obtained from running `pip freeze` (or `pdm export`, etc.)
While this was commonly found before, we have more modern standards these days so we don't really need to use it anymore.
Still, it's useful to be aware that a `requirements.txt`-file can function as an absolutely minimal lock file.

Finally, we saw that while the lock file is useful for keeping a record of the dependencies, it is not meant for human consumption.
Rather, if you want to inspect the dependencies of a project, then you should probably look at a visual representation of the dependency tree.

## Note: Upcoming standard
Lock files were recently standardised in [PEP 751](https://peps.python.org/pep-0751/).
This is great news, as lock files are one of the final hurdles for truly being able to work with different packaging frontends (like uv, PDM, Hatch and Poetry) on the same project.
However, there is still a way to go before the different tools switch to this new format (and some may never switch completely).
Still, it's great to see that the standard has arrived after many years of work.
So, in the future, you may see `pylock.toml` as a common file in Python projects as well, together with the `pyproject.toml`!

## Next up
[Building your project](../03-building-and-publishing-packages/11-building-wheels.md)
