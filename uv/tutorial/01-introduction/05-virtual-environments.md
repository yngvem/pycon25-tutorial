# Virtual environments with uv

In the previous section, we saw how two dependencies can be incompatible.
But what if we have two different projects we are developing, and their dependencies are incompatible?
That shouldn't be a problem: each app could work by itself. 
However, if we just install the dependencies in the global Python installation, we cannot work on both applications at the same time!

Virtual environments come to the rescue: virtual environments are more or less separate Python installations isolated from the rest of your system.
These environments are incredibly useful as they let us develop our libraries and applications without worrying about messing up any other applications or libraries we have installed on our computer.

There are many different tools that can create virtual environments such as the builtin `venv` module, the slightly more powerful [`virtualenv`](https://virtualenv.pypa.io/en/latest/) module or `conda`.
However, you don't need to worry about that at all, because uv takes care of creating and managing virtual environments for us (with its own virtual environment implementation)!

## Exercises

> [!NOTE]
> You may need to replace python here with either py (Windows) or python3 (Linux and Mac)

1. Run `python -c "import sys; print(sys.executable)"` in a terminal emulator (cmd or powershell) to see which Python executable Windows uses by default (the first result).
2. Run `uv run python -c "import sys; print(sys.executable)"` to see which Python executable uv uses by default in your project. Is there any difference?
3. Activate the virtual environment by running `.venv\Scripts\activate` (Windows) or `.venv\bin\activate` (Linux/Mac OS)
4. Run `python -c "import sys; print(sys.executable)"` to see which Python executable Windows now uses by default
5. Deactivate the virtual environment by running `deactivate`
6. Run `python -c "import sys; print(sys.executable)"` to see which Python executable Windows now uses by default
7. Discuss with your neighbour: What are the benefits of using a different virtual environment for each project compared to using just one large environment for everything?

<img src="../../../assets/post_it_yellow.svg" alt="Illustraiton of a pink post it note" width="50px" />

## Reflection

When we run Python in a virtual environment, we use a Python executable that is different from when we run the system Python executable.
Moreover, if we want to run Python in the virtual environment, then we can either run `uv run python` or activate it by first running `.venv\Scripts\activate` (Windows) or `.venv\bin\activate` (Linux/Mac OS) and then `python`.
We recommend using `uv run`, as that will sync your environment with the `pyproject.toml`-file as well, but use whichever method you prefer.

> [!IMPORTANT]
> uv has a couple of very strange behaviours, which is there for speed.
> First and foremost, it tries to install libraries by hardlinking them to a specific local installation cache.
> That was a lot of fancy words, but essentially, it means that if you open a library installed in a uv virtual environment and edit it, then you will edit that library for ALL uv environments that have installed it!
> This will usually not be a problem for beginner programmers, but it's not unusual for more experienced programmers to make small edits to libraries while debugging, and if you do that with uv, then you should be aware that you are modifying the global installation cache.
> In other words: uv environments are not completely isolated!
> 
> If you want to avoid this behaviour, you can set the environment variable `UV_LINK_MODE=copy`.

> [!IMPORTANT]
> [uv will not compile `.py`-files to `.pyc`-files](https://pythonspeed.com/articles/faster-pip-installs/) (those in the `__pycache__`-directories).
> These are files that Python generate whenever it runs a script or imports a module, and creating them is a bit time-consuming.
> Python will therefore helpfully cache these `.pyc`-files in the `__pycache__`-directories, and only update them when the corresponding `.py`-files are updated.
> Furthermore, Pip autogenerates these `.pyc`-files for every module in every package you install.
> Uv, on the other hand, skips this step, as it makes installing packages slower, and a key feature of uv is lightning-fast environment setup ([Poetry also skips this step](https://github.com/python-poetry/poetry/pull/6205)).
> Also, you can disable bytecode compilation in pip as well by running `pip install --no-compile {package}`.
> 
> When you're developing, this doesn't matter much, however it means that if you use `uv` to generate containers that you deploy at cloud services, then you should probably include the `--compile-bytecode`-flag, which makes sure that the `.pyc`-files are generated upon installation, not at runtime.
> Otherwise, you'd have to pay the bytecode compilation price every time you start a container, instead of when you build the container image.

## Specifying virtual environments in your IDE

Some IDEs (integrated development environments -- a fancy name for a code editor) let you specify a virtual environment for your projects, and by doing so, the IDE can provide better code completion and syntax highlighting.

### Specifying virtual environment in VSCode

To specify the virtual environment in VSCode, press <kbd>Ctrl</kbd><kbd>⇧ Shift</kbd><kbd>P</kbd> to get the command palette and write `Python: Select interpreter`.

### Specifying virtual environment in PyCharm
Press <kbd>Ctrl</kbd><kbd>Alt</kbd><kbd>S</kbd> to open settings and select **Project: <project name> | Python Interpreter**. Click **Add Interpreter** → **Add Local Interpreter** → **Virtualenv Environment** and select the environment from the list (or browse for the correct environment if it doesn't appear).
For more info see [the official PyCharm documentation](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env).

## Optional reading: Installing new Python versions
If you work on many Python projects at once, then you may need to install multiple Python versions as well.
Your previous project might have used Python 3.12, but you want to use the latest features of Python 3.13!
Luckily, there's an easy way to get around this problem: the `uv python install`-command.

You can, for example, use uv to install the latest version of Python 3.13 by running `uv python install 3.13`, which will download the Python 3.13 version of *[Python build standalone](https://github.com/astral-sh/python-build-standalone)* (originally developed by [Gregory Szorc (indygreg)](https://github.com/indygreg), but now maintained by Astral, the makers of uv).
Python build standalone is a patched standalone version of CPython that can be copied around on your file system.
It has a couple of [behaviour quirks](https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html) compared to the stock CPython, but likely nothing you will notice in practice.

## Next up
[Development dependencies and unit tests](../02-more-about-dependencies/06-unit-tests.md)
