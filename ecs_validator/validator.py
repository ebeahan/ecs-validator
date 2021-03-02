from pathlib import Path

import jsonschema

from .utils import load_jsonschema

# globals
JSONSCHEMA = "https://raw.githubusercontent.com/ebeahan/ecs-validator/main/schemas/schema.json"
ERROR_SKIPLIST: list = [ 'properties', 'enum', 'required' ]


def index_mapping_validation_errors(mapping) -> list:
    schema = load_jsonschema(JSONSCHEMA)
  
    validator = jsonschema.Draft7Validator(schema)
    return sorted(validator.iter_errors(mapping), key=lambda e: e.path)


def get_validation_errors(index_mapping) -> list:
    errors = index_mapping_validation_errors(index_mapping)

    formatted_errors = []

    if errors:
        for error in errors:
            shortened_schema_path = [path_item for path_item in list(error.schema_path) if path_item not in ERROR_SKIPLIST]
            formatted_errors.append(f'{error.message} at {".".join(shortened_schema_path)}') 

    return formatted_errors