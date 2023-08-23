from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from src.main.python.api.app import app
from src.main.python.models.db_connection import setup_db_config


def test_db_connection():
    """
    Call the setup_db_config method to get the database configuration
    Construct the database URI
    Try to establish a connection to the database
    Assert that the connection was successful
    return : db_uri
    """
    db_config = setup_db_config(app)

    db_uri = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"

    try:
        engine = create_engine(db_uri)
        connection = engine.connect()
        connection.close()
        engine.dispose()
        connection_successful = True
    except OperationalError:
        connection_successful = False

    assert connection_successful, "Database connection could not be established"

    return db_uri
