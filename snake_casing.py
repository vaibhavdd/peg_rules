import argparse
from typing import Sequence
import re

def snake_casing(lines):
    lines_uppercase = []
    flag=0
    err_flag = 0
    reg = '[A-Za-z]+.'
    for count, i in enumerate(lines):
        if i.islower()==False and i!='\n':
            x=i.split("'")
            for cnt,j in enumerate(x):
                if re.search(reg, j):
                    if cnt%2 ==0 and j.islower()==False and j!='\n':
                        flag=1
                        lines_uppercase.append([count+1,i])
                        err_flag = 1
                        print('Line no. {} contains uppercase characters:\n{}'.format(count+1,i.strip()))
    if err_flag == 1:
        print('\n--------------------------------\n')
    return err_flag

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Check for snake casing')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        with open(filename, 'r') as f:
            lines = f.readlines()
            f.seek(0)
        if snake_casing(lines) == 1:
            retv = 1
    return retv

if __name__ == '__main__':
    raise SystemExit(main())
