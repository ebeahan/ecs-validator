from click.testing import CliRunner
import pytest

from .main import root


@pytest.fixture
def runner():
    return CliRunner()


def test_missing_schema_file_arg(runner):
    result = runner.invoke(root, ['--elasticsearch-url', 'http://localhost:9200', '--no-auth', '--index', 'test'])
    assert result.exit_code == 2
    assert "Missing option '--schema-file'" in result.output


def test_missing_elasticsearch_url_arg(runner):
    with runner.isolated_filesystem():
        with open('sample.json', 'w') as f:
            f.write('{ "hello": "world" }')

        result = runner.invoke(root, ['--no-auth', '--index', 'test', '--schema-file', 'sample.json'])
        assert result.exit_code == 1
        assert 'Missing required arguments --cloud-id or --elasticsearch-url' in result.output
