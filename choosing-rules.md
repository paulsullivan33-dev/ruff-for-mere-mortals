# Choosing Rules

By the end of this chapter you can turn
rule families on and off for a single run,
survey everything Ruff knows how to check,
and silence one diagnostic in one place
without silencing it everywhere.

Chapter 3 noted the surprise: Ruff 0.17.3
enables roughly 400 rules with no
configuration at all. The lab counted them
by family (transcript
`t10-default-rules.txt`). The biggest
groups are the ones descended from older
tools:

| Prefix | Origin | What it watches for |
|--------|--------|--------------------|
| `F` | Pyflakes | Undefined names, unused imports and variables — mistakes, not style |
| `E`, `W` | pycodestyle | Layout and spelling of the code itself |
| `I` | isort | Import blocks sorted and grouped |
| `UP` | pyupgrade | Outdated spellings that newer Python writes better |
| `B` | flake8-bugbear | Patterns that are legal but probably bugs |
| `SIM` | flake8-simplify | Code that says in five lines what one would say |
| `PL` | Pylint | A large family: errors (`PLE`), warnings (`PLW`), refactors (`PLR`), conventions (`PLC`) |
| `RUF` | Ruff itself | Rules with no ancestor in another tool |

Dozens more families exist beyond the
defaults. `--select ALL` turns on
everything Ruff knows, and on the lab's
small file it is an education:

```console
$ ruff check --select ALL --statistics messy.py
...
Found 26 errors.
```

Twenty-six findings on a file the defaults
called eight — the extra eighteen are
mostly *opinions*: missing docstrings,
style preferences, stricter patterns. ALL
is a survey instrument, not a setting.
Nobody sane ships with all of it on; many
good projects start from the defaults and
add families deliberately.

## Selecting and ignoring for one run

`--select` chooses rules for a single run.
It takes codes or whole prefixes:

```console
$ ruff check --select I unsorted.py
I001 [*] Import block is un-sorted or un-formatted
...
Found 1 error.
```

Only the import rule ran, so only its
complaint appeared — the unused imports in
the same file were not Ruff's business for
that run. `--ignore` subtracts instead:

```console
$ ruff check --ignore F401 messy.py
...
Found 5 errors.
```

The three unused-import findings vanished;
the other five stayed. When both flags
appear, ignore wins for the rules it names.

Families you will most likely reach for
first, because the defaults leave them off:

- **`E501`** — line too long. The default
  limit is 88 characters:

  ```console
  $ ruff check --select E501 long_lines.py
  E501 Line too long (144 > 88)
  ```

- **`E711` / `E712`** — comparisons to
  `None` and `True` written with `==`, a
  genuine bug habitat, since `==` can be
  redefined by the objects compared while
  `is` cannot. Their fixes are classified
  unsafe for exactly that reason.
- **`E731`** — a lambda assigned to a name,
  where a `def` is clearer.

## Silencing one line: `noqa`

Sometimes one diagnostic, in one place, is
wrong on purpose — a deliberate pattern, a
name imported for its side effects. The
surgical tool is a comment:

```python
import os  # noqa: F401
```

The lab added exactly that to `messy.py`,
and the count dropped from eight findings
to seven (transcript `t06-noqa.txt`): that
one F401, on that one line, is forgiven;
every other rule still applies there, and
F401 still applies everywhere else. A bare
`# noqa` with no code silences everything
on the line — use it rarely, because it
also silences the finding you did not know
was coming.

Ruff can write these comments for you:

```console
$ ruff check --add-noqa messy.py
```

On the lab's file it annotated every
offending line with the codes found there,
and a fresh check passed — eight findings,
eight little pardons. Treat `--add-noqa`
as a way to adopt Ruff on an existing
codebase without fixing everything first,
not as a way to make findings disappear:
every comment it writes is a debt with a
rule code on it, and chapter 10's recipes
return to paying those down.
