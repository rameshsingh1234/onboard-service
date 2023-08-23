from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.unittest.python.db.test_database_connection import test_db_connection
from src.main.python.models.database import UserInfo
from sqlalchemy.exc import NoResultFound


def test_retrieve_data_from_user_info():
    """
     Get the db_uri from the test_db_connection function
     Create a database session
     Try to retrieve data from the 'user_info' table
     Assert that data is retrieved
     If no data is found, this exception will be raised
     Close the session
    """

    db_uri = test_db_connection()

    engine = create_engine(db_uri)
    session_maker = sessionmaker(bind=engine)
    database_session = session_maker()

    try:
        user_info_data = database_session.query(UserInfo).all()
        assert len(user_info_data) > 0, "No data retrieved from 'user_info' table"
    except NoResultFound:
        assert False, "No data retrieved from 'user_info' table"

    database_session.close()
