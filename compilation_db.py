#! /bin/env python
import re
import sys

from opster import command

from client import cache_client


compilation_database_pattern = re.compile('(?<=\s)-[DIOUWfgs][^=\s]+(?:=\\"[^"]+\\"|=[^"]\S+)?')


@command()
def main(fname):
    '''An example that uses easy peasy JSON cache server: LLVM compilation database interface'''
    client = cache_client(host="localhost", port=36840)
    for ret in client('file', fname):
        cmd = ret['command']
        sys.stdout.write('\n'.join(p.strip() for p in compilation_database_pattern.findall(cmd)))

if __name__ == '__main__':
    main.command()
