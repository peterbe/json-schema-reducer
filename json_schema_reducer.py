import json
import os


def make_reduced_dict(schema, original):
    """return a new dict based on a schema and a payload.
    Only the properties from the schema are put in this new dict."""
    return _make_reduced_dict(
        dictify(schema),
        dictify(original)
    )


def _make_reduced_dict(schema, original):
    new_dict = {}
    required = schema.get('required', [])
    for key, prop in schema['properties'].items():
        if prop.get('type') == 'object':
            # need to recurse
            new_dict[key] = make_reduced_dict(
                prop,
                original[key]
            )
        else:
            if key in required or key in original:
                value = original[key]  # try:except attributeerror
                new_dict[key] = value
    return new_dict


def dictify(thing):
    if not isinstance(thing, dict):
        if hasattr(thing, 'read') and callable(thing.read):
            thing = json.load(thing)
        elif os.path.isfile(thing):
            thing = json.load(open(thing))
        else:
            assert isinstance(thing, basestring)
            thing = json.loads(thing)
    assert isinstance(thing, dict)
    return thing


if __name__ == '__main__':
    import sys
    schema = json.load(open(sys.argv[1]))
    json_files = sys.argv[2:]
    for json_file in json_files:
        print json.dumps(
            make_reduced_dict(
                schema,
                json.load(open(json_file)),
                # verbose=True

            ),
            indent=4, sort_keys=True
        )
