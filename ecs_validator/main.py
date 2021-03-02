import click
from elasticsearch import exceptions

from .es import get_elasticsearch_client
from .validator import get_validation_errors
from .utils import extract_index_mappings

@click.command()
@click.option('--cloud-id')
@click.option('--elasticsearch-url')
@click.option('--es-user')
@click.option('--es-password')
@click.option('--timeout', default=60, help='Timeout for Elasticsearch client.')
@click.option('--index', "-i", help='Name of index to evaluate.', required=True)
@click.option('--no-auth', help='Disable HTTP authentication to Elasticsearch.', is_flag=True)
def root(cloud_id, elasticsearch_url, es_user, es_password, timeout, index, no_auth):
    click.echo()
    click.echo(f'Retrieving index settings for index `{index}`...')
    click.echo()

    # init es client
    client = get_elasticsearch_client(cloud_id, elasticsearch_url, es_user, es_password, timeout, no_auth)
    
    # Retrieve the index settings
    try:
        index_settings = client.indices.get(index=index)
    except exceptions.NotFoundError:
        raise click.ClickException(f'No such index `{index}` found at {elasticsearch_url}')

    # Validate the index settings mapping properties 
    mappings = extract_index_mappings(index_settings, index)
    validation_errors = get_validation_errors(mappings)

    if not validation_errors:
        click.secho('No validation errors.', bold=True)
    else:
        click.secho(f'*** {len(validation_errors)} validation error(s) detected. ***', bold=True)
        click.echo()
        for error in validation_errors:
            click.echo(f'* {error}')
        exit(1)