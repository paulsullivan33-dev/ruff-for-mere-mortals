# Reading Diagnostics

By the end of this chapter you can take any
Ruff diagnostic apart into its five pieces
and find the full documentation for any
rule in one command.

Here is one diagnostic, complete:

```text
F401 [*] `os` imported but unused
 --> messy.py:1:8
  |
1 | import os
  |        ^^
2 | import sys
3 | from collections import OrderedDict
  |
help: Remove unused import: `os`
```

Read it left to right:

1. **The rule code** — `F401`. The letter
   is the family (here `F`, Pyflakes); the
   number is the individual rule. The code
   is stable: it means the same thing in
   every Ruff version, in documentation,
   and in configuration files.
2. **The `[*]` marker** — a fix exists.
   No marker means Ruff can point at the
   problem but will not offer to edit it.
3. **The message** — one sentence saying
   what was found, naming the exact thing
   (`os`, in backticks).
4. **The location** — file, line, column,
   then the source itself with the offending
   span underlined. You rarely need to open
   the file to understand the complaint.
5. **The help line** — what the fix would
   do, when a fix exists.

Some diagnostics add a **note**. The F841
diagnostics in `messy.py` (a variable
assigned but never used) carry one:

```text
note: This is an unsafe fix and may change runtime behavior
```

That note is the boundary from chapter 1,
drawn on the specific case: Ruff will
remove the assignment if told to, but
deleting code is a decision, not a tidy-up.
Chapter 5 shows what happens when you say
yes anyway.

## Counting instead of reading

On a big codebase nobody reads diagnostics
one by one first. `--statistics` collapses
a run into counts per rule:

```console
$ ruff check --statistics messy.py
3	F401	[*] unused-import
2	F841	[ ] unused-variable
1	E722	[ ] bare-except
1	F821	[ ] undefined-name
1	I001	[*] unsorted-imports
Found 8 errors.
```

The `[*]` column still marks which rules
have fixes. Statistics is the right first
move on any new project: it tells you
whether you are looking at eight problems
or eight thousand, and of what kind, before
you read a single one. For scale, the lab
ran the same command over the entire
Python 3.12 standard library installed on
the machine: 5,585 findings, in 3.8 seconds
(transcript `t09-stdlib-scale.txt`).

## Asking Ruff about a rule

Every rule has a page of documentation,
and Ruff carries it inside the binary:

```console
$ ruff rule F401
```

The lab's transcript `t02-statistics-and-rule.txt`
keeps the full answer. Its shape is the
same for every rule: what it checks, why it
is considered bad, an example of the
offending pattern, what to write instead,
and how safe the fix is. Two habits are
worth forming:

- When a diagnostic surprises you, read its
  rule page before arguing with it. Half of
  all "false positives" are a rule meaning
  something more precise than its one-line
  message — F401's page, for instance,
  explains exactly how to mark an import as
  an intentional re-export.
- When a diagnostic is right but unwanted —
  a generated file, a deliberate pattern —
  the answer is configuration, not
  annoyance. Chapters 7 and 8 cover telling
  Ruff to stop asking.
