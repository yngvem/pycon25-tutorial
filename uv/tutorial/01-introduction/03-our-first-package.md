# Creating an installable Python package
We are now ready to make our first package.
Luckily, we don't need to do this manually -- many amazing people in the Python community spend their time maintaining tools that do the heavy lifting for us.
We will use a modern, feature-packed and standard complying packaging tool: [uv](https://docs.astral.sh/uv/), but there are many other great tools too, like [PDM](https://pdm-project.org/latest/), [Hatch](https://hatch.pypa.io/latest/), [Poetry](https://python-poetry.org/) and [Setuptools](https://setuptools.pypa.io/en/latest/).

What we learn in this tutorial will easily transfer across different packaging tools, as all solve more or less the same problem: how to distribute Python packages. 
If you want a comparison of the different tools for packaging in Python, then we recommend [this excellent writeup by pyOpenSci](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-build-tools.html).

## Exercises

1. Install uv (e.g. by following the official [installation instructions](https://docs.astral.sh/uv/getting-started/installation/)).
2. We will now create a new empty Python project with uv. Create a folder with the name you want your project to get, e.g. `packaging-tutorial-{myname}`, navigate your terminal to that directory, and run `uv init --package`.
3. Where do you think you should should put the source code for your package? 
4. Open the pyproject.toml file. Can you find where the following pieces of information are stored?

    * The author's name
    * The author's e-mail
    * The version number
    * The minimal Python version required to use your package

5. What are the dependencies of your package?
6. Discuss with your neighbour: what do you think the purpose of the `__init__.py`-file in the `src/{PACKAGE_NAME}`-directory is?

<img src="../../../assets/post_it_yellow.svg" alt="Illustraiton of a pink post it note" width="50px" />

## Reflection

We have now learned how we can create a new package with uv.
By default, uv uses a [src-layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) for libraries, which has some benefits compared to using a flat layout (see e.g. [this blog post](https://hynek.me/articles/testing-packaging/#src), [this blog post](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure) or [this discussion](https://github.com/pypa/packaging.python.org/pull/1150)).
Additionally, uv stores the package metadata in an easy-to-read pyproject.toml file that follows the [official PEP-621 specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/).

We have also looked at the `__init__.py`-file.
This is a special file that tells Python that the `src/{PACKAGE_NAME}`-directory should be importable.
Strictly speaking, it turns the directory into a [package](https://docs.python.org/3/tutorial/modules.html#packages), but that package is confusingly a bit different from what people normally talk about when they talk about packaging.
The file does several things, but you can conceptualize it as two things: it makes it possible to do "[relative imports](https://docs.python.org/3/reference/import.html#package-relative-imports)", and its the file you import when you write `import {PACKAGE_NAME}`.

## Next up
[Dependencies and creating your first package](./04-dependencies.md)
