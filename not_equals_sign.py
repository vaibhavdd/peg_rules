import argparse
from typing import Sequence
import re

def not_equals_sign(lines):
#     print('Use != instead of <> in following lines: \n')
    lines_sign = []
    err_flag = 0
    for count, i in enumerate(lines):
        if i.__contains__("<>"):
            lines_sign.append([count,i])
    for count, i in enumerate(lines_sign):
        err_flag = 1
        print("Use != instead of <> on line no. {}\n{}".format(i[0]+1,i[1].strip()))
    if err_flag == 1:
        print('\n--------------------------------\n')
    return err_flag

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Incorrect not equals sign')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        with open(filename, 'r') as f:
            lines = f.readlines()
            f.seek(0)
        if not_equals_sign(lines) == 1:
            retv = 1
    return retv

if __name__ == '__main__':
    raise SystemExit(main())
