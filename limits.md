# Limits

What Ruff cannot do, stated as plainly as
the rest of the guide. None of these are
bugs; they are the edges of the idea.

**Ruff does not run your code.** Every
finding comes from reading text. It can
prove a name is undefined in a file; it
cannot prove the program works. Code that
builds names dynamically — `globals()`
tricks, `exec`, plugin systems that load
by string — can hide real uses from it,
producing findings that are wrong, or
hide real mistakes, producing silence that
is wrong. The lab's F841 surprise in
chapter 5 is the small version: a text
edit changed a function's shape without
understanding it.

**Ruff does not type-check.** Passing a
string where a number belongs, calling a
method the object does not have — Ruff
does not follow types, so it does not see
these. That is the type checkers' work
(chapter 11), and a project that wants the
whole static picture runs both.

**A green check is not correctness.** "All
checks passed" means *none of the enabled
patterns were found*. A program can be
lint-clean, formatted, and wrong. Ruff
raises the floor; tests and thought raise
the ceiling.

**Fixes are edits, not understanding.**
Safe fixes are safe because their pattern
cannot change behaviour — and even they
deserve a glance at the diff. Unsafe fixes
are labelled and gated, but the label is a
heuristic about a pattern, not a proof
about your program. Chapter 5's fix was
correct by the pattern and still changed
what the function did.

**The formatter is not Black, exactly.**
It follows Black's style closely, and most
files come out identical, but corner cases
differ, and the project does not promise
byte-for-byte equality forever. A team
switching tools should expect one
reformatting commit and a few surprises in
exotic constructs, and should not mix two
formatters in one repository.

**The defaults are a moving target.** Ruff
is young. Its default rule set grew
substantially before version 0.17 — the
roughly 400 default rules this guide
counted surprised the lab, which expected
the smaller historical set — and it may
move again. The defence is chapter 8: a
project that writes its selection down is
insulated; a project that floats on the
defaults accepts the drift.

**Opinions are not errors.** Most of the
thousands of available rules encode
somebody's preference. Enabling families
wholesale (chapter 7's ALL experiment:
twenty-six findings where the defaults
found eight) trades real signal for noise
and teaches a team to ignore the tool. The
limit here is social, and it is the one
that most often ends a linting project.
