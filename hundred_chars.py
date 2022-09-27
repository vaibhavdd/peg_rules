import argparse
from typing import Sequence
import re

def hundred_chars(lines):
    err_flag = 0
    for count, i in enumerate(lines):
        cnt = 0
        for j in i:
            if j != ' ':
                cnt=cnt+1
        if cnt>100:
            err_flag = 1
            print("\nLine no. {} contains more than 100 characters:\n{}".format(count+1,i.strip()))
    if err_flag == 1:
        print('\n--------------------------------\n')
    return err_flag

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Max 100 Characters in a line')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        with open(filename, 'r') as f:
            lines = f.readlines()
            f.seek(0)
        if hundred_chars(lines) == 1:
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
