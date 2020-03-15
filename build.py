#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import environ
from sys import platform
from bincrafters import build_template_default

if __name__ == "__main__":

    # workaround for platform-specific CPT behaviour
    # see https://github.com/conan-io/conan-package-tools/issues/479
    if platform in ["darwin", "win32"]:
        environ["CONAN_USERNAME"] = "_"
        environ["CONAN_CHANNEL"] = "_"
    else:
        if not environ["CONAN_REFERENCE"].endswith("@/"):
            environ["CONAN_REFERENCE"] += "@/"

    builder = build_template_default.get_builder(build_policy="outdated")
    builder.run()
