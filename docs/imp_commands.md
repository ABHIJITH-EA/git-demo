# **Importand commands**


>`git branch -vv`
- To see what tracking branches you have set up

> `git pull`
- which is essentially a git fetch immediately followed by a git merge in most cases. If you have a tracking branch set up *`git pull`* will look up what server and branch your current branch is tracking, fetch from that server and then try to merge in that remote branch.

> `git push <remote> --delete <branch>`
- Delete remote branch