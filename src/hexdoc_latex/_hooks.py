from importlib.resources import Package
from pathlib import Path

from hexdoc.core import Properties
from hexdoc.model import Color
from hexdoc.plugin import (
    HookReturn,
    ModPlugin,
    ModPluginImplWithProps,
    hookimpl,
)
from jinja2.sandbox import SandboxedEnvironment
from typing_extensions import override

import hexdoc_latex

from .__version__ import VERSION


class LaTeXPlugin(ModPluginImplWithProps):
    @staticmethod
    @hookimpl
    def hexdoc_mod_plugin(branch: str, props: Properties) -> ModPlugin:
        return LaTeXModPlugin(branch=branch, props=props)


class LaTeXModPlugin(ModPlugin):
    @property
    @override
    def modid(self) -> str:
        return "latex"

    @property
    @override
    def full_version(self) -> str:
        return VERSION

    @property
    @override
    def plugin_version(self) -> str:
        return VERSION

    @override
    def resource_dirs(self) -> HookReturn[Package]:
        return []

    @override
    def jinja_template_root(self) -> tuple[Package, str]:
        return hexdoc_latex, "_templates"

    @override
    def default_rendered_templates(self) -> dict[str | Path, str]:
        return {
            f"{self._filename}.tex": "index.tex.jinja",
        }

    @override
    def update_jinja_env(self, env: SandboxedEnvironment) -> None:
        env.autoescape = False
        env.filters |= {  # type: ignore
            "latex_color": latex_color,
        }

        # https://github.com/samuelcolvin/jinjahtml-vscode#jinja-latex
        env.block_start_string = "((*"
        env.block_end_string = "*))"
        env.variable_start_string = "((("
        env.variable_end_string = ")))"
        env.comment_start_string = "((="
        env.comment_end_string = "=))"

    @property
    def _filename(self):
        if self.props:
            if self.props.book_id:
                return self.props.book_id.path
            return self.props.modid
        return "book"


def latex_color(color: str):
    return Color(color).value.upper()
