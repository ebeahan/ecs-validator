import click
import elasticsearch
from elasticsearch import Elasticsearch

def get_elasticsearch_client(cloud_id=None, elasticsearch_url=None, es_user=None, es_password=None,
                             timeout=None, no_auth=False) -> Elasticsearch:

    if not (cloud_id or elasticsearch_url):
       raise click.ClickException('Missing required arguments --cloud-id or --elasticsearch-url')

    if not no_auth:
        es_user = es_user or click.prompt('es_user')
        es_password = es_password or click.prompt('es_password')
        http_auth=(es_user, es_password)
    else:
        http_auth=None
    hosts = [elasticsearch_url] if elasticsearch_url else None
    timeout = timeout if timeout else 60

    try:
        client = Elasticsearch(hosts=hosts, cloud_id=cloud_id, http_auth=http_auth, timeout=timeout)
        client.info()
        return client

    except elasticsearch.AuthenticationException as error:
        error_message = f'Failed authentication for {elasticsearch_url or cloud_id}.\nReason: {error}'
        raise click.ClickException(error_message)
