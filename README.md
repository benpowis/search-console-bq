# Search Console BQ
### Getting data from Google Search Console into BigQuery with some readable Python code
In this example code we build a finction that download data from Google Search Console and stores it in BigQuery. We can look through this function to grab lots of data for multiple properties.

`search_console_bq.py` contains working code with examples of looping over multiple properties, one should update the variables at the top before using.

`Search console BQ 2020.ipynb` is a Jupyter notebook containing all the code, a good starting point if you want to make any changes or run through the process interactively.

Required technical steps:

- Create a Google Cloud project.
- Activate the Google Search Console API on your GCP project.
- Create a service account user, with access to write to BigQuery.
- Add this service account user to each Search Console property that you want to download data from.
- Edit the search_console_bq.py file and set the parameters at the top of the code, populating them with your values.
- The code is designed to load all data to a single BigQuery table, appending each time. This table does not need to exist before the first run.

Read more details on this code and my approach on this Medium post:
https://medium.com/@singularbean/revisiting-google-search-console-data-into-google-bigquery-708a19e2f746
