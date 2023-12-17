from importlib.resources import Package
from pathlib import Path

from hexdoc.plugin import (
    HookReturn,
    ModPlugin,
    ModPluginImpl,
    hookimpl,
)
from typing_extensions import override

import hexdoc_latex

from .__version__ import VERSION


class LaTeXPlugin(ModPluginImpl):
    @staticmethod
    @hookimpl
    def hexdoc_mod_plugin(branch: str) -> ModPlugin:
        return LaTeXModPlugin(branch=branch)


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
            "index.tex": "index.tex.jinja",
        }
