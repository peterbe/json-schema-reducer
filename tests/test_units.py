import json
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import pytest

from json_schema_reducer import dictify, _make_reduced_dict, ValidationError


def test_dictify():
    buf = StringIO()
    buf.write(json.dumps({'foo': 123}))
    buf.seek(0)
    result = dictify(buf)
    assert result == {'foo': 123}

    result = dictify(json.dumps({'bar': [1, 2, 3]}))
    assert result == {'bar': [1, 2, 3]}


def test_simplest():
    schema = {
        '$schema': 'http://json-schema.org/draft-04/schema#',
        'type': 'object',
        'properties': {
            'foo': {
                'type': 'string',
            },
            'bar': {
                'type': 'string',
            },
        }
    }
    sample = {
        'foo': 'Hej!',
        'bar': 'Hoo',
        'baz': "Don't include me in the result",
    }
    result = _make_reduced_dict(
        schema,
        sample
    )
    assert result == {'foo': 'Hej!', 'bar': 'Hoo'}


def test_excess():
    schema = {
        '$schema': 'http://json-schema.org/draft-04/schema#',
        'type': 'object',
        'properties': {
            'foo': {
                'type': 'string',
            },
            'bar': {
                'type': 'string',
            },
        }
    }
    sample = {
        'foo': 'Hej!',
        'baz': "Don't include me in the result",
    }
    result = _make_reduced_dict(
        schema,
        sample
    )
    assert result == {'foo': 'Hej!'}


def test_excess_nested():
    schema = {
        '$schema': 'http://json-schema.org/draft-04/schema#',
        'type': 'object',
        'properties': {
            'foo': {
                'type': 'string',
            },
            'bar': {
                'type': 'object',
                'properties': {
                    'one': {
                        'type': 'string',
                    },
                }
            },
        }
    }
    sample = {
        'foo': 'Hej!',
        'baz': "Don't include me in the result",
    }
    result = _make_reduced_dict(
        schema,
        sample
    )
    assert result == {'foo': 'Hej!'}


def test_required_error():
    schema = {
        '$schema': 'http://json-schema.org/draft-04/schema#',
        'type': 'object',
        'required': ['foo', 'bar'],
        'properties': {
            'foo': {
                'type': 'string',
            },
            'bar': {
                'type': 'string',
            },
        }
    }
    sample = {
        'foo': 'Hej!',
        # missing 'bar'
    }
    with pytest.raises(ValidationError) as excinfo:
        _make_reduced_dict(
            schema,
            sample
        )
    assert 'bar' in str(excinfo.value)
