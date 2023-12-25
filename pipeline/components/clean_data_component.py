from kfp import dsl
from typing import List
from kfp.dsl import Input, Output, Dataset


@dsl.component(
    base_image='us-west1-docker.pkg.dev/your-project/ptp-pipeline-images/clean_data_component:latest')
def clean_hts_core_request_component(id_list: List[int],  df_output: Output[Dataset]):
    from hts_request import clean_hts_request
    import pandas as pd
    cleaned_requests = []
    cleaned_requests_df = pd.DataFrame()
    for id in id_list:
        cleaned_request = clean_hts_request(id)
        if cleaned_request is not None:
            cleaned_requests.append(cleaned_request)
    if cleaned_requests != []:
        cleaned_requests_df = pd.concat(cleaned_requests)
    cleaned_requests_df.to_csv(df_output.path, header=True,  index=False)


