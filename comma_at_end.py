import argparse
from typing import Sequence
import re

def comma_at_end(lines):
    lines_sign = []
    err_flag = 0
    for count, i in enumerate(lines):
        if i.lstrip() != '':
            if i.lstrip()[0].__contains__(","):
                lines_sign.append([count,i])
                err_flag = 1
                print('Line no. {} contains comma at start of the line: \n{}'.format(count,i.strip()))
    if err_flag == 1:
        print('\n--------------------------------\n')
    return err_flag

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Comma should be at column end')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        with open(filename, 'r') as f:
            lines = f.readlines()
            f.seek(0)
        if comma_at_end(lines) == 1:
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
