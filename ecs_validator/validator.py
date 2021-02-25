from pathlib import Path

import jsonschema

from .utils import load_jsonschema

# globals
JSONSCHEMA_DIR: str = Path('./schemas').resolve()
ERROR_SKIPLIST: list = [ 'properties', 'enum', 'required' ]


def index_mapping_validation_errors(mapping) -> list:
    schema = load_jsonschema(f'{JSONSCHEMA_DIR}/schema.json')
  
    resolver = jsonschema.RefResolver(base_uri=f'{JSONSCHEMA_DIR.as_uri()}/', referrer=schema)

    validator = jsonschema.Draft7Validator(schema, resolver=resolver)
    return sorted(validator.iter_errors(mapping), key=lambda e: e.path)


def get_validation_errors(index_mapping) -> list:
    errors = index_mapping_validation_errors(index_mapping)

    formatted_errors = []

    if errors:
        for error in errors:
            shortened_schema_path = [path_item for path_item in list(error.schema_path) if path_item not in ERROR_SKIPLIST]
            formatted_errors.append(f'{error.message} at {".".join(shortened_schema_path)}') 

    return formatted_errors