# Exercise2
## Branching
Commands:
```
remote, fetch, branch, log
```

Check the remote repository address.
```bash
git remote -v
```

Fetch remote branches.   
The branches starting with `/origin` are remote, other branches are local.   
```bash
git fetch
git branch --all
```

Check the log of your current branch.   
Who made the last commit?   
```bash
git branch
git log
```

Checkout another branch (let's say the other branch is named `feature`).
```bash
git checkout -b feature
git branch
git log
```