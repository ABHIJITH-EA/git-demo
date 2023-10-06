# **Git branching**
- Once the commit object is created, Git inserts it into the Git repository's object database, and it becomes a permanent part of your project's history.
- when you run `git commit`, Git checksums each subdirectory and stores them as a tree object in the Git repository.Git then creates a commit object that has the metadata and a pointer to the root project tree(snapshot of the content you staged.) so it can re-create that snapshot when needed.

![A commit and its tree](./resources/commit-and-tree.png)

- If you make some changes and commit again, the next commit stores a pointer to the commit that came immediately before it.

![Commits and their parents](./resources/commits-and-parents.png)

## How to set up remote tracking branch

We can create a local branch and set up the branch to track a remote branch.
.
`git checkout -b local-dev --track origin/dev`

OR

`git switch -c local-dev -t origin/dev`

Now we can easily easily fetch the remote work by,

`git fetch`

`git pull`

### [Git branching model](./docs/branching_models.md)
