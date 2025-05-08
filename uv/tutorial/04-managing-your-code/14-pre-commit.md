# Pre-commit hooks

While linters are great for making a codebase easier to read, they are also easy to forget.
This is why you often find commits with the message "Run ruff", "Run black", "Run flake8", etc.
Instead, we should have Git automatically lint our code before every commit.
If there is anything the linters want to change, then the commit should not succeed, and we should be asked to update the code.

Luckily, this is possible, and the main tool for running commands that verify your code before committing is called "pre-commit".

## Exercises

1. Check if you have pre-commit installed on your system by running `pre-commit -h`. If you get the help message, then pre-commit is installed. If not, then you can install it by running `uv tool install pre-commit` (this will install pre-commit as an application globally on your system, not just for this project).
1. Run the command `pre-commit sample-config` to get a sample pre-commit file. Copy the output into a new file in your project root that you name `.pre-commit-config.yaml`.
1. Install your pre-commit hooks by running `pre-commit install`
1. Run your pre-commit hooks by running `pre-commit run --all`. What do you think just happened (look at your `.pre-commit-config.yaml`-file)?
1. If any files were changed (you can e.g. check this by running `git status`), then stage and commit them with the commit message "Run pre-commit"
1. Open a file, and add a new line with a comment and a blank space at the end of it. Save the file, stage it, and try to commit it. What happened?
1. Stage the file again and commit it. Discuss with your neighbour: what do you think just happened?

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection
Pre-commit is an amazing tool.
In the `.pre-commit-config.yaml`-file, you specify a set of *hooks* that runs automatically every time you try to commit a change.
By default, these hooks run only on the staged files, and any unstaged files will be ignored.
If the hooks exit successfully, then you can commit the changes. 
If not, then the hooks will try to fix the errors automatically, updating all your staged files (but it will not stage the changes).
You can then inspect the changes, stage them and try to commit again.

Also, we used `uv tool` to install `pre-commit`, which is a good to install Python applications globally on our systems (i.e. it's not for project-specific tools).
If you're familiar with apt or homebrew, then you can think of `uv tool` kind of like those programs, except `uv tool` is for applications written in Python.

## Exercises

1. Why do you think pre-commit doesn't automatically stage fixes as well?
2. Open the `.pre-commit-config.yaml`-file and add the following lines:
```
-   repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.11.6
    hooks:
    -   id: ruff
    args: [ --fix ]
    -   id: ruff-format
```
3. Stage and commit the updated `.pre-commit-config.yaml`-file.
4. Discuss with your neighbour: What do you think the lines you added in the previous exercise lines do?
5. Add the following code to `src/{package_name}/pycon.py` (be exact and keep the weird formatting):
```python

def print_future_sessions() -> None:
    sessions = get_sessions(
    )
    for session in sessions:
        print( session,  session.start )
```
6. Stage and commit the updated `pycon.py`-file. Did it pass the pre-commit hooks?
7. Stage the fixed file and commit again

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />


## Reflection

We have now added pre-commit configuration so that every time we commit a file, it's passed through Ruff (which we learned about [earlier](../02-more-about-dependencies/09-static-code-checkers.md)), and only if it passes the linter checks do we allow the commit to go through.

## Next up
[Sharing our code on GitHub](./15-using-github.md)
