from your_module import get_raw_data
from your_transformation_module import clean_data
import pandas as pd

def clean_data(request_id):
    df = get_raw_data(request_id)
    archive_df = clean_data(df)
    return archive_df
