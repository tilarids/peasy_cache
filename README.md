peasy_cache
===========

It's a simplest client & server for sharing JSON data and making simple requests. If you ever needed to make lots of requests to the local JSON file and don't want to parse it every time then this tool can be for you. It's simple as hell: it's less than 100 lines of code ATM and I hope there will be no need for tests ever. It's initial purpose was to serve [LLVM's JSON Compilation Database](http://clang.llvm.org/docs/JSONCompilationDatabase.html) and provide an ability to use it from the [SublimeClang](https://github.com/quarnster/SublimeClang). Check the `compilation_db.py` file for that.

Requirements
------------

This tool uses exceptional [opster library](https://github.com/piranha/opster) for command line parsing and [Pyro4 library](http://pypi.python.org/pypi/Pyro4) for interprocess communication

Usage
-----

Start a cache server with `cache.py` and make some requests with `client.py` or use `compilation_db.py` for SublimeClang integration. Use `--help` command line option for help

