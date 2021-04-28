from pathlib import Path

import json
import jsonschema


# globals
ERROR_SKIPLIST: list = [ 'properties', 'enum', 'required' ]


def get_validation_errors(index_mapping, schema) -> list:

    validator = jsonschema.Draft7Validator(schema)

    errors = sorted(validator.iter_errors(index_mapping), key=lambda e: e.path)

    formatted_errors = []

    if errors:
        for error in errors:
            shortened_schema_path = [path_item for path_item in list(error.schema_path) if path_item not in ERROR_SKIPLIST]
            formatted_errors.append(f'{error.message} at {".".join(shortened_schema_path)}') 

    return formatted_errors
