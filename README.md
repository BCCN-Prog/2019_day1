# Syllabus
- Day 1
    - Summary of git internals
    - Standard git workflow
    - Forking and cloning repos
    - Branching and adding upstream repos
    - Making pull-requests
    - Reviewing and merging a pull-request

- Day 2
    - Benefits of prototyping
    - Project management and Agile
    - Basics of good testing
    - The structure of tests (Given, When, Then)
    - Essentials of PyTest
    - Continuous Integration with Travis CI

- Day 3 & 4
    - Contributing to Numpy

- Day 5
    - Planning and preparation for the semester project
    - Requested tutorials

# git

## Warm-Up
- how to start a repo from scratch? 
    - `git init` local method
    - on GitHub `git clone` and either `git push --force` or `git pull` methods
- how to revert mistakes?
    - `git revert` vs. …
    - `git reset` vs. …
    - `git reset --hard`
- how to go to a specific point in history?
    - `git checkout SHA` ⟶ `DETACHED HEAD` problem
    - interaction with branches
- `git gui`: building commits along the way interactively (for the *mess around* type of workflows)

## The Open Source model
- remotes: `pull`, `push`, `fetch`, `merge`
- GitHub: forks, branches and PRs
- strategies for keeping your fork up-to-date: `rebase` or `merge`
- a more thorough and deailed explanation can be found on the [Numpy Contributor's Guide](https://docs.scipy.org/doc/numpy/dev/gitwash/index.html). This guide can be adapted to your own needs, see [gitwash](https://github.com/matthew-brett/gitwash).
