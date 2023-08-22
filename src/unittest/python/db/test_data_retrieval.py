import pytest
import psycopg2
from src.unittest.python.db.test_database_connection import db_params


def test_data_retrieval(db_params):
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        table_name = 'user_info'

        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        assert len(data) > 0, f"No data retrieved from table '{table_name}'."

    except psycopg2.OperationalError as e:
        pytest.fail(f"Database connection failed: {e}")


# if __name__ == '__main__':
#     pytest.main([__file__])
