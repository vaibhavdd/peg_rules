import argparse
from typing import Sequence
import re

def cte_alignment(text):
    def find_parens(s):
        toret = {}
        pstack = []

        for i, c in enumerate(s):
            if c == '(':
                pstack.append(i)
            elif c == ')':
                toret[pstack.pop()] = i
        return toret
    bracket_dict = find_parens(text)
    opening_bracks = list(bracket_dict.keys())
    closing_bracks = list(bracket_dict.values())
    cte_dict = {}
    err_flag = 0
    for i in bracket_dict.keys():
        if text[i-4:i] == ' as ':
            cte_dict[i] = bracket_dict[i]
    for start_brack in cte_dict.keys():
        k = start_brack
        while text[k] != '\n':
            k=k-1
        cte_name = text[k:start_brack]
        if cte_name[1] == ' ':
            new_line_count = 0
            for i in text[:start_brack]:
                if i=='\n':
                    new_line_count+=1
            err_flag = 1
            print('CTE Alignment incorrect for on line no. {}'.format(new_line_count+1))
        end_brack = cte_dict[start_brack]
        if text[end_brack-1] != '\n':
            new_line_count = 0
            for i in text[:end_brack]:
                if i=='\n':
                    new_line_count+=1
            err_flag = 1
            print('CTE Alignment incorrect for on line no. {}'.format(new_line_count+1))
    if err_flag == 1:
        print('\n--------------------------------\n')

    return err_flag

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Check for cte alignment')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        with open(filename, 'r') as f:
            text = f.read()
            f.seek(0)
        if cte_alignment(text) == 1:
            retv = 1
    return retv

if __name__ == '__main__':
    raise SystemExit(main())
