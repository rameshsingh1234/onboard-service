import os
import pytest
import psycopg2
import yaml


@pytest.fixture
def db_params():
    test_script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(test_script_dir, '..', '..', '..', '..'))
    config_path = os.path.join(project_root, 'src', 'main', 'python', 'resources', 'db_config.yaml')

    with open(config_path, 'r') as config_file:
        return yaml.safe_load(config_file)


def test_database_connection(db_params):
    try:
        connection = psycopg2.connect(**db_params)
        connection.close()
        assert True, "Database connection successful."
    except psycopg2.OperationalError as e:
        pytest.fail(f"Database connection failed: {e}")


if __name__ == '__main__':
    pytest.main([__file__])
