import argparse
from typing import Sequence
import re

def inner_join_keyword(lines):
    lines_join = []
    err_flag_inner = 0
    err_flag_on = 0
    for count, i in enumerate(lines):
        if i.__contains__("join"):
            lines_join.append([count,i])

    lines_after_join = []
    flag = 0
    for count, i in enumerate(lines):
        if flag == 1:
            flag = 0
            lines_after_join.append([count, i])
        if i.__contains__("join"):
            flag = 1

    join_ls = ['inner', 'left', 'outer', 'right']
    for count, i in enumerate(lines_join):
        flag = 0
        for k in join_ls:
            if flag == 0:
                if k in i[1]:
                    flag = 1
        if flag ==0:
            err_flag_inner = 1
            print("Use Inner keyword on line no. {}\n{}".format(i[0]+1,i[1].strip()))
    if err_flag_inner == 1:
        print('\n--------------------------------\n')
    for count, i in enumerate(lines_after_join):
        if ' using' in i[1]:
            err_flag_on = 1
            print(f"Use 'On' keyword instead of 'Using' on Line no. {i[0]+1}\n{i[1].strip()}")
    if err_flag_on == 1:
        print('\n--------------------------------\n')
    return err_flag_inner + err_flag_on

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Inner keyword missing')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        with open(filename, 'r') as f:
            lines = f.readlines()
            f.seek(0)
        if inner_join_keyword(lines) > 0:
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
