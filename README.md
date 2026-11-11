<div align="center">

# Learn Git with AI

**Build confidence with Git commands, one small step at a time.**

Learn what each command does, try it in a repository, and use AI to explain the result.

</div>

---

## Start with the essentials

Git helps you track changes to files and revisit earlier versions of your work. These commands are a useful starting point:

| Command | What it does |
| --- | --- |
| `git init` | Starts a Git repository in the current directory. |
| `git status` | Shows changed files and the current branch. |
| `git add <file>` | Stages a file's current changes for a commit. |
| `git commit -m "message"` | Records staged changes with a message. |
| `git log --oneline` | Shows a compact history of commits. |

## Save a snapshot

A typical edit-and-commit cycle looks like this:

```bash
git status
git add README.md
git commit -m "Update README"
git log --oneline
```

Run `git status` again after each step to see how the repository changes. A commit records what is staged, so review the staged changes before committing.

## Explore safely

Branches let you work on a change separately from the current branch:

```bash
git switch -c my-change
# make and stage your changes
git commit -m "Describe my change"
git switch main
```

To bring a completed branch into `main`, switch to `main` and merge it:

```bash
git merge my-change
```

## Learn with AI

Ask AI to explain a command before running it, or to help interpret output afterward. For example:

> Explain what `git add` stages, and how it differs from `git commit`.

> Here is the output of `git status`. What changed, and what are my safe next steps?

> Walk me through creating a branch and merging it, explaining each command as we go.

Use a disposable practice repository when experimenting with commands that change history or remove files. Read suggested commands before running them, especially if they use options you do not recognize.

## Keep practicing

Try a small change, inspect it with `git status`, stage only the file you intended, then create a commit. Repeat the same workflow on a branch and compare the results with `git log`.
