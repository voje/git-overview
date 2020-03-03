# Exercise3
## Merging
Commands:
```
diff, merge
```

You should have two branches in your local repository: `master` and let's say `feature`.   
```
git branch
```

Check the difference between `master` and `feature`.   
```bash
git diff master feature
```

We can also check specific files:
```bash
git diff master feature -- README.md
```

Merge the changes in `feature` into `master`.   
```bash
git checkout master
git merge feature
```

Resolve conflicts
```bash
git status
# Edit the files
git add . README.md
git status
git commit -m "Merged feature branch."
```

Push the changes to origin/master.
```bash
git push origin master
```