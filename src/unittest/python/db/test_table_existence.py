from src.main.python.models.database import db, create_tables
from src.main.python.api.app import app
from sqlalchemy import inspect
from src.unittest.python.db.test_database_connection import test_db_connection


def test_user_info_table_exists():
    """
    Get the db_uri from the test_db_connection function
    Call the create_tables method to create the tables (if they don't exist)
    Check if the 'user_info' table exists
    """
    db_uri = test_db_connection()

    with app.app_context():
        create_tables()

    with app.app_context():
        engine = db.create_engine(db_uri)
        inspector = inspect(engine)
        assert 'user_info' in inspector.get_table_names()
