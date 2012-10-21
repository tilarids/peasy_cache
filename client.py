#! /bin/env python
from opster import command
import Pyro4


def cache_client(host, port):
    uri = "PYRO:peasy_cache@%s:%s" % (host, port)
    storage = Pyro4.Proxy(uri)
    return storage.query


@command()
def main(column,
         value,
         host=('h', "localhost", "host to connect to"),
         port=('p', 36840, "port to connect to")):
    '''Easy peasy JSON cache client'''
    client = cache_client(host, port)
    print client(column, value)

if __name__ == '__main__':
    main.command()
