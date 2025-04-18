# Using GitHub

In this part of the tutorial, we'll look at how to use [GitHub](https://github.com/) to host your code.
While the tutorial is for GitHub, there are a vast amount of similar tools you can use ([GitLab](https://gitlab.com/), [Atlassian BitBucket](https://bitbucket.com), [CodeBerg](https://codeberg.org/) and [GitTea](https://about.gitea.com/)).
The reason we use GitHub here is that it's the most popular tool with ready-built components that makes it easier to upload your code to PyPI.

## Exercises

1. Create a new repository on GitHub, name it {{name-packaging-tutorial}}. Initialise it as an empty repository, and **DO NOT** press the "Include README file" option.
1. Add the GitHub repository as a *Git remote* by running `git remote add "origin" {remote-url}`, where `{remote-url}` either is the HTTPS or SSH URL. To find this URL, press the green <kbd>\<\> Code</kbd> button on your GitHub repository.
1. Push your changes to GitHub by running `git push --set-upstream origin main`.
1. Open your repository on GitHub and validate that your updates are there.

<img src="../../../assets/post_it_yellow.svg" alt="Illustraiton of a pink post it note" width="50px" />

## Reflection

You have now uploaded your code to GitHub so other people can clone it.
You did this by first creating an empty repository on GitHub.
Then, you added that repository as a *remote* to your local Git repository, which essentially means that Git knows that it can find a copy of the code on GitHub.
However, changes aren't synchronised automatically.
Instead, you must explicitly *push* changes, telling Git to upload them to GitHub.
If there are no new changes on GitHub that you don't have locally, then the code is pushed.
Otherwise, you will need to merge the changes into one coherent repository.
We will not have time to go into how that's done here and refer, e.g. to Chalmer Lowe's [Introduction to Sprinting tutorial](https://github.com/chalmerlowe/intro_to_sprinting/) for more information about this.

## Next up
[Setting up a continuous integration (CI) pipeline](./16-github-workflows.md)
