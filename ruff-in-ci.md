# Ruff in CI

By the end of this chapter Ruff's results
come out in shapes other tools can read —
pipeline annotations and JSON — and you
know which of its integrations the lab ran
and which it only read about.

Chapters 3 and 6 established the contract:
exit 0 for clean, 1 for findings, 2 for
"Ruff itself failed". A continuous
integration pipeline needs nothing more to
be useful:

```console
$ ruff check .
$ ruff format --check .
```

Two lines in a build script, and no pull
request merges with an unused import or an
unformatted file again. Everything else in
this chapter is about making the *output*
kinder to the humans reading the pipeline
log.

## Annotations a pipeline understands

GitHub Actions (and compatible systems)
turn specially formatted lines into
annotations pinned to the exact line of the
pull request. Ruff speaks that format
natively:

```console
$ ruff check --output-format github messy.py
::error title=ruff (F401),file=messy.py,line=1,col=8,endLine=1,endColumn=10::messy.py:1:8: F401 `os` imported but unused%0A  help: Remove unused import: `os`
...
(exit code: 1)
```

The lab's transcript `t08-ci.txt` has all
eight. The contributor never opens the
build log; the finding appears in the
review, on the line, with the fix
suggestion attached. The exit code is
unchanged — the format is for readers, the
number is for the pipeline.

## JSON for everything else

For dashboards, editor integrations, or
your own scripts, `--output-format json`
emits the diagnostics as structured data:
each finding an object with its code,
message, file, start and end location, and
— where one exists — the fix itself,
including the exact edits and whether Ruff
classifies them as safe. The lab captured
the shape in the same transcript. If you
are building tooling on top of Ruff, build
it on this; screenscraping the human
output is building on sand.

Two smaller switches complete the kit:
`--output-format concise` gives the
one-line-per-finding form
(`messy.py:1:8: F401 ...`) that suits
terminals and logs, and `--exit-zero`
reports everything but still exits 0 — for
a first adoption week, when you want the
findings visible in the log and the build
green while the team works the list down.

## The integrations the lab did not run

Honesty section, as promised in chapter 1:

- **Editor extensions.** Ruff ships an
  official extension for VS Code and
  supports other editors through its
  language server (`ruff server`), showing
  diagnostics as you type and offering
  fixes in place. Described here from the
  documentation; a terminal-driven lab has
  no editor to demonstrate.
- **Pre-commit.** The pre-commit framework
  can run Ruff on every commit, using the
  project's official hook definitions.
  Same engine, same configuration; the lab
  drove Ruff directly.
- **The official GitHub Action and Docker
  images** install and run the same binary
  in the pipeline. The lab verified the
  `--output-format github` output those
  integrations rely on, locally.
- **Notebooks.** Ruff checks and formats
  Jupyter notebooks directly, treating code
  cells as Python. Documented-only here;
  the lab's fixtures are plain files.
- **Watch mode** (`ruff check --watch`)
  re-checks on every save for terminal
  workflows. Interactive by nature, so
  described rather than transcribed.
