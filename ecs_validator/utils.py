import json


def load_jsonschema(schema_file) -> dict:
    # resp = requests.get(schema_uri, timeout=request_timeout)
    # return resp.json()
    with open(schema_file, 'r') as source:
        schema_json = json.load(source)

    return schema_json


def extract_index_mappings(index_mappings, index_name) -> dict:
    return index_mappings.get(index_name).get('mappings').get('properties') 
