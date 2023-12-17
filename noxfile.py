from __future__ import annotations

import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session
def build(session: nox.Session):
    session.install("-e", ".")

    session.run("hexdoc", "build")


@nox.session
def hexcasting(session: nox.Session):
    session.chdir("test/hexcasting")
    session.install("-r", "requirements.txt")

    session.run(
        "hexdoc",
        "--quiet-lang=zh_cn",
        "--quiet-lang=ru_ru",
        "build",
        "./out",
        "--branch=main",
        env={
            "GITHUB_REPOSITORY": "hexdoc-dev/hexdoc-latex",
            "GITHUB_SHA": "main",
            "GITHUB_PAGES_URL": "https://hexdoc-dev.github.io/hexdoc-latex/",
        },
    )
