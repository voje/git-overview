# Exercise1
## Basic workflow
Commands:
```
clone, add, status, commit, push
```

Using the above commands, clone a git project and write a new fild:
```bash
git clone <project>
echo "Hello Git!" > hello.txt
```

Add the newly created file to the index.  
```bash
git status
git add hello.txt
git status
```

Commit the changes.
```bash
git commit -m "Adding hello.txt"
git status
```

Push the changes to remote master branch.
```bash
git push origin master
```
