#!/usr/bin/env python
# @author: Jennings Zhang <Jennings.Zhang@childrens.harvard.edu>

import sys
from argparse import ArgumentParser
from pathlib import Path
import subprocess as sp
from typing import Optional

import numpy as np
import numpy.typing as npt

parser = ArgumentParser(description='Create transformation for centering a mesh about the origin')
parser.add_argument('input_file', type=Path,
                    help='Wavefront .obj surface file')
parser.add_argument('output_file', type=Path,
                    help='output .xfm file')


def main():
    options = parser.parse_args()
    with options.input_file.open('r') as f:
        parsed_data = map(parse_vertex_line, f)
        points = np.array([p for p in parsed_data if p is not None])
    center = np.mean(points, axis=0)
    slide = 0 - center
    cmd = ('param2xfm', '-translation', *map(str, slide), options.output_file)
    proc = sp.run(cmd)
    sys.exit(proc.returncode)


def parse_vertex_line(line: str) -> Optional[npt.NDArray[np.float32]]:
    data = line.strip().split()
    if data[0] != 'v':
        return None
    arr = np.fromiter(map(float, data[1:]), dtype=np.float32)
    assert len(arr) == 3
    return arr


if __name__ == '__main__':
    main()

