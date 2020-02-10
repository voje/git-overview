# git-overview
Overview of the git workflow, meant as a beginner level training course.   
This page will contain working examples of git commands.  
For more details, see the `in-depth` link for a specific chapter.   
I will be visualizing all of the commands using [this project](https://git-school.github.io/visualizing-git/).   

## Contents

* What is git?
* tl;dr workflow
* Basic workflow (https://rogerdudler.github.io/git-guide/)
  * git clone
  * git pull
  * git add
  * git commit
  * git push
* Advanced workflow


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


## Basic workflow

### tl;dr
The too long, didn't read version of this document would be the following basic git commands used 80% of the time:

Starting from scratch, we will pull a project, make a change and push that change back to the remote server.   
```bash
# Get the project.
git clone https://github.com/voje/git-overview.git
cd git-overview

# Create a new file (or change an existing one).
echo "Some new feature" > new_feature.txt

# Add the change to the working tree.
git add new_feature.txt

# Commit the change.
git commit -m "Adding new feature."

# Check the working tree.
git status

# When happy, push to remote.
git push origin master
```
That's it.   


### git clone



### git add
### git commit
### git push