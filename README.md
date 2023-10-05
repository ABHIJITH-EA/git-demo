# *Git branching*
- Once the commit object is created, Git inserts it into the Git repository's object database, and it becomes a permanent part of your project's history.
- when you run `git commit`, Git checksums each subdirectory and stores them as a tree object in the Git repository.Git then creates a commit object that has the metadata and a pointer to the root project tree(snapshot of the content you staged.) so it can re-create that snapshot when needed.

![A commit and its tree](./resources/commit-and-tree.png)
