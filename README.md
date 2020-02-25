# git-overview

Prezi link:
https://prezi.com/view/GRX22I4Rh8Fe9smLUxdN/

Overview of the git workflow, meant as a beginner level training course.   
This page contains working examples of git commands.  

You can use the following visualization tool:
https://git-school.github.io/visualizing-git/#free-remote


## Content

* What is git?
* tl;dr workflow
* Git workflow (https://rogerdudler.github.io/git-guide/)
  * git clone
  * git pull
  * git add
  * git commit
  * git push
---
Advanced

* HEAD
* index
* working tree


## What is git?
According to their own documentation:
> Git is a fast, scalable, distributed revision control system with an unusually rich command set that provides both high-level operations and full access to internals.  

It is a Version Control System (VCS), used by the major Software-hosting plaftorms like GitHub, GitLab and BitBucket.   

Powerful features:

* Strong support for non-linear development   
Git has strong support for `branching` and `mergine`, which means several parties can work on the same codebase, on different `branches`. Git provides a set of tools to gracefully `merge` the changes from different teams into a single revision.   
* Distributed development   
Git creates a local copy of the whole project. All changes are done locally. When we are happy with our local repository, we can `push` our changes to the `remote` server. Git is both: a client and a server.   
* Cryptographic authentication of history
Git was doing blockchains before it was cool. Each version ID (called `commit`) depends on the whole history of the project up to that point. Commits are stored in a structure similar to a `Merkle tree` (the data structure powering cryptocurrency blockchains). It is impossible to change git history without being noticed.   


## Git workflow

### tl;dr
The too long, didn't read version of this document would be the following basic git commands used 80% of the time:

Starting from scratch, we will pull a project, make a change and push that change back to the remote server.   
```bash
# Get the project.
git clone https://github.com/voje/git-overview.git
cd git-overview

# You don't want to write to the master branch, 
# create a new branch instead.
git checkout -b new_feature_branch

# Create a new file (or change an existing one).
echo "Some new feature" > new_feature.txt

# Add the change to the working tree.
git add new_feature.txt

# Commit the change.
git commit -m "Adds new feature."

# Check the working tree.
git status

# When happy, push to remote.
git push origin new_feature_branch
```
That's it.   


### git clone
Go to GitHub or GitLab, find a project you like and find the `Clone or download` button.   
You will get the URL to the project, looking something like:
`https://github.com/voje/git-overview.git`.   
Make sure to use the `https://` url, not the `git@` one.   

```bash
git clone https://github.com/voje/git-overview.git
```
A folder is created with the same name as the project (in this case: `git-overview`).   
This is the local git repository (an exact clone of the remote project).   
Cd into the directory.   
```bash
cd git-overview
```
We are inside the project now.   
This is the root of the project.   
We can find a `.git` folder, containing all the project metadata.   
It is recommended not to change this folder - you should interact with the project using the `$ git` command.   

For a quick overview, you can try `$ git status` to see what's new and `$ git log` to see the commit history. More on those commands in the following chapters.   


### git checkout -b new_branch
After cloning a git project, we are on the `master` branch.   
You can check this with `$git branch --all`.   
You will see your local branches (only `master` right now) and all the remote branches -- the branches on the remote server.   

It's bad practise to modify master since this is the production branch and we can break a lot of things that way.   

When editing the project, create another branch with a meaningful name:
Let's say we want to edit the `README.md` file.   
```bash
# create a new local branch
git branch editing_readme

# go to that branch
git checkout editing_readme
```
Last step, check that you are on the correct branch:
```bash
git branch --all
```


### git status
> git-status - Show the working tree status

Git status shows the state of git index -- index vs working tree???


### git add
> git-add - Add file contents to the index

Git tracks all the changes to the current branch.   
Let's add a file:   
```bash
echo "Hello, Git!" > new_file.txt
```
Also let's modify an existing file:
```bash
echo "New line." >> README.md
```
We can check the current status of our project with `$ git status`.   
Now add the the changes to the index(TODO):
```bash
git add new_file.txt
git add README.md
```
Checking `$ git status`, we see that we've added all our changes.   


### git diff
Git diff is a powerful tool to compare different versions of files in our project.   
We can check how our current branch differs from the original (`master`) branch.   
```bash
git diff master
```
Or in case we are only interested in one specific file, use the `--` syntax:
```bash
git diff master -- README.md
```

### git commit
TODO

### git push


---

### HEAD
Commit at the tip of the current branch.   

### Index == Staging Area
Intermediate state between our filesystem and our working tree.   
Index tracks three types of files:

* tracked, modified (staged) - files to-be-committed
* tracked, modified (unstaged)
* untracked

### Working Tree
The file and directory representation of the project you are currently working on.   
`git add` stages changes in the working tree to the `index`.   




## Sources

* https://blog.osteele.com/2008/05/my-git-workflow/ -- awesome workflow example, oldschool guy, uses index as intermediate staging area (instead of rebasing)
* https://git-school.github.io/visualizing-git/#free-remote