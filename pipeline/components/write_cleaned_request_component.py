from kfp import dsl
from kfp.dsl import Input, Dataset


@dsl.component(
    base_image='us-west1-docker.pkg.dev/your-project/ptp-pipeline-images/write_cleaned_request_component:latest')
def write_cleaned_request_component(cleaned_requests: Input[Dataset], table_name: str, pipeline_id: str):
    import pyodbc
    import pandas as pd
    import os
    df = pd.read_csv(cleaned_requests.path, header=0)
    df['pipeline_run'] = pipeline_id
    connection_string = os.environ.get("CONNECTION_STRING")
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        for index, row in df.iterrows():
            row = [value if pd.notna(value) else None for value in row]
            insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['?'] * len(df.columns))})"
            cursor.execute(insert_query, tuple(row))
        conn.commit()
        conn.close()
        print(f"Data appended to table '{table_name}' successfully.")
    except Exception as e:
        print(f"Error appending cleaned data to SQL Server: {str(e)}")
