import argparse
from typing import Sequence
import re

def cte_padding(lines):
    lines_with_cte = []
    err_flag = 0
    for count, i in enumerate(lines):
        if i.strip() == "with" or i.__contains__("as ("):
            lines_with_cte.append([count,i])
    reg = r'\s*\W\n'
    for i in lines_with_cte:
        if lines[i[0]+1].strip() != '':
            err_flag = 1
            print("Padding absent after line no {} line - {}".format(i[0]+1,lines[i[0]]))
        if lines[i[0]-1].strip() != '':
            err_flag = 1
            print("Padding absent before line no {} line - {}".format(i[0]+1,lines[i[0]]))
        if lines[i[0]+1].lstrip() == '' and lines[i[0]+2].lstrip() == '':
            err_flag = 1
            print("Extra padding present after line no {} line - {}".format(i[0]+1,lines[i[0]]))
        if lines[i[0]-1].strip() == '' and lines[i[0]-2].strip() == '':
            err_flag = 1
            print("Extra padding present before line no {} line - {}".format(i[0]+1,lines[i[0]]))
    lines_select = []
    for count, i in enumerate(lines):
        if i.__contains__("select") and not i.__contains__("select * from"):
            lines_select.append([count,i])
    reg = r'\s*\W\n'
    for i in lines_select:
        if lines[i[0]+1].strip() == '':
            err_flag = 1
            print("Padding present after line no {} line - {}".format(i[0]+1,lines[i[0]]))
        if lines[i[0]-1].strip() == '' and lines[i[0]-2].strip() == '':
            err_flag = 1
            print("Extra padding present before line no {} line - {}".format(i[0]+1,lines[i[0]]))
    if err_flag == 1:
        print('\n--------------------------------\n')
    return err_flag

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Check for cte padding')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        with open(filename, 'r') as f:
            lines = f.readlines()
            f.seek(0)
        if cte_padding(lines) == 1:
            retv = 1
    return retv

if __name__ == '__main__':
    raise SystemExit(main())
