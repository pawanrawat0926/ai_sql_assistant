import snowflake.connector
import pandas as pd
from app_secrets import *

def execute_sf_query(sql):
    # Snowflake connection parameters
    connection_params = {
        'user': SF_USER,
        'password': SF_PASSWORD,
        'account': SF_ACCOUNT,
        'warehouse': SF_WAREHOUSE,
        'database': SF_DATABASE,
        'schema': SF_SCHEMA,
        'role':SF_ROLE
    }

    query=sql

    try:
        # Establish a connection to Snowflake
        conn = snowflake.connector.connect(**connection_params)

        # Create a cursor object
        cur = conn.cursor()

        # Execute the query
        try:
            cur.execute(query)
        except snowflake.connector.errors.ProgrammingError as pe:
            print("Query Compilation Error:", pe)
            return("Query compilation error")

        # Fetch all results
        query_results = cur.fetchall()

        # Get column names from the cursor description
        column_names = [col[0] for col in cur.description]

        # Create a Pandas DataFrame
        data_frame = pd.DataFrame(query_results, columns=column_names)

        # Print the DataFrame
        #print(data_frame)
        return data_frame

    except snowflake.connector.errors.DatabaseError as de:
        print("Snowflake Database Error:", de)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the cursor and connection
        try:
            cur.close()
        except:
            pass

        try:
            conn.close()
        except:
            pass


if __name__ == "__main__":
    # Snowflake query
    query = '''
            select n.n_name , count(*) as order_count from analytics.raw.orders o 
            inner join analytics.raw.customer c on o.o_custkey = c.c_custkey
            inner join analytics.raw.nation n on c.c_nationkey = n.n_nationkey
            group by n.n_name order by order_count desc limit 3
    '''
    execute_sf_query(query)