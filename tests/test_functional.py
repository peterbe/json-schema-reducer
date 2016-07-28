import json
import os

from json_schema_reducer import make_reduced_dict

_here = os.path.dirname(__file__)


def test_airmozilla_example():
    schema_file = os.path.join(_here, 'contribute-schema.json')
    sample_file = os.path.join(_here, 'contribute-airmo.json')
    result = make_reduced_dict(
        schema_file,
        sample_file
    )
    # We know *exactly* what the difference is between the schema
    # and the sample file.
    # The sample file is identical plus it has two additional
    # keys. One of them nested.
    sample = json.load(open(sample_file))
    assert sorted(sample.keys()) == sorted(result.keys() + ['whatsdeployed'])
    assert 'other_stuff' in sample['participate'].keys()
    assert 'other_stuff' not in result['participate'].keys()
