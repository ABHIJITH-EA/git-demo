# **Importand commands**


>`git branch -vv`
- To see what tracking branches you have set up

> `git pull`
- which is essentially a git fetch immediately followed by a git merge in most cases. If you have a tracking branch set up *`git pull`* will look up what server and branch your current branch is tracking, fetch from that server and then try to merge in that remote branch.

> `git push <remote> --delete <branch>`
- Delete remote branch

> `git switch -c <branch-name> -t <remote>/<branch>`
- This will setup branch wich will start tracking the remote branch.

> `git branch -a`
- List all the branch's including remote and local.

> `git add --patch`
- To partially stage files
