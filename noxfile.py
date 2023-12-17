from __future__ import annotations

import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session
def hexcasting(session: nox.Session):
    with session.chdir("test/hexcasting"):
        session.install("-r", "requirements.txt")

    session.run(
        "hexdoc",
        "--quiet-lang=zh_cn",
        "--quiet-lang=ru_ru",
        "build",
        "./out",
        "--branch=main",
        "--props=test/hexcasting/hexdoc.toml",
    )
