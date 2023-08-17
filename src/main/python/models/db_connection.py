# Python with postgres Db connection
import os
import psycopg2
import yaml


def get_db_config():
    """
    use try catch method to
    Read database configuration from the resources
    """
    test_script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(test_script_dir, '..', '..', '..', '..'))
    config_path = os.path.join(project_root, 'src', 'main', 'python', 'resources', 'db_config.yaml')
    with open(config_path, 'r') as config_file:
        return yaml.safe_load(config_file)


def create_table():
    """
    using try catch method to
    create the 'user_info' table if it doesn't exist in the db
    """
    try:
        db_params = get_db_config()
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        create_table_query = """
            CREATE TABLE IF NOT EXISTS public.user_info1
            (
                clientId character varying,
                userType character varying,
                clientSecret character varying,
                entity_id character varying NOT NULL,
                CONSTRAINT entity_info FOREIGN KEY (entity_id)
                    REFERENCES public.entity_info (entity_id) MATCH SIMPLE
                    ON UPDATE NO ACTION
                    ON DELETE NO ACTION
            )
        """
        cursor.execute(create_table_query)
        connection.commit()

        cursor.close()
        print("Table created")

    except psycopg2.DatabaseError as e:
        connection.rollback()
        raise Exception(f"Error creating table: {e}")


def insert_data(clientId, userType, clientSecret, entity_id):
    """
    Insert data into the 'user_info' table.

    :param clientId: The client ID.
    :param userType: The user type.
    :param clientSecret: The entity type.
    :param entity_id: The entity ID.
    """
    try:
        db_params = get_db_config()
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        insert_query = """
            INSERT INTO public.user_info (clientId, userType, clientSecret, entity_id)
            VALUES (%s, %s, %s, %s)
        """
        data = (clientId, userType, clientSecret, entity_id)
        cursor.execute(insert_query, data)
        connection.commit()

        cursor.close()

        print("Data inserted")
    except psycopg2.DatabaseError as e:
        connection.rollback()
        print("Error inserting data")
        raise Exception(f"Error inserting data: {e}")


# Call the function to create the table
create_table()
