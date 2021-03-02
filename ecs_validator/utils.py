import json

import requests

def load_jsonschema(schema_uri, request_timeout=60) -> dict:
    resp = requests.get(schema_uri, timeout=request_timeout)
    return resp.json()


def extract_index_mappings(index_mappings, index_name) -> dict:
    return index_mappings.get(index_name).get('mappings').get('properties') 
