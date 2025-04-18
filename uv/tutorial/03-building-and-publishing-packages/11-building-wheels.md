# Building your package

Recall that we, [in the beginning of this tutorial](../01-introduction/02-pip-internals.md), looked at how pip installs packages: By downloading and extracting a wheel.
In reality, pip can work with both wheels and source distributions, and we'll look a bit closer at these now that we are ready to build our package.

In other words, we are ready to gather all the parts we need to import our library and place them into a nice bundle that other people can install and use.
You could do this yourself, but realistically, what you want to do is to use a *build backend* that can do this automatically.
A build backend is essentially a piece of code that follows a specification called [PEP-517](https://peps.python.org/pep-0517/), which specifies how tools should convert code into installable bundles.

## Exercises

1. Build your package by running `uv build`. What do you think happened now?
2. Look inside the `dist`-directory. How many files do you see there?
3. Unzip the source distribution into a directory called `dist/sdist`, e.g. by running `uv run python -m tarfile -e dist/{sdist_name}.tar.gz dist/sdist`.
4. Unzip the wheel file into a directory called `dist/wheel`, e.g. by running `uv run python -m zipfile -e dist/{wheel_name}.whl dist/wheel`.
5. Inspect the `dist/sdist` and `dist/wheel` directories. Are there any differences? If so, what are they?
6. Open the `.venv/lib/python3.12/site-packages` (Linux and Mac) or the `.venv/Lib/site-packages` (Windows) directory. Compare the folder names in this directory to the folder names in the extracted of the wheel and source distribution. Can you see any similarities?

<img src="../../../assets/post_it_yellow.svg" alt="Illustraiton of a pink post it note" width="50px" />

## Reflection

By running `uv build`, we trigger the build backend to make a *source distribution* and a *wheel* - the file types we looked at earlier in this tutorial.
The difference between wheels and source distributions is subtle, especially when we only have Python code, but it's worth knowing.
A source distribution is the source code combined with instructions on how to build it stored in a *tarball* (you can think of a tarball as a zip file, while not 100% accurate, it's close enough) so users can build and install it themselves.
It's essentially a snapshot of our code repository.
There is therefore, essentially, nothing that happens when you make the source distribution, it just selects a collection of files, puts them in an archive and that's about it.
A wheel, on the other hand is an installable bundle that can be extracted directly into the site-packages directory (a place Python looks for imports).
Since we are working on a pure Python project, the wheel is very similar to the source distribution, but the `pyproject.toml`-file is parsed and the metadata is extracted into the `{package_name}-{version}.dist-info`-folder.

Where wheels really shine is for extension modules written in other languages (like C or Rust).
In that case, the source distribution will contain the C or Rust files, and the user would need to compile it themselves, while the wheel would contain pre-compiled binaries for specific platforms.
This means that it's much easier to install wheels than source distributions, and you should always provide them if possible.

## Exercises

1. Let's change the build backend. Open the `pyproject.toml`-file and modify the `[build-system]` to use `setuptools` instead of Hatchling. Specifically, modify it so it says `requires = ["setuptools"]` and `build-backend = "setuptools.build_meta"` (Note: Setuptools isn't better than Hatchling, just different. So unless you have some specific advanced requirements, we recommend just sticking to the defaults here, but you should still know how to do it). 
2. Build the project again. What do you think was different this time around?

<img src="../../../assets/post_it_yellow.svg" alt="Illustraiton of a pink post it note" width="50px" />

## Reflection

The build backend is the tool that actually creates the wheel and source distribution.
What we just did was switching out the build backend to use [Setuptools](https://setuptools.pypa.io/en/latest/setuptools.html) instead of Hatchling, the buildsystem made for [Hatch](https://hatch.pypa.io/).
This means that instead of calling `hatchling.build.build_wheel('dist/')` and `hatchling.build.build_sdist('dist/')` to create the wheel and source distribution, uv called `setuptools.build_meta.build_wheel('dist/')` and `setuptools.build_meta.build_wheel('dist/')` when you ran `uv build`.
This might seem complicated, but luckily, unless you have good reasons, it doesn't really matter if you choose Hatchling, Setuptools or PDM as the build backend.
Still, there are differences, but you can switch the build backend when you find a reason to.
Until then, just stick with the defaults.

## Next up
[Publishing your package to PyPI](./12-publishing-packages.md)
