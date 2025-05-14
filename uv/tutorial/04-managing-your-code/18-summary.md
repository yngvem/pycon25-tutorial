# Summary

Now, you are pretty much up-to-date on the modern packaging standards in Python.
You should know how to organise your code in a good way, that the `pyproject.toml` file is organised in four parts: The `project` table with package metadata, the `dependency-groups`-table with development dependencies, the `build-backend` table, which parametrises how to build the package and the `tool` table, which parametrises other utilities you use while you're developing your package.
Moreover, you've learned to use the modern project management tool, uv and how uv plays together with the python packaging ecosystem.

You have also learned about tools that make it easier to make high-quality Python packages, like pytest (with a couple of plugins) and Ruff, and how you can use pre-commit hooks to make Ruff run automatically when you commit and how to set up a CI-pipeline that runs unit tests automatically when you push to GitHub.

Finally, you've learned about building your package, the difference between a wheel and a source distribution, and how to publish your packages to PyPI, both manually and automatically through a CD-pipeline (that you secured with Zizmor).

What we haven't really looked at is how to build Python extension modules (i.e. modules written in other languages, like C, C++, Fortran or Rust).
While this can be very useful in certain circumstances, building such packages also requires knowledge about the build systems commonly used with these extension modules.
However, if you are interested in making extension modules, then you can still use uv -- you just need to set the correct build backend.
Here are some resources for further reading about building extension modules for Python:

 - [The Python Packaging User Guide's recommendations on build systems](https://packaging.python.org/en/latest/guides/tool-recommendations/#build-backends)
 - [The Meson build system for C, C++, Fortran, etc.](https://mesonbuild.com/meson-python/)
    - Meson is, for example, used to build [NumPy](https://numpy.org) and [SciPy](https://scipy.org).
 - [Scikit-build-core (wrapping CMake projects for Python)](https://scikit-build-core.readthedocs.io/en/latest/)
 - [Maturin](https://www.maturin.rs) and [PyO3](https://github.com/PyO3/pyo3) for extension modules written in Rust.
    - Maturin is, for example, used to build [Pydantic](https://docs.pydantic.dev/latest/).
 - [PyOpenSci's quick introduction to extension modules](https://www.pyopensci.org/python-package-guide/package-structure-code/complex-python-package-builds.html)
