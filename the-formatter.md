# The Formatter

By the end of this chapter the lab's worst-
formatted file is in canonical shape, you
have seen the formatter report before it
changes anything in `--check` mode, and
you know how the
formatter differs from the linter you have
been using so far.

`ruff format` is Ruff's second personality.
The linter reads code and comments on it;
the formatter reads code and *rewrites* it
into a single canonical layout: four-space
indents, spaces around operators, one
statement per line, argument lists split or
joined by one set of rules, string quotes
normalised. Where the linter offers
hundreds of rules to pick from, the
formatter deliberately offers almost no
choices. That is the point of a formatter:
the style stops being a decision.

The style itself follows the Black
formatter's conventions closely — if a
project was formatted with Black, Ruff's
formatter aims to produce the same output,
which is what makes switching cheap. The
two are not identical in every corner case,
and chapter 12 says so plainly.

The lab's victim is `unformatted.py`: valid
Python, laid out like it was typed during
an earthquake. Extra spaces everywhere, an
eight-space indent, two statements sharing
a line.

## Check first

Like the linter, the formatter separates
*reporting* from *changing*:

```console
$ ruff format --check toformat.py
1 file would be reformatted
(exit code: 1)
```

In this version Ruff also prints a preview
diff of what would change — lines removed
marked `-`, lines added marked `+` — so
"would be reformatted" comes with evidence.
`--diff` prints that same patch on its own.
Either way, nothing on disk moves, and the
exit code is 1: something *would* change.
CI pipelines live on this mode (chapter 9).

## Format

```console
$ ruff format toformat.py
1 file reformatted
(exit code: 0)
```

The result (transcript `t04-formatter.txt`
keeps before and after):

```python
def greet(name, greeting="hello"):
    message = greeting + ", " + name + "!"
    return message


def total(prices):
    total = 0
    for price in prices:
        total += price
    return total
```

Every change is layout only: spacing,
indentation, the shared line split in two.
No names changed, no logic moved. A second
run is a no-op —

```console
$ ruff format --check toformat.py
1 file already formatted
(exit code: 0)
```

— and the linter agrees the formatted file
is clean. Formatting is *idempotent*: once
done, it stays done, which is why "just run
the formatter" ends formatting arguments in
a way no style guide document ever has.

## Where formatting stops

The formatter will not rescue bad
structure. A 200-line function formats into
a beautifully indented 200-line function.
It also will not touch the contents of
strings, reorder your imports (that is
rule I001's job, chapter 7), or wrap a line
it cannot break — a very long string stays
long, and the linter's line-length rule, if
you enable it, will keep pointing at it.
Formatting is the floor of tidiness, not
the ceiling.
