# Troubleshooting

The failures this guide's lab actually met,
and the ones every new Ruff user meets
soon after.

## "Ruff reports things I did not ask for"

You upgraded, or a project's config is not
the one being read. First check which
configuration Ruff found — it walks upward
from each file, so a file outside the
project tree uses a different config, or
none. Then run the same file with
`--isolated`, which ignores all
configuration: if the finding survives,
it is in the defaults (which have grown
between versions — chapter 12); if it
vanishes, it is your config talking.
`ruff check --show-settings <file>` prints
the fully resolved settings, including the
exact list of enabled rules, when you need
the definitive answer.

## "Ruff fixed my code and broke it"

Almost always an unsafe fix applied without
reading the diff. The fix is marked unsafe,
its diagnostic carries the note, and the
defence is the guide's rule: version
control first, read every diff. Revert the
change, re-apply with plain `--fix` (safe
fixes only), and handle the unsafe ones by
hand. If a *safe* fix genuinely changed
behaviour, that is a bug worth reporting to
the project — with the smallest example you
can cut it down to.

## "Exit code 2"

Ruff itself failed: typically a rule code
that does not exist in your version (the
lab produced this with `--select ZZZ` and
got a clear "Unknown rule selector"
message), a malformed configuration file,
or a path that cannot be read. Exit 2 is
deliberately distinct from 1 so a pipeline
can tell "the code failed the check" from
"the check never ran". Read the error; it
names the setting and where it came from.

## "The formatter and the linter disagree"

One file, two complaints that chase each
other: the formatter splits a line, the
linter's setting wanted it joined. This
happens when line-length or a style rule in
the lint selection fights the formatter's
layout. The settlement is that the lint
selection serves the formatter: check for a
`line-length` set in one place and relied
on in another, and drop lint rules that
police pure layout the formatter owns.

## "A finding is wrong"

Start with `ruff rule <CODE>` — a third of
the time the rule means something narrower
than its one-line message, and your code is
the exception it documents (F401's
re-export spelling is the classic). If the
rule is right and the code is deliberate,
the order of preference is: a targeted
`# noqa: CODE` with a comment saying why, a
per-file ignore in configuration, and only
then a global ignore. Each wider tool
excuses more future mistakes along with the
present one.

## "It is too fast to have done anything"

It did it. Checking thousands of files in
seconds is the normal experience, and the
lab's standard-library run (5,585 findings
in 3.8 seconds on a two-CPU machine) is the
evidence. If a run feels instant *and*
reports nothing, confirm it looked where
you think it looked: pass the file
explicitly once, and check the exit code.
