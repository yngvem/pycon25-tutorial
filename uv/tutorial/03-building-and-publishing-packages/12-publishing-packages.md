# Publishing your package to PyPI

Once we've created installable wheels and source distributions, we need to share them.
This is typically done by uploading them to the Python Packaging Index (PyPI).
Technically, PyPI is a *package repository*, and while PyPI is the most common packaging repository, many others exist.
For example, your employer might have a copy of PyPI internally that you can upload internal packages to.
In this part of the tutorial, we'll upload our package to a package repository named Test PyPI, which is a clone of PyPI where we can mess around without cluttering the official PyPI.

## Exercises
1. If you haven't already, register a new user for Test-PyPI at https://test.pypi.org/
1. Navigate to your account settings on Test PyPI and create an API-token with full access to your account. Store this token somewhere safe (preferably in a password or credential manager).
1. Publish your package by running `uv publish --publish-url https://test.pypi.org/legacy/`. Use the username `__token__` and the token you created earlier as password.
1. Navigate to your account settings on Test PyPI and delete the API token you created.
1. Navigate to https://test.pypi.org/ and search for you package.
1. Navigate to https://test.pypi.org/simple and see if you find your package. What do you think this "simple view" is used for?
1. Navigate to https://test.pypi.org/simple/{your-package-name}/, what do you see here?

<img src="../../../assets/post_it_yellow.svg" alt="Illustraiton of a pink post it note" width="50px" />

## Reflection
By now, you have created a user at a package registry and pushed code there that anyone can install.
Moreover, you might have gotten a deeper understanding of how pip works: it finds projects by parsing a simple HTML file and downloads and installs wheels by following the links.
This is VERY similar to how we could do it manually, but luckily, we don't need to.

If you're interested in the specifics of PyPI and how it's built up, then you can check out the [PyPI documentation](https://docs.pypi.org/api/index-api/), or the HTML repository specs in [PEP 503](https://peps.python.org/pep-0503/) (there is also a JSON-spec that you can use if you want to create your own package repository: [PEP 691](https://peps.python.org/pep-0691/)).

## Exercise (Optional)
1. Use what you've learned so far to set up one of your own project to use uv.

<img src="../../../assets/post_it_yellow.svg" alt="Illustraiton of a pink post it note" width="50px" />

## Next up
[Using git to keep track of our code](../04-managing-your-code/13-using-git.md)
