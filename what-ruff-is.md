# What Ruff Is

By the end of this chapter you can say what
Ruff checks, what it formats, and the one
habit that makes its automatic fixes safe
to use.

**Ruff** is a tool for Python code. It does
two jobs that used to belong to a drawer
full of separate tools:

- It is a **linter**: it reads your code
  without running it and reports problems —
  imports you never use, names that do not
  exist, comparisons written the risky way,
  and a few hundred other patterns, most of
  them copied from older tools so their rule
  codes still match.
- It is a **formatter**: it rewrites your
  code into one consistent layout — spacing,
  line breaks, quote style — so that style
  stops being something people argue about.

Both jobs live in a single program, written
in the Rust programming language by the
Astral company, and released as free and
open-source software. The single program
matters more than it sounds: one install,
one configuration file, one set of rule
codes, and a run that finishes before your
hand leaves the keyboard. Chapter 3 shows
Ruff checking the Python standard library
on a small machine in under four seconds;
speed is not a footnote here, it is the
reason the tool gets run at all.

## The mental model

Ruff never runs your code. It reads it the
way a careful proofreader reads an essay:
looking at the text, not the results. That
one fact explains both its strengths and
its limits. It can prove that `results` is
not defined anywhere in a file, because
that is a fact about the text. It cannot
prove your program prints the right answer,
because that is a fact about running it.
Chapter 12 returns to this line; keep it in
mind from the start and Ruff will never
surprise you.

Every complaint Ruff makes is called a
**diagnostic**. A diagnostic names a
**rule** — a single pattern Ruff knows how
to spot — with a short code like `F401`.
Chapter 4 takes one apart. Rules are
grouped into families by where they came
from: `F` is Pyflakes, `E` is pycodestyle,
`I` is import sorting, and so on. You
choose which families are on, in a
configuration file or on the command line,
and chapter 7 shows how.

Some diagnostics carry a **fix**: an edit
Ruff is willing to make for you. Fixes come
in two kinds, and the difference matters.
A **safe fix** cannot change what your
program does — removing an import nothing
uses, for example. An **unsafe fix** might
change behaviour, so Ruff never applies
those unless you explicitly ask. Chapter 5
works through both kinds on a real file.

## The rule of this guide

Ruff edits code. That is its gift and its
danger, so this guide has one rule, stated
here and in chapter 5 where it bites:

**Only let Ruff fix what you can restore,
and read every diff it makes.**

In practice that means: run it on code that
lives in version control, so every edit is
one command away from being undone; look at
what changed before you keep it; and do not
point `--fix` or the formatter at someone
else's project uninvited. Reformatting a
shared codebase is a social act, not a
cleanup — it buries other people's work
under thousands of cosmetic changes. On
your own code, with a way back, Ruff is one
of the safest power tools in the Python
world.

## What the lab ran

The lab behind this guide ran the real
thing: Ruff 0.17.3, the official release
binary, against small fixture files written
for the purpose — a config loader with
planted mistakes, an unformatted greeting
program, an unsorted import block — and,
for scale, against the entire Python 3.12
standard library installed on the machine.
Every transcript quoted in the chapters is
kept in `ruff-lab/transcripts/`, and the
fixtures are in `ruff-lab/fixtures/`.
`criteria.md` lists what was run and what
is only documented.
