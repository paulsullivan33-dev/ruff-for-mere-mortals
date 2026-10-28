# Your First Check

By the end of this chapter you have run
Ruff on a real file, seen it find real
mistakes, and seen the exit code that makes
it useful in scripts: 1 when it finds
problems, 0 when it does not.

The lab's practice file is `messy.py`, in
`ruff-lab/fixtures/`. It is a small config
loader and user finder, written for this
guide with mistakes planted in it: imports
nothing uses, a variable assigned and
forgotten, a name that was never defined,
a bare `except:`. Nothing in it is exotic —
these are the four most ordinary mistakes
in Python, which is the point.

Run Ruff on it:

```console
$ ruff check messy.py
```

Ruff answers with a list of diagnostics
(transcript `t01-first-check.txt`). Trimmed
to the first two, they look like this:

```text
I001 [*] Import block is un-sorted or un-formatted
 --> messy.py:1:1
  |
1 | / import os
2 | | import sys
3 | | from collections import OrderedDict
...
help: Organize imports

F401 [*] `os` imported but unused
 --> messy.py:1:8
  |
1 | import os
  |        ^^
...
help: Remove unused import: `os`
```

Eight problems in all: the unsorted import
block, three unused imports, two variables
assigned but never used, one undefined
name — `return results`, where the variable
is called `result` — and one bare `except`.
The full list, with every line and column,
is in the transcript.

Now the important part for everything that
follows: the exit code.

```console
$ ruff check messy.py
...
(exit code: 1)
$ ruff check clean.py
All checks passed!
(exit code: 0)
```

`clean.py` is the same config loader with
the mistakes removed. Ruff's contract is
simple and worth memorising:

- **0** — nothing to report.
- **1** — diagnostics were found (or, for
  the formatter, files would change).
- **2** — Ruff itself failed: a bad rule
  name, an unreadable configuration file.
  The lab produced this too, by asking for
  a rule family that does not exist.

That contract is what turns Ruff from an
opinion into a tool: a script, an editor, or
a CI pipeline can run it and branch on the
number. Chapter 9 builds on exactly this.

One more observation from the first run,
because it surprises people: all of this
happened with **no configuration at all**.
Ruff 0.17.3 switches on roughly 400 rules
by default — the lab counted them
(transcript `t10-default-rules.txt`) —
covering unused imports and names, unsorted
imports, outdated spellings like
`typing.List`, old-style `super()` calls,
files opened without a context manager, and
much more. The default set is deliberately
conservative about *style opinions*,
though: the famous line-length rule and the
`== None` comparison rule stay off until
you ask for them, as chapter 7 shows.
