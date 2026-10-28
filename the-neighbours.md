# The Neighbours

Ruff did not invent most of its rules. It
reimplemented the rule sets of a generation
of Python tools in one fast program, which
raises a fair question: what are those
tools, and does anything still belong to
them? Short characterisations, not
benchmarks.

**Pyflakes and Flake8.** Pyflakes is the
original "mistakes, not style" checker, and
its codes are Ruff's `F` family, unchanged.
Flake8 wrapped Pyflakes and pycodestyle in
a plugin system and ran Python's linting
for a decade. Ruff covers nearly all of
both, plus many of the popular plugins —
which is why so many rule codes will look
familiar if you have linted before.

**pycodestyle and Black.** pycodestyle
checks PEP 8 layout (Ruff's `E` and `W`);
Black made formatting a solved argument by
refusing options (Ruff's formatter is its
close descendant, and migration between
them is meant to be boring). If a project
already formats with Black, Ruff's
formatter will mostly agree with it —
chapter 12 is honest about the corners
where they differ.

**isort.** A whole tool for sorting import
blocks, now Ruff's `I` family. If your only
linting need was import order, it is inside
Ruff already.

**Pylint.** The deep analyser: it follows
code further than the others, and some of
its checks (the `PL` family) are in Ruff —
but not all. Pylint still earns its keep on
projects that want its most thorough
analysis and can tolerate its slower,
opinionated runs. Running both is a
legitimate choice, not a contradiction.

**pyupgrade, flake8-bugbear,
flake8-simplify, and friends.** Each began
as one good idea — modernise old spellings,
catch bug-shaped patterns, simplify
convoluted code. Inside Ruff they are the
`UP`, `B` and `SIM` families, and the
long tail of prefixes in chapter 7's
counting exercise is mostly this: a decade
of good ideas, unified.

**mypy and pyright.** Not neighbours but
the next street over: *type checkers*. They
follow the type annotations in your code
and catch a class of error — passing a
string where a number belongs — that Ruff
deliberately does not attempt. Ruff plus a
type checker is the complete static
picture; neither replaces the other.
Chapter 12 returns to this.

**ShellCheck** deserves a mention for
readers of this series: it does for shell
scripts exactly what Ruff does for Python —
reads without running, names the pattern,
suggests the fix. If Ruff feels familiar,
that is why.
