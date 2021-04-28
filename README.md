# ecs-validator

The `ecs-validator` tool uses [JSON Schema](https://json-schema.org) spec to validate if an [Elasticsearch](https://elastic.co) index is compliant with the [Elastic Common Schema (ECS)](https://www.elastic.co/what-is/ecs).

## Getting Started

Install dependencies using `pipenv`:

```
$ pipenv install 
```

Confirm everything is installed properly:

```
$ python -m ecs_validator --help
Usage: ecs_validator [OPTIONS]

Options:
  --cloud-id TEXT
  --elasticsearch-url TEXT
  --es-user TEXT
  --es-password TEXT
  --timeout INTEGER         Timeout for Elasticsearch client.
  -i, --index TEXT          Name of index to evaluate.  [required]
  --no-auth                 Disable HTTP authentication to Elasticsearch.
  --schema-file PATH        File name of the JSON schema to evaluate against.
                            [required]

  --help                    Show this message and exit.

```

Basic usage:

```
$ python -m ecs_validator --elasticsearch-url http://localhost:9200 --no-auth --index non-compliant-index-name --schema-file schemas/ecs-1.9.0.json

Retrieving index settings for index `bad-ecs-0005`...

*** 5 validation error(s) detected. ***

* 'text' is not one of ['keyword'] at agent.build.original.type
* 'keyword' is not one of ['text'] at error.message.type
* 'flattened' is not one of ['object'] at labels.type
* 'keyword' is not one of ['text'] at message.type
* 'text' is not one of ['keyword'] at tags.type
```