#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
helpers for amimoto_alexa
"""

from __future__ import print_function
from __future__ import unicode_literals
import yaml

flatten=lambda i:[a for b in i for a in(flatten(b)if hasattr(b,'__iter__')else(b,))]

with open('data/aliases.yml') as f:
    aliases = yaml.load(f.read())
    words = flatten(aliases.values())

if len(words) == len(set(words)):
    print("No dup aliases")
else:
    raise StandardError, "found dup aliases!!"