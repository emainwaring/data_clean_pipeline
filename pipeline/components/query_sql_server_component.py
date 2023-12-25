from typing import List
from kfp import dsl

@dsl.component(
               base_image='us-west1-docker.pkg.dev/your-project/ptp-pipeline-images/query_sql_server_component:latest')
def query_sql_server_component(
    query: str,
) -> List[int]:
    try:
        import pyodbc
        import os
        connection_string = os.environ.get("CONNECTION_STRING")
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(query)
        results = [row[0] for row in cursor.fetchall()]
        return results

    except Exception as e:
        raise RuntimeError(f"Error executing SQL query: {str(e)}")

