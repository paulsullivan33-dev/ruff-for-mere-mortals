# Installing Ruff

By the end of this chapter Ruff is on your
machine, `ruff --version` answers, and you
know what you actually installed: one file.

Ruff is a single self-contained program.
It is not a Python package that needs a
Python to run (though it can be installed
that way), it does not phone home, and it
keeps no state of its own. Delete the file
and it is gone. This guide's lab used the
official release binary — the route taught
here — and `criteria.md` lists the other
install routes (pip, Homebrew, the
project's installer script, and more) as
documented-only: they all end at the same
`ruff` command.

## The release binary

Ruff is published on its GitHub releases
page, under `astral-sh/ruff`. Each release
offers an archive per platform. The lab
downloaded the Linux x86-64 build of
version 0.17.3:

```console
$ curl -LO https://github.com/astral-sh/ruff/releases/download/0.17.3/ruff-x86_64-unknown-linux-gnu.tar.gz
$ tar xzf ruff-x86_64-unknown-linux-gnu.tar.gz
```

The archive contains one folder holding one
file: the `ruff` program, about 24 MB. The
lab verified its download against the
release's checksum file; the SHA-256 of the
archive it used was
`2b0890f5a55900af741f133918c2656919bbf18c2ab7741b4ca8403a90e647a9`.
Checking a checksum before running a
downloaded binary is a habit worth keeping
for any tool, this one included.

Put the binary somewhere on your `PATH` —
`~/.local/bin` is a good home on Linux —
and confirm:

```console
$ ruff --version
ruff 0.17.3
```

That is the whole install (transcript
`t00-version.txt`). There is no second step:
no daemon to start, no index to build, no
account. macOS and Windows builds follow
the same pattern — pick the archive for
your platform from the same releases page.

## The other doors

If you already live in Python, `pip install
ruff` (ideally into a virtual environment)
installs the same program as a package.
macOS users can use Homebrew, Windows users
WinGet, and the project also offers an
installer script on its website that fetches
the same binary for you. Teams often add
Ruff through the pre-commit framework or a
Docker image instead. The lab did not run
these routes; the documentation describes
them, and they are equivalent — what matters
is that `ruff --version` answers the same
everywhere.

One caution about versions: Ruff is young
and moves quickly, and its default rule set
has grown between releases. If a project's
configuration was written for an older
Ruff, a newer one may report more. That is
the tool keeping its promises louder, not
your code getting worse — chapter 8 shows
how a project pins its choices in a
configuration file so the rules stop
drifting.
