#! /bin/env python
import simplejson
from collections import defaultdict

from opster import command
import Pyro4


class Storage(object):
    def __init__(self, data, index_column):
        self.data = data
        self.indexes = {}
        if index_column:
            self.add_index(index_column)

    def add_index(self, index_column):
        # building index
        index = defaultdict(list)
        for (i, row) in enumerate(self.data):
            index_data = row[index_column]
            index[index_data].append(i)
        self.indexes[index_column] = index

    def query(self, column, value):
        if column in self.indexes:
            # there is an index for it!
            index = self.indexes[column]
            return [self.data[i] for i in index[value]]
        else:
            return [row for row in self.data if row[column] == value]


@command()
def main(json_file,
         index=('i', "", "column to index"),
         host=('h', "localhost", "host to run server on"),
         port=('p', 36840, "port to run server on")):
    '''Easy peasy JSON cache server'''
    with open(json_file) as f:
        data = simplejson.load(f)
    storage = Storage(data, index)
    daemon = Pyro4.Daemon(host=host, port=port)
    uri = daemon.register(storage, objectId='peasy_cache')
    print "Ready. URI=[%s]" % uri
    daemon.requestLoop()

if __name__ == '__main__':
    main.command()
