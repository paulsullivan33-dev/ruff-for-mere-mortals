# Configuration

By the end of this chapter your choices
live in a file next to the code, Ruff finds
them by itself, and one file in a project
can be excused from one rule without
excusing the rest.

Command-line flags are for experiments.
Real projects write their choices down, so
every run — yours, your editor's, the
pipeline's — uses the same ones. Ruff reads
configuration from two places:

- a `[tool.ruff]` section in the project's
  **`pyproject.toml`** — the standard file
  Python projects already keep their
  settings in, or
- a dedicated **`ruff.toml`** file.

Ruff discovers the file on its own: for
each file it checks, it looks in that
file's folder and upward through its
parents, and the nearest configuration
wins. (Where both files exist in the same
folder, the project's documentation gives
`ruff.toml` priority.) You never pass the
path in ordinary use; running `ruff check`
inside the project is enough.

## A first configuration

The lab built a small project in
`ruff-lab/projects/config-project/` with
this `pyproject.toml`:

```toml
[tool.ruff]
line-length = 72

[tool.ruff.lint]
select = ["E501", "F"]

[tool.ruff.lint.per-file-ignores]
"long_lines.py" = ["E501"]
```

Three decisions are recorded there:

- **Line length is 72**, not the built-in
  88 — one number, agreed once, applied to
  both the linter and the formatter.
- **The rule selection is explicit**:
  the `F` family plus `E501`. Writing a
  `select` replaces the default selection
  rather than adding to it — this project
  deliberately runs a small, strict set.
  (An `extend-select` option exists for
  adding families on top of the defaults
  instead.)
- **One file is excused from one rule.**
  `long_lines.py` holds a long string that
  cannot be broken, so E501 does not apply
  to it — and only to it.

The project has two files with long lines:
`tidy.py`, whose longest line runs 89
characters, and `long_lines.py`, at 144.
Running the check (transcript
`t07-configuration.txt`):

```console
$ ruff check .
E501 Line too long (89 > 72)
...
Found 1 error.
```

Exactly one finding: `tidy.py` broke the
project's 72-character rule, and
`long_lines.py` — the worse offender —
stayed silent because of its per-file
excuse. That is configuration working as
intended: the team's decisions, enforced
mechanically, with exceptions written down
where anyone can see them.

## The dedicated file

The second lab project keeps the same kind
of choices in a `ruff.toml`:

```toml
line-length = 100

[lint]
select = ["F401"]
```

Same content, shallower nesting — without
the `[tool.ruff]` wrapper, because the file
belongs to Ruff alone. Checking the project
reported exactly the three unused imports
and nothing else: the selection did what it
said. Choose whichever file your project
already prefers; the settings are the same
either way.

## Settings worth knowing

Beyond `line-length` and the rule
selection, the settings a project usually
meets early are:

- **`target-version`** — the oldest Python
  the code must run on. It steers rules
  like pyupgrade's: Ruff will not suggest a
  spelling your oldest Python cannot read.
  If your `pyproject.toml` declares a
  `requires-python`, Ruff infers this from
  it.
- **`exclude`** — folders Ruff should not
  look in at all: generated code, vendored
  copies, build output. Quieter than a
  thousand per-file excuses.
- **`per-file-ignores`** — as above: the
  scalpel beside `exclude`'s fence.
- **Formatter settings** live under
  `[tool.ruff.format]` — quote style, indent
  style, line-ending handling. There are
  few, on purpose (chapter 6).

And the escape hatch that proves the rule:
`--isolated` runs Ruff as if no
configuration existed. When a check behaves
strangely, one `--isolated` run tells you
whether the config or the code is talking.
