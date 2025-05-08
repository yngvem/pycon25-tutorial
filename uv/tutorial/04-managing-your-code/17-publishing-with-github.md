# Continuous delivery with GitHub Actions

We now have a continuous integration pipeline that automatically checks if new code can be included in the next release.
However, we still don't have a good way of doing a release!
We need to manually clone the repository, build wheels and source distributions and push them to PyPI (remember your token!), which is an annoying workflow.

What we want instead, is for the release to happen automatically any time we add a tag on the format `v*.*.*` to our GitHub repository.
This is a form of continuous delivery (CD), and luckily, there's a way to do just that with GitHub actions!
And what's more, we don't even need to set up tokens.

## Exercises

1. Set up your GitHub repository as a trusted publisher on Test PyPI. To do so, navigate to the project management page on Test PyPI (https://test.pypi.org/manage/project/{project-name}/releases/), press the publishing button on the left and add a GitHub trusted publisher.
2. Create a new GitHub actions file name `.github/workflows/publish.yml` with the following content
```yaml
name: release

on:
  push:
    tags:
      - "v*.*.*"

permissions:
  id-token: write

jobs:
  build-and-publish:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Setup uv
        uses: astral-sh/setup-uv@v6
        with:
          python-version: 3.13
          enable-cache: true
      - name: build package
        run: uv build
      - name: Publish package distributions to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          repository-url: https://test.pypi.org/legacy/
```
3. Modify the pipeline so the unit tests and linting checks are run before the release. What do you think will happen if you add a tag to a commit that doesn't pass the linter checks or unit tests?
4. Commit and push the new pipeline. In your browser, navigate to your GitHub repository and press the "Releases" button on the right.
5. Open `src/{package_name}/__init__.py` and add the line `__version__ = "0.2.0"`. Then, open the `pyproject.toml`-file and update the version number to "0.2.0" as well. Commit and push these changes. 
6. In the GitHub repository: press the "Make a release button" (or "Draft a release" if you've already made one) on the right-hand side of your project's front page and make a release with the tag `v0.2.0`. Check if your CD-pipeline runs.

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection

You have now set up CI-CD pipelines for your project with CI-pipelines that check if your code follows your coding standards and CD-pipelines that automatically publish your code to PyPI whenever you make a new version!

However, the downside of this setup is that it still requires us to remember many steps whenever we want to publish a new version of our package: Update the `__version__` variable in `__init__.py`, update the `version`-field in `pyproject.toml`, commit, push and make a release.
A much easier way would be if Python, somehow, could automatically set the version based on the tag alone.
While no build backends natively support this, most still have plugins that enable *dynamic versioning*.

## Exercises

1. Update `__init__.py` so it contains the following
```python
import importlib.metadata

__version__ = importlib.metadata.version(__name__)
```
2. Modify the `build_system` table of `pyproject.toml` so it contains the following (what do you think this change does?):
```toml
[build-system]
requires = ["setuptools", "setuptools-scm"]
build-backend = "setuptools.build_meta"

[tool.setuptools_scm]
```
3. Delete the `version` field in the project table of `pyproject.toml` and add the field `dynamic = ["version"]`. What do you think this signifies?
4. Commit and push your code
5. Run `git fetch --tags` to get all tags from GitHub.
6. Install the project again with `uv install`. Which version are you currently on?
7. Add the tag `v0.3.0` by running `git tag v0.3.0`. Which version of your library do you think will be installed when you run `uv sync` now? Run `uv sync` and check if you were right.
8. Push the tag to GitHub with `git push origin tag v0.3.0`. Go to GitHub and create a release with this tag.
9. Check if the CD-pipeline runs. Once it has succeeded, check `test.pypi.org` to see if you can find the latest version of your code.

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection

You have now set up dynamic versioning for the package, with the version number automatically updating based on the git tag.
To do this, we first updated the `__init__.py`-file so it fetched the version from the metadata of the package (which is created when the package is built). 

Then, we updated the build system to use setuptools with the `setuptools-scm` plugin.
This plugin automatically fetches the version from Git tags.
The final thing we had to do to enable dynamic versioning was to remove the version field from `pyproject.toml` and add the `dynamic = ["version"]` field.
This tells the build system that the version is dynamic and should be generated at build time.

While we can create new releases very easily, there are still things to consider, specifically regarding security.
With CD, we must be extra careful that no one can hijack our CD-pipeline, as that can lead to our name being used to spread malware.
To avoid this, we can use a GitHub Actions security scanner tool named "[Zizmor](https://woodruffw.github.io/zizmor/)", which became popular after a clever pipeline injection on the popular Ultralytics package for computer vision (more details are available [here](https://blog.yossarian.net/2024/12/06/zizmor-ultralytics-injection)).

## Exercises
1. Add `zizmor` as a development dependency and run it on your workflows (try both normal mode and pedantic mode with `zizmor -p`). Read about the warnings and fixes on the [audit rules page of Zizmor's documentation](https://woodruffw.github.io/zizmor/audits/)
2. Resolve all Zizmor findings (decide if you want pedantic mode or normal mode).
3. Add the [Zizmor pre-commit hook](https://github.com/woodruffw/zizmor-pre-commit) to `pre-commit-config.yaml`
4. Add Zizmor to your CI-workflow.

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection

We have now secured our CI-workflows with Zizmor as well, so now, we can feel confident that we are following best practices regarding workflow security.

## Optional: build native wheels for many platforms with `cibuildwheel`

If you are publishing an extension module (i.e. a library with compiled code from languages like C, C++ or Rust), then you'd ideally want to provide pre-compiled wheels for as many platforms and Python versions as possible.
Luckily, PyPA provides a tool that helps us do exactly that: [`cibuildwheel`](https://github.com/pypa/cibuildwheel).
So it might be worthwhile to check that out if you are publishing an extension module!

## Next up
[A summary of what we've learned](./18-summary.md)
