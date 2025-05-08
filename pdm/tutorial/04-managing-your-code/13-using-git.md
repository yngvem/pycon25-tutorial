# Using Git

This part functions as an extremely quick introduction to creating a [Git](https://git-scm.com/) repository.

We've all been there: we have made some changes to some files, but we don't know if we prefer them to the previous versions. So what do we do?
We save the file as `{filename}_v2.py`, `{filename}_v2-2.py`, `{filename}_v3.py` `{filename}_final.py` and `{filename}_old.py.bak`.
But what's the difference between `{filename}_v2-2.py` and `{filename}_v3.py`? And do we really need all this clutter in our codebase?
The answer is of course no -- and the solution: a version control system (VCS)/source control management tool (SCM-tool) named Git.

Simply put, Git is a tool that makes it easy to have multiple versions of the same code.
It facilitates sharing and makes it easy (or, let's face it, easier) to merge changes from multiple parties.

We won't cover much here, just the absolute basics (and maybe not even that).
A complete introduction to Git is, unfortunately, outside the scope of this tutorial. 
For a more thorough introduction to git, we refer to the excellent [Introduction to Sprinting](https://github.com/chalmerlowe/intro_to_sprinting/) tutorial by Chalmer Lowe, the [How Git Works](https://wizardzines.com/zines/git/) Wizard Zine by Julia Evans, and the [Pro Git book](https://git-scm.com/book/en/v2).

## Exercises

1. Run `git init` in your project root to initialize a Git repository.
1. *Stage* all files in your project root and all subdirectories by running `git add *`
1. *Commit* the changes by running `git commit -m "Initial commit"`
1. Check that the files are committed by running `git log` followed by `git status`. What do you think these commands do?

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection

You have now initialized a Git repository and committed some files.
Essentially, this means that Git knows about the files and knows to track their changes.
If you make any change to one file (multiple files), then you can *commit* it (them), telling Git that "this is the latest version of this file".
Together with the commit, you write a message, which typically is a short description of what you did, and maybe why did it.
Then, if you ever want to see old versions of your files, you can write `git log` to go through all changes and `git checkout` to "go back in time" and see the state of your repository at a given commit.

## Exercises

1. Modify a file (e.g. by adding a comment). Run git status again. What do you see?
1. What do you think the command `git diff` does? Run it and see if you were right (PS. If you're stuck in the diff view, then you can exit it by pressing <kbd>q</kbd>).
1. *Stage* the file you changed by running `git add {path/to/file}.`
1. *Commit* the file by running `git commit` and write a descriptive message.
1. Have a look at the updated git log by running `git log`.

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection
You have now updated your file and committed the changes.
In doing so, you first had to stage the file, which is akin to telling Git "These are the changes I want to store."
Then, you commited the changes, essentially telling Git: "Store a snapshot of the files as they were when I staged them."

## Next up
[Using pre-commit hooks to automatically check the code before committing](./14-pre-commit.md)
