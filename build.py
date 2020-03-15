#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_default

if __name__ == "__main__":

    builder = build_template_default.get_builder(username="_", channel="_", build_policy="outdated")
    builder.run()
