import argparse
from typing import Sequence
import re

def select_indentation(lines):
    lines_select = []
    err_flag = 0
    for count, i in enumerate(lines):
        if i.__contains__("select") and not i.__contains__("select * from final") and \
        (lines[count-2].__contains__(' as (') or lines[count-1].__contains__('union') or lines[count-1].__contains__('except')):
            lines_select.append([count,i])
    reg = '[a-zA-Z]'
    for j in range(0,len(lines_select)):
        match = re.search(reg,lines_select[j][1])
        if(match.start()!=4):
            err_flag = 1
            print("Select keyword indentation incorrect at line no {}".format(lines_select[j][0]))
    if err_flag == 1:
        print('\n--------------------------------\n')
    return err_flag

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Check for indentation of select keyword')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        with open(filename, 'r') as f:
            lines = f.readlines()
            f.seek(0)
        if select_indentation(lines) == 1:
            retv = 1
    return retv

if __name__ == '__main__':
    raise SystemExit(main())
