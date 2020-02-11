# Search Console BQ
### Getting data from Google Search Console into BigQuery with some readable Python code
In this example code we build a finction that download data from Google Search Console and stores it in BigQuery. We can look through this function to grab lots of data for multiple properties.

Required technical steps:

- Create a Google Cloud project.
- Activate the Google Search Console API on your GCP project.
- Create a service account user, with access to write to BigQuery.
- Add this service account user to each Search Console property that you want to download data from.
- Edit the search_console_bq.py file and set the parameters at the top of the code, populating them with your values.
- The code is designed to load all data to a single BigQuery table, appending each time. This table does not need to exist before the first run.

Read more details on this code and my approach on this Medium post:
https://medium.com/@singularbean/revisiting-google-search-console-data-into-google-bigquery-708a19e2f746
