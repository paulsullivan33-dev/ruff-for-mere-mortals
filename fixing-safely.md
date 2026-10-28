# Fixing, Safely

By the end of this chapter Ruff has fixed
the lab's messy file twice — once with safe
fixes, once with unsafe ones — and you have
seen what each kind of fix can and cannot
do, and what no fix can do at all.

Work on a copy. The guide's rule from
chapter 1 applies with full force here:
only fix what you can restore. In the lab
that meant copying `messy.py` to
`fixed.py`; in your projects it should mean
version control.

## Look before you leap: `--fix --diff`

Before applying anything, preview it. The
`--diff` flag shows the edits `--fix`
*would* make, as a patch, and changes
nothing:

```console
$ ruff check --fix --diff fixed.py
--- fixed.py
+++ fixed.py
@@ -1,6 +1,3 @@
-import os
-import sys
-from collections import OrderedDict
 
 import json
 
Would fix 3 errors (2 additional fixes available with `--unsafe-fixes`).
```

Three edits, all of them removing an unused
import. Note what is *not* in the patch:
the unsorted-imports complaint (I001) is
also about that block, and removing the
three imports settles it as a side effect —
the one remaining import is trivially in
order. Ruff reports fixes as edits, and
one edit can close several diagnostics.

## Safe fixes

Apply them:

```console
$ ruff check --fix fixed.py
...
Found 7 errors (3 fixed, 4 remaining).
```

Four diagnostics remain: the two unused
variables (their fixes are unsafe), the
undefined name, and the bare `except`.
Ruff exits 1, correctly: `--fix` is not
`--make-it-pass`. It applies every safe
edit it has and reports the rest.

## Unsafe fixes

Now the explicit opt-in:

```console
$ ruff check --fix --unsafe-fixes fixed.py
...
Found 5 errors (3 fixed, 2 remaining).
```

Ruff removed all three assignments to
variables nothing used — including
`result = None`, the initialisation at the
top of `find_user`. Look at what that did
to the function (transcript
`t03-fixing.txt` keeps the whole file):
the loop that used to store the matching
user now does `pass`, and the function
still ends with `return results` — a name
that does not exist. The code was already
wrong; the unsafe fix made it wrong
*differently*, silently. That is the whole
lesson of unsafe fixes in one example:
they are text edits that usually express
the right intention, and the gap between
"usually" and "always" is your review.
Ruff marks them unsafe, keeps them behind
a flag with a scary name, and prints a
note on every one. Believe the note.

## What no fix can do

Two diagnostics survived everything:

- **F821, undefined name.** Ruff knows
  `results` is wrong. It cannot know you
  meant `result`. Any tool that guessed
  would sometimes guess wrong, so Ruff
  refuses, and the fix is a human typing
  one letter.
- **E722, bare `except`.** Catching
  *something specific* is a design
  decision. Ruff flags the pattern and
  leaves the decision to you.

A checker that fixes everything would be
lying about one of these. The honest end
state of the lab's file is two real
decisions left for a person — and a file
that is otherwise clean, reached in two
commands. After any fixing session, run
your tests if you have them; Ruff checked
the text, and only running the code checks
the behaviour.
