import json

def load_jsonschema(schema_file) -> dict:
    with open(schema_file) as schema:
        return json.load(schema)


def extract_index_mappings(index_mappings, index_name) -> dict:
    return index_mappings.get(index_name).get('mappings').get('properties') 
