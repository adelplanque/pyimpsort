import io
import sys
import typing

from pyimpsort import pyimpsort

import pytest


if sys.version_info >= (3, 7):

    from dataclasses import dataclass, field

    @dataclass
    class TestCase:
        infname: str
        outfname: str
        group: bool = False

    @dataclass
    class Args:
        infile: typing.TextIO
        outfile: typing.TextIO
        group: bool = False
        site: bool = False
        local: list = field(default_factory=list)

else:

    class TestCase:

        def __init__(self, infname, outfname, group=False):
            self.infname = infname
            self.outfname = outfname
            self.group = group

    class Args:

        def __init__(self, infile, outfile, group=False, site=False, local=()):
            self.infile = infile
            self.outfile = outfile
            self.group = group
            self.site = site
            self.local = local


@pytest.mark.parametrize(
    "test_case",
    [
        TestCase("samples/1.in", "samples/1.out"),
        TestCase("samples/2.in", "samples/2.out"),
        TestCase("samples/3.in", "samples/3.out"),
        TestCase("samples/4.in", "samples/4.out"),
        TestCase("samples/5.in", "samples/5.out"),
        TestCase("samples/6.in", "samples/6.out"),
        TestCase("samples/7.in", "samples/7.out"),
        TestCase("samples/8.in", "samples/8.out"),
        TestCase("samples/9.in", "samples/9.out"),
        TestCase("samples/10.in", "samples/10.out"),
        TestCase("samples/11.in", "samples/11.out", group=True),
        TestCase("samples/12.in", "samples/12.out"),
        TestCase("samples/12.in", "samples/12-grouped.out", group=True),
        TestCase("samples/13.in", "samples/13.out"),
    ],
)
def test_sort_import(test_case):
    with io.open(test_case.infname) as fin, io.open(test_case.outfname) as fout, io.StringIO() as res:
        pyimpsort(Args(fin, res, test_case.group))
        assert res.getvalue().split("\n") == fout.read().split("\n")
