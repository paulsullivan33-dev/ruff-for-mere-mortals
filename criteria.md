# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's traffic is the lab talking to itself.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 12 names what the tool
   cannot do: it never runs your code, so behaviour stays
   unproven; it does not follow types, so a whole class of
   error passes silently; its fixes are text edits, and the
   unsafe kind can change what a program does; its formatter
   follows Black closely but not exactly; and its default
   rule set has grown between versions and may move again.
8. **The care rule is in the text, early.** Chapter 1 and the
   README state the rule plainly — *only fix what you can
   restore, and read every diff* — before any procedure
   depends on it, and later chapters point back to it where
   the tooling would make crossing the line easy.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU Ubuntu 24.04 sandbox with Python
3.12 installed. Ruff **0.17.3** was verified as the official
standalone release binary, downloaded from the project's
GitHub releases (archive SHA-256
`2b0890f5a55900af741f133918c2656919bbf18c2ab7741b4ca8403a90e647a9`)
and run against fixture files written for this guide. All
transcripts live in `ruff-lab/transcripts/`; the fixtures are
in `ruff-lab/fixtures/` and the two configuration projects in
`ruff-lab/projects/`.

Run for real, with transcripts as evidence:

- Version and the single-binary install from the release
  archive (t00).
- A first check on a fixture with planted mistakes: eight
  diagnostics across five rules, exit code 1, and a clean
  fixture passing with exit code 0 (t01). Exit code 2 was
  also produced for real, by selecting a rule family that
  does not exist.
- `--statistics` counts, and the full built-in documentation
  of a rule via `ruff rule F401` (t02).
- Fixing in three passes: `--fix --diff` previewing three
  edits, `--fix` applying the safe ones, and
  `--fix --unsafe-fixes` removing assignments to unused
  variables and visibly changing a function's shape — the
  two diagnostics with no fix (undefined name, bare
  `except`) surviving all passes (t03).
- The formatter end to end: `--check` reporting and exiting
  1, `--diff`, the reformat itself, a second `--check`
  passing, and the linter agreeing the formatted file is
  clean (t04).
- Selecting and ignoring: `--select I` isolating import
  order, `--ignore F401` removing three findings, `--select
  E501` producing "Line too long (144 > 88)", and `--select
  ALL` raising the same file from 8 findings to 26 (t05).
- `noqa` comments: one targeted comment removing exactly one
  finding, and `--add-noqa` annotating every offending line
  until the check passed (t06).
- Configuration both ways: a `pyproject.toml` with a
  72-character line length, an explicit rule selection, and
  a per-file ignore that silenced the worse of two long-line
  files; and a `ruff.toml` restricting a project to F401
  alone (t07).
- Pipeline output: `--output-format github` annotations for
  all eight findings and the `--output-format json`
  structure, fix edits included (t08).
- Scale: the whole installed Python 3.12 standard library
  checked with the defaults — 5,585 findings in 3.8 seconds
  on the sandbox (t09).
- The default rule set counted from `--show-settings`: 408
  rules enabled with no configuration (t10) — the finding
  that corrected this guide's own expectation of the older,
  smaller default set.

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- Installation by pip, Homebrew, WinGet, cargo or conda,
  the project's installer script, and its Docker images.
  The lab verified the release binary only; every route
  ends at the same command.
- Editor integrations: the VS Code extension, the language
  server (`ruff server`), and diagnostics in the editor.
- The pre-commit framework's Ruff hooks and the official
  GitHub Action. The action's `--output-format github`
  output was verified locally, as listed above.
- Jupyter notebook checking and formatting, and watch
  mode; the lab's fixtures are plain files and its runs
  are batch runs.
- The priority of `ruff.toml` over `pyproject.toml` when
  both exist in one folder, and `extend-select` and the
  formatter's handful of options, which are named but not
  exercised.
- The neighbours in chapter 11 are characterised, not
  benchmarked, and the formatter's corner-case differences
  from Black are stated from the project's documentation
  rather than demonstrated.

Fixtures are this guide's own and deliberately generic: a
config loader with planted mistakes, a greeting program with
planted layout problems, an unsorted import block, and one
long sentence about a warehouse inventory item. No example
is modelled on any real person, project, service or
organisation.
