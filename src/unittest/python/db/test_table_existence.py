import pytest
import psycopg2
from src.unittest.python.db.test_database_connection import db_params


def test_table_existence(db_params):
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        # Specify the table name you want to check
        table_name = 'user_info'

        # Execute a query to check if the table exists
        cursor.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = %s)", (table_name,))
        exists = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        assert exists, f"Table '{table_name}' does not exist."
    except psycopg2.OperationalError as e:
        pytest.fail(f"Database connection failed: {e}")


# if __name__ == '__main__':
#     pytest.main([__file__])
