from google.oauth2 import service_account
from googleapiclient.discovery import build
import requests
import json
import pandas as pd
from google.cloud import bigquery

########### SET YOUR PARAMETERS HERE ####################################
PROPERTIES = ["https://www.google.com","https://www.apple.com"]
BQ_DATASET_NAME = 'test_dataset'
BQ_TABLE_NAME = 'test_table'
SERVICE_ACCOUNT_FILE = 'my_key.json'
################ END OF PARAMETERS ######################################

SCOPES = ['https://www.googleapis.com/auth/webmasters']
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build(
    'webmasters',
    'v3',
    credentials=credentials
)

def get_sc_df(site_url,start_date,end_date,start_row):
    """Grab Search Console data for the specific property and send it to BigQuery."""

    request = {
      'startDate': start_date,
      'endDate': end_date,
      'dimensions': ['query','device', 'page', 'date'], # uneditable to enforce a nice clean dataframe at the end!
      'rowLimit': 25000,
      'startRow': start_row
       }

    response = service.searchanalytics().query(siteUrl=site_url, body=request).execute()

    if len(response) > 1:

        x = response['rows']

        df = pd.DataFrame.from_dict(x)
        
        # split the keys list into columns
        df[['query','device', 'page', 'date']] = pd.DataFrame(df['keys'].values.tolist(), index= df.index)
        
        # Drop the key columns
        result = df.drop(['keys'],axis=1)

        # Add a website identifier
        result['website'] = site_url

        # establish a BigQuery client
        client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_FILE)
        dataset_id = BQ_DATASET_NAME
        table_name = BQ_TABLE_NAME
        # create a job config
        job_config = bigquery.LoadJobConfig()
        # Set the destination table
        table_ref = client.dataset(dataset_id).table(table_name)
        job_config.destination = table_ref
        job_config.write_disposition = 'WRITE_APPEND'

        load_job = client.load_table_from_dataframe(result, table_ref, job_config=job_config)
        load_job.result()

        return result
    else:
        print("There are no more results to return.")

# Loop through all defined properties, for up to 100,000 rows of data in each
for p in PROPERTIES:
    for x in range(0,100000,25000):
        y = get_sc_df(p,"2020-01-01","2020-01-01",x)
        if len(y) < 25000:
            break
        else:
            continue
