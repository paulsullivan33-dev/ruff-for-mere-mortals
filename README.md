# Ruff for Mere Mortals

Python code collects small mistakes the way
a workbench collects offcuts: an import left
behind after the code that used it was
deleted, a variable assigned and never
read, a name spelled almost like the right
one. None of them stop the program from
starting. All of them make it harder to
read, and one of them — the misspelled name
— is a crash waiting for the right input.
**Ruff** is the tool that sweeps the bench.
It reads your code without running it,
reports the mistakes and the questionable
patterns, fixes the ones that can be fixed
mechanically, and formats everything into
one consistent layout — fast enough that
"fast" stops sounding like marketing: this
guide's lab checked the entire Python
standard library, thousands of files, in
under four seconds.

This guide explains how Ruff thinks, how to
read the diagnostics it produces down to
the last marker, how its safe fixes differ
from its unsafe ones (with a worked example
of an unsafe fix changing a function's
shape), how the formatter and the linter
divide the work, how to choose rules and
write the choice into a configuration file,
and how to wire the results into a pipeline
so the findings arrive as annotations on
the exact line that caused them. The limits
are stated plainly, including the central
one: Ruff reads text, and only running the
code proves behaviour.

One rule governs everything here, and
chapter 1 states it before any procedure
depends on it: **only let Ruff fix what you
can restore, and read every diff.** Run it
on code that lives in version control. Look
at what changed. And do not point its
formatter, uninvited, at somebody else's
project — a surprise reformat of a shared
codebase is a social act, not a cleanup.

The lab behind this guide ran the real
thing: **Ruff 0.17.3**, the official release
binary, against fixture files written for
the purpose. It checked a config loader
with planted mistakes and got eight real
diagnostics; previewed, applied, and then
extended the fixes until only the two
human decisions remained; formatted a
badly-laid-out program and watched the
check pass afterwards; silenced findings
with `noqa` comments and let Ruff write
those comments itself; configured two
small projects two different ways and
watched the same files produce different
findings; produced the pipeline annotation
format and the JSON output; and, for scale,
counted the findings in the machine's own
Python 3.12 standard library. It also
counted the rules Ruff enables with no
configuration at all — about 400, many
more than the small historical set the lab
expected — and chapter 7 is written from
that evidence rather than from the older
documentation's smaller claim.

What the lab could not do, it did not fake.
It worked in a text-only sandbox, so the
editor extensions and the language server
are described from the documentation, as
are the install routes it did not take
(pip, Homebrew, and friends), the
pre-commit hooks, notebook support, and
watch mode. `criteria.md` keeps the full
ledger of what was run and what was only
read.

## What this guide covers

- [**What Ruff is**](what-ruff-is.md) —
  the mental model: a linter and a
  formatter in one fast program, what it
  means that it reads without running, and
  the rule about fixing only what you can
  restore
- [**Installing Ruff**](installing-ruff.md) —
  the official release binary, the checksum,
  and the other doors into the same command
- [**Your first check**](your-first-check.md) —
  a file with planted mistakes, eight
  diagnostics, and the exit-code contract
  everything else builds on
- [**Reading diagnostics**](reading-diagnostics.md) —
  the anatomy of a finding, counting with
  `--statistics`, and asking Ruff about any
  rule with `ruff rule`
- [**Fixing, safely**](fixing-safely.md) —
  previewing with `--diff`, safe fixes,
  unsafe fixes and what they did to the
  lab's function, and the two problems no
  fix can solve
- [**The formatter**](the-formatter.md) —
  check mode, the reformat itself, why
  formatting is idempotent, and where it
  stops
- [**Choosing rules**](choosing-rules.md) —
  the rule families and where they came
  from, selecting and ignoring for one run,
  the ALL survey, and the `noqa` scalpel
- [**Configuration**](configuration.md) —
  choices written in `pyproject.toml` or
  `ruff.toml`, line length, per-file
  ignores, and the settings met early
- [**Ruff in CI**](ruff-in-ci.md) —
  exit codes in a pipeline, GitHub
  annotations, JSON output, and an honest
  list of the integrations the lab did not
  run
- [**Recipes**](recipes.md) — adopting
  Ruff on an existing project, formatting
  without a flag day, mistakes-only mode,
  excusing generated code, checking only
  what changed
- [**The neighbours**](the-neighbours.md) —
  Flake8, Black, isort, Pylint, the plugin
  family, and the type checkers: what each
  still owns
- [**Limits**](limits.md) — no execution,
  no types, fixes as text edits, formatter
  versus Black in the corners, and defaults
  that move
- [**Troubleshooting**](troubleshooting.md) —
  mystery findings, a fix that broke
  something, exit code 2, and the run that
  felt too fast to be real
- [**Glossary**](glossary.md) — the terms,
  collected in one place

## What it doesn't cover

Making a program correct — Ruff raises the
floor, and chapter 12 explains why "all
checks passed" is not a proof. Type
checking, which belongs to mypy and pyright
and is pointed to, not taught. Rewriting
code by hand to satisfy the strictest
possible rule set: this guide teaches
choosing a sane set and living with it, not
turning every dial to maximum. And running
Ruff as an organisation-wide gate — policy,
waivers, central configuration for many
teams — is beyond its scope; it stays with
one person, their projects, and their
pipeline.

## How to use this guide

Read chapter 1 for the model and the rule,
and run chapter 3 in the same sitting as
the install: the first check makes
everything after it concrete. Chapter 5 is
the one to read slowly — the difference
between safe and unsafe fixes is the
difference between a tool and a hazard, and
the lab's example shows rather than tells.
Do chapter 6's formatter work on a copy of
something real, and let chapter 8's
configuration be the moment your own
project's choices get written down.
Chapter 9 repays its small effort the first
time a finding lands on the exact line of
a pull request. The lab's transcripts live
in `ruff-lab/transcripts/`; its fixtures
are `ruff-lab/fixtures/` and its two
configuration projects are
`ruff-lab/projects/`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Python for Mere Mortals](https://paulsullivan33-dev.github.io/python-for-mere-mortals/)
- [ShellCheck for Mere Mortals](https://paulsullivan33-dev.github.io/shellcheck-for-mere-mortals/)
- [Git for Mere Mortals](https://paulsullivan33-dev.github.io/git-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/ruff-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/ruff-for-mere-mortals/blob/main/LICENSE-CODE).
