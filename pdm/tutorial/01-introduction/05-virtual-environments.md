# Virtual environments with PDM

In the previous section, we saw how two dependencies can be incompatible.
But what if we have two different projects we are developing, and their dependencies are incompatible?
That shouldn't be a problem: each app could work by itself. 
However, if we just install the dependencies in the global Python installation, we cannot work on both applications at the same time!

Virtual environments come to the rescue: virtual environments are more or less separate Python installations isolated from the rest of your system.
These environments are incredibly useful as they let us develop our libraries and applications without worrying about messing up any other applications or libraries we have installed on our computer.

There are many different tools that can create virtual environments such as the builtin `venv` module, the slightly more powerful [`virtualenv`](https://virtualenv.pypa.io/en/latest/) module or `conda`.
However, you don't need to worry about that at all, because PDM takes care of creating and managing virtual environments for us!
(It uses `virtualenv` to manage dependencies by default, but you probably don't need to worry about those details)

## Exercises

> [!NOTE]
> You may need to replace python here with either py (Windows) or python3 (Linux and Mac)

> [!NOTE]
> If you're using the integrated terminal in VSCode, PyCharm or another "smart" code editor, then you may not see the system Python executable in exercise 1. and 6.

1. Run `python -c "import sys; print(sys.executable)"` in a terminal emulator (cmd or powershell) to see which Python executable Windows uses by default (the first result).
2. Run `pdm run python -c "import sys; print(sys.executable)"` to see which Python executable PDM uses by default. Is there any difference?
3. Activate the virtual environment by running `.venv\Scripts\activate` (Windows) or `.venv\bin\activate` (Linux/Mac OS)
4. Run `python -c "import sys; print(sys.executable)"` to see which Python executable Windows now uses by default
5. Deactivate the virtual environment by running `deactivate`
6. Run `python -c "import sys; print(sys.executable)"` to see which Python executable Windows now uses by default
7. Discuss with your neighbour: What are the benefits of using a different virtual environment for each project compared to using just one large environment for everything?

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection

When we run Python in a virtual environment, we use a Python executable that is different from when we run the system Python executable.
Moreover, if we want to run Python in the virtual environment, then we can either run `pdm run python` or activate it by first running `.venv\Scripts\activate` (Windows) or `.venv\bin\activate` (Linux/Mac OS) and then `python`.

## Specifying virtual environments in your IDE

Some IDEs (integrated development environments -- a fancy name for a code editor) let you specify a virtual environment for your projects, and by doing so, the IDE can provide better code completion and syntax highlighting.

### Specifying virtual environment in VSCode

To specify the virtual environment in VSCode, press <kbd>Ctrl</kbd><kbd>⇧ Shift</kbd><kbd>P</kbd> to get the command palette and write `Python: Select interpreter`.

### Specifying virtual environment in PyCharm
Press <kbd>Ctrl</kbd><kbd>Alt</kbd><kbd>S</kbd> to open settings and select **Project: <project name> | Python Interpreter**. Click **Add Interpreter** → **Add Local Interpreter** → **Virtualenv Environment** (PDM uses Virtualenv by default) and select the environment from the list (or browse for the correct environment if it doesn't appear).
For more info see [the official PyCharm documentation](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env).

## Optional reading: Installing new Python versions
If you work on many Python projects at once, then you may need to install multiple Python versions as well.
Your previous project might have used Python 3.12, but you want to use the latest features of Python 3.13!
Luckily, there's an easy way to get around this problem: the `pdm python install`-command.

You can, for example, use PDM to install the latest version of Python 3.13 by running `pdm python install 3.13`, which will download the Python 3.13 version of *[Python build standalone](https://github.com/astral-sh/python-build-standalone)* (originally developed by [Gregory Szorc (indygreg)](https://github.com/indygreg), but now maintained by Astral).
Python build standalone is a patched standalone version of CPython that can be copied around on your file system.
It has a couple of [behaviour quirks](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html) compared to the stock CPython, but likely nothing you will notice in practice.

## Next up
[Development dependencies and unit tests](../02-more-about-dependencies/06-unit-tests.md)
