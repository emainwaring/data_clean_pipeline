import pyodbc

def test_sql_connection():
    #sql_connection_string ="DRIVER={ODBC Driver 17 for SQL Server};SERVER=sqlwarehouse1.amyris.local;DATABASE=dataout;UID=dataout_reader;PWD=dataout_reader"
    sql_connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=sqlwarehouse1-stage.amyris.local;DATABASE=dataout;UID=svc_vertex_ai_hts_core_clean_stg;PWD=@myris5885!!"
    sql_query = """
        SELECT * from furnace.ADL_manufacturing_data_Ferm amdf 
    """
    sql_write_query= """INSERT INTO furnace.hts_cleaned_core_request (well_id, layer_id, upstream_process, is_outlier, plate_effect, row_col_effect, adjusted_assay_value)
VALUES
    (1, 101, 'Process A', 0, 0.1, 0.2, 99),
    (2, 102, 'Process B', 1, 0.2, 0.3, 88),
    (3, 103, 'Process A', 0, 0.3, 0.4, 77),
    (4, 104, 'Process C', 0, 0.4, 0.5, 66),
    (5, 105, 'Process B', 1, 0.5, 0.6, 55);
"""
    try:
        connection = pyodbc.connect(sql_connection_string)
        cursor = connection.cursor()
        cursor.execute(sql_write_query)
        connection.commit()
        #rows = cursor.fetchall()
        #for row in rows:
        #    print(row)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_sql_connection()
