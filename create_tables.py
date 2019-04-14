import psycopg2
from sql_queries import create_table_queries, drop_table_queries

"""create_database:
    Recreates the datawarehouse and establishes a connection to it
    
    Returns:
        cur: cursor to the database
        conn: connection to the database
"""
def create_database():
    # connect to default database
    conn = # set up your data connection
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn

"""drop_tables:
    Drops the tables in the datawarehouse
"""
def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

"""create_tables:
    Creates the tables in the datawarehouse
"""
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
