===================
json-schema-reducer
===================

.. image:: https://travis-ci.org/peterbe/json-schema-reducer.svg?branch=master
    :target: https://travis-ci.org/peterbe/json-schema-reducer

.. image:: https://badge.fury.io/py/json-schema-reducer.svg
    :target: https://pypi.python.org/pypi/json-schema-reducer

Extract from a JSON/dict only whats in the JSON Schema. Assumes that the
JSON/dict you supply is valid according to the JSON Schema you also supply.


Installation
============

    pip install json-schema-reducer

How to use it
=============

Suppose you have two files on disk: ``schema.json`` and ``mything.json``.
And suppose that the ``schema.json`` only lists the properties ``foo`` and
``bar`` but the file ``mything.json`` contains many more things::

    >>> from json_schema_reducer import make_reduced_dict
    >>> make_reduced_dict('schema.json', 'mything.json')
    {'foo': 'value1', 'bar': 'value2'}

The arguments are flexible. You can also do this::

    >>> make_reduced_dict(open('schema.json'), open('mything.json'))

Or this::

    >>> make_reduced_dict(open('schema.json').read(), open('mything.json').read())

Or this::

>>> make_reduced_dict(
...   json.load(open('schema.json')),
...   json.load(open('mything.json')))


Runnings tests
==============

Simply run::

    python setup.py test


Version History
===============

0.1.0
  * First, hopefully, working version.
