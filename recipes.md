# Recipes

Short, complete jobs. Each assumes the
configuration of chapter 8 is in place
unless it says otherwise, and each ends
with the check that proves it worked.

## Adopt Ruff on an existing project

Run the defaults first and read the
statistics, not the findings:

```console
$ ruff check --statistics .
```

If the count is small, fix by hand or with
`--fix`. If it is enormous, write the codes
down as the project's starting `select`,
run `ruff check --add-noqa .` to pardon the
existing backlog in place, and check the
result in. From that commit on, the project
is clean *as far as the pardon list says*,
new findings fail the build, and the
`noqa` comments get paid down file by file.
Finish with `ruff check .` exiting 0.

## Format a project without a flag day

Formatting an entire codebase at once
creates one giant, unreviewable commit.
Do it as its own commit anyway — but a
*labelled* one: run `ruff format .`, commit
with a message that says only formatting
changed, and add the commit's hash to a
`.git-blame-ignore-revs` file so blame
history steps over it. Reviewers check the
one commit by re-running the formatter and
seeing no further changes; after that,
`ruff format --check .` in CI keeps the
peace permanently.

## Find the mistakes, skip the opinions

A project that wants Ruff as a bug-finder
only can pin the mistake families and leave
style to taste:

```toml
[tool.ruff.lint]
select = ["F", "E9", "B"]
```

`F` catches undefined and unused names,
`E9` the pycodestyle errors that indicate
real breakage, `B` the bugbear patterns.
Verify by planting an undefined name in a
scratch file and watching it fail while a
style peccadillo passes.

## Excuse a generated file properly

Code a generator writes should not be
hand-edited to please a linter, and its
findings are noise. Fence it:

```toml
[tool.ruff]
exclude = ["src/generated"]
```

Not `noqa` (hundreds of pardons in a file
nobody may touch) and not per-file ignores
rule by rule. Afterwards, `ruff check .`
should not mention the folder at all.

## Check only what changed

In a large repository, the pre-commit
question is usually about *these* files,
not the whole tree. Ruff accepts file
lists, so:

```console
$ git diff --name-only --cached | grep '\.py$' | xargs ruff check
$ git diff --name-only --cached | grep '\.py$' | xargs ruff format --check
```

Exit 0 means the change you are about to
commit is clean, whatever the rest of the
tree's history holds.

## Ask what a rule would do here

Before enabling an unfamiliar family on a
real project, audition it:

```console
$ ruff check --select UP --statistics .
```

The statistics say how many findings the
family brings and of what kind; `ruff rule
UP006` (or any code from the list) explains
the pattern. Enable families whose audition
you have read, in the configuration, one at
a time — the project's history then shows
which choice brought which findings.
