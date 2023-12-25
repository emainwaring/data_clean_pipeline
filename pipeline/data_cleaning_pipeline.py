from typing import List
from kfp import dsl
from kfp import compiler
from google.cloud import storage
from components.clean_data_component import clean_data_component
from components.query_sql_server_component import query_sql_server_component
from components.write_cleaned_request_component import write_cleaned_request_component



@dsl.pipeline
def data_cleaning_pipeline():
    sql_query_path = 'pipeline/sql/get_updated_core_requests.sql'
    with open(sql_query_path, 'r') as file:
        sql_query = file.read()

    query_results = query_sql_server_component(query=sql_query)
    id_list = query_results.output
    cleaned_core_requests = clean_data_component(id_list=id_list)
    staging_table = "core_request"
    pipeline_id = dsl.PIPELINE_JOB_NAME_PLACEHOLDER
    upload_step = write_cleaned_request_component(cleaned_requests=cleaned_core_requests.outputs["df_output"], table_name=staging_table, pipeline_id=pipeline_id)

compiler.Compiler().compile(
    pipeline_func=data_cleaning_pipeline,
    package_path='data_cleaning_pipeline.yaml')
