import os
from src.unittest.python.utils import read_config_file


def setup_db_config(app):
    db_params = read_config_file.read_config(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "db_config.yaml"))

    app.config[
        'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}"
    return db_params
