import json
from StringIO import StringIO

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
