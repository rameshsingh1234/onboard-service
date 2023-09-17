import psycopg2

db_params = {
    'host': 'localhost',
    'database': 'sahamati_cr',
    'user': 'postgres',
    'password': 'root',
}

try:
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(**db_params)

    cursor = connection.cursor()
    #cursor.execute("SELECT version();")

    cursor.execute("SELECT count(*) FROM datasets.nishtha_achievedcertification_chydbgqxd0rtzw5hz3zt")
    db_version = cursor.fetchone()

    print("no of records", db_version)

    # Close the cursor and connection
    cursor.close()
    connection.close()

except psycopg2.Error as e:
    print("Error:", e)

