# Glossary

The terms, collected in one place.

**Diagnostic** — a single finding from
`ruff check`: a rule code, a message, a
location in the source, and sometimes a
fix. Diagnostics are what the exit code
counts.

**Rule** — one pattern Ruff knows how to
detect, named by a stable code (`F401`) and
a descriptive name (`unused-import`).
Every rule has documentation inside the
binary: `ruff rule F401`.

**Rule family** — a group of rules sharing
a code prefix and an origin: `F` from
Pyflakes, `UP` from pyupgrade, `PL` from
Pylint, `RUF` for Ruff's own.

**Linting** — reading code without running
it to report mistakes and questionable
patterns. Named after a tool from the
1970s that picked fluff off C programs.

**Formatter** — a tool that rewrites code
into one canonical layout. `ruff format`
is Ruff's; it follows the Black style
closely.

**Safe fix** — an automatic edit Ruff
classifies as unable to change what a
program does. Applied by `--fix`.

**Unsafe fix** — an automatic edit that
might change behaviour: powerful, labelled
on every diagnostic that offers one, and
applied only with `--fix --unsafe-fixes`.

**`noqa`** — a comment (`# noqa: F401`)
that excuses the named rule on that one
line. Short for "no quality assurance" —
a convention Ruff inherited from Flake8.

**Per-file ignores** — configuration that
excuses named rules for named files, for
exceptions bigger than a line and smaller
than a project.

**Exit code** — the number a command
leaves behind. Ruff's contract: 0 clean,
1 findings, 2 Ruff itself failed.

**CI** — continuous integration: the
pipeline that builds and checks code
automatically when it is pushed. Where
Ruff's exit codes earn their keep.

**Target version** — the oldest Python a
project must run on. Ruff infers it from
`requires-python` or takes it from
configuration, and refuses to suggest
spellings that Python cannot read.

**Preview rules** — rules and behaviours
Ruff is still stabilising, available with
`--preview`. Interesting, and deliberately
not part of the default promise.
