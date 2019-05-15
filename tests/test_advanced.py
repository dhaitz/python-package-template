# -*- coding: utf-8 -*-

from .context import sample


def test_thoughts():
    assert(sample.hmm() is None)
