# Automatic code quality control on GitHub

While pre-commit hooks are a great way to prevent us from committing code with style errors, they are insufficient to prevent bugs.
We cannot run our full test suite before every commit.
If we did, we could lose all momentum while coding and end up never committing at all.
Instead, we set up a continuous integration (CI) pipeline that runs the test suite and linter checks every time we push code to GitHub.

The nice thing about these pipelines is that you can set them up so all pull requests must pass the CI pipeline before it can be merged.
There are many systems we can use to set up such pipelines, but perhaps the most common is GitHub's builtin system: GitHub Actions.

## Exercises

1. Create a directory in your project root named `.github`. Create a new directory called `workflows` inside there again and a file named `ci.yml` inside the `workflows directory`. Copy the below configuration into that file.

```yaml
name: Run test

on: [push, pull_request]

jobs:
  run-tests:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Setup PDM
        uses: pdm-project/setup-pdm@v4
        with:
          python-version: 3.13
          cache: true
      - name: Install project
        run: pdm install
      - name: Run unit tests
        run: pdm run pytest
```

1. What do you think the `on: [push, pull_request]` line does?
1. What is the difference between `run`-steps and `uses`-steps?
1. Commit the file and push to GitHub. Open the GitHub repository in your browser and have a look at the `Actions` tab. Do you see a job? If so, press it and have a look at its log. Can you tell what happens?

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection
We have now set up a very simple CI job where the unit tests are run automatically every time someone pushes to GitHub and every time someone opens or make changes to a PR.
You can even [create badges](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/adding-a-workflow-status-badge) that show if the CI-pipeline fails or succeeds so anyone can see the CI-pipeline status from your README file!
However, pay attention to how we set up these pipelines: we use `uses`-steps and `run`-steps.
The `run`-steps simply run terminal commands, while the `uses`-steps are a bit "scarier": They run jobs defined in external GitHub repositories.
We'll look a bit more at that later, but first, let's improve our CI pipeline a bit.

## Exercises

1. Add the following configuration right under the `run-tests:` line and update the `runs-on: ubuntu-latest` line so it says `runs-on: ${{ matrix.os }}` instead. What do you think this does?
```yaml
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
```
2. Commit and push your changes to see how the new pipeline runs. Are there any changes compared to last time the pipeline ran?
3. Update the pipeline so it also runs with multiple Python versions (e.g. '3.11', '3.12', and '3.13'). If you're stuck, then you can check out the [GitHub Actions docs](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow). Commit and push the code to see if you succeeded.
4. Add a new step before the unit tests are run where you run the command `pdm run ruff check . && pdm run ruff format --check .`. Commit and push the code to see if you succeeded. What do you think this command does?

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection

We now have a CI-pipeline that runs our tests on several Python versions AND several operating systems.
This gives us confidence that the code we write is robust and will work for many users.
However, remember what we said earlier?
We're running arbitrary code from other repositories in our CI-CD pipeline!

## Exercises

1. Visit https://github.com/pdm-project/setup-pdm and discuss what you think this repository contains with your neighbour.
1. Discuss with your neighbour: what do you think can happen if a nefarious actor gains access to the `pdm-project/setup-pdm` repository? Is there any way for us to protect ourselves from such a scenario?
1. Visit https://github.com/pdm-project/setup-pdm/tree/v4 and press the commit hash link (it should be a string of seven numbers and letters (a-f) below the <kbd>\<\> Code</kbd> button). Copy the hash from the URL you just visited (the URL should have the following format: https://github.com/{user/org}/{repo}/commit/{hash}). It should be a long string of seemingly random letters and numbers (e.g. `deb8d8a4e2a03aabcef6f2cc981923fc6b29ef99`). 
1. Update the `uses: pdm-project/setup-pdm@v4`-line so it says `uses: pdm-project/setup-pdm@deb8d8a4e2a03aabcef6f2cc981923fc6b29ef99`. Discuss with your neighbour: Why should you do this with your CI-pipelines? And is there any considerations regarding when you should pin based on the Git hash?

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection

We have now updated our pipeline to use a specific commit of the `setup-pdm` step.
This is an immutable reference, so we can feel pretty confident that the contents of the action won't suddenly change and inject malware in our code.
It is, in general, good practice to [pin your CI/CD pipelines based on Git hashes](https://julienrenaux.fr/2019/12/20/github-actions-security-risk/), and you can set up [Dependabot](https://docs.github.com/en/code-security/dependabot) to keep your dependencies up-to-date (but we do not have experience with that).
Still, it might be OK to use non-static references like tags, on certain workflows where you 100% trust the author (e.g. company-internal workflows).
So, when you use GitHub actions, you should be aware that [they have been used as threat vectors](https://blog.pypi.org/posts/2024-12-11-ultralytics-attack-analysis/), but in general, the safety they provide in letting you run a CI pipeline outweighs the potential risk they bring.
Furthermore, if you want to protect yourself, then you can use [zizmor](https://woodruffw.github.io/zizmor/) to scan your GitHub actions for potential security flaws (which we will look at later).

## Next up
[Setting up continuous delivery (CD) to automatically push changes to PyPI](./17-publishing-with-github.md)
