# Python project packaging: from zero to hero

Packaging your code is an essential skill that empowers you to share your Python projects with the world.
However, the packaging process can appear complex and overwhelming, and it can be difficult to know where to begin.

This is meant as a hands-on tutorial to clarify what packaging is and how good packaging tools can help you share your code with others.
We’ll cover how to structure projects and follow best practices for project layouts, specify project metadata, make your package installable, and publish it to PyPI. While the materials are meant for a hands-on tutorial, they can also be used for self study.

We'll use uv in this tutorial, but there are also materials for PDM if you'd prefer that.
Also, most of the topics covered will also apply to other packaging tools like Hatch or Poetry.
Moreover, while the correct technical term for what we'll look at here is [distribution packages](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package), we'll just use the word package (despite it's [more general meaning](https://docs.python.org/3/glossary.html#term-package)) as it's commonly used as a shorthand for distribution package (see e.g. PEP [458](https://peps.python.org/pep-0458/), [480](https://peps.python.org/pep-0480/) and [668](https://peps.python.org/pep-0668/)).

## Overview

This workshop will be a hands-on way to explore the following concepts:

* What a (distribution) package is
* How pip install packages
* What a wheel file is
* How you can create packages
* What the preffered way to specify project metadata is

However, the workshop will **not** cover *application packaging*, which is usually done with a container system like Docker, Podman or Kubernetes.
Still, the concepts will be useful for mastering application packaging, as most of the concepts covered here are necessary for application packaging as well.
In fact, a common way to deploy an application is to first package it as a library and then install that library in a container image. 

## Prerequisites

These materials are meant both for beginner coders who are just getting ready to share their code and experienced developers who haven't looked at the Python packaging ecosystem for a couple of years and want a refresher.
They assume that you are sort of familiar with Python and that you are somewhat familiar using the terminal (CMD/Bash/Zsh/Powershell/etc). It will also be beneficial to know the basics of Git for the later parts of the tutorial, but it's not a requirement. Though, if you're attending the live workshop, then we can help you along!

Also you should know how to use a code editor like VSCode, PyCharm or Sublime Text.

> [!NOTE]
> If you cannot install uv on your machine, then you can fork our [base project repo](https://github.com/yngvem/pycon25-tutorial-project), which as a devcontainer with uv installed.

## Next
[Introduction (uv)](uv/tutorial/01-introduction/01-workshop-introduction.md) or [Introduction (pdm)](pdm/tutorial/01-introduction/01-workshop-introduction.md)

## Copyright
© Yngve Mardal Moe & Marie Roald (2025-)
