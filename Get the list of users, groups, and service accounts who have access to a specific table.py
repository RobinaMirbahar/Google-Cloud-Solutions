from google.cloud import bigquery

# Initialize a BigQuery client
client = bigquery.Client()

# Get a reference to the table you want to set access controls for
table_ref = client.dataset('my_dataset').table('my_table')
table = client.get_table(table_ref)

# Set access controls for the table
policy = bigquery.IAMPolicy()
policy.viewers.add('user:viewer@example.com')
policy.owners.add('user:owner@example.com')
table.iam_policy = policy
client.update_table(table, ['iam_policy'])



The IAMPolicy class was added in version 2.0.0 of the google-cloud-bigquery library. If you're using version 3.7.0 of the library, you should be able to use the bigquery.IAMPolicy class to set table access controls.

Here's an updated example that should work with version 3.7.0

from google.cloud import bigquery

# Initialize a BigQuery client
client = bigquery.Client()

# Get a reference to the table you want to set access controls for
table_ref = client.dataset('my_dataset').table('my_table')
table = client.get_table(table_ref)

# Set access controls for the table
policy = bigquery.IAMPolicy()
policy.viewers.add('user:viewer@example.com')
policy.owners.add('user:owner@example.com')
table._properties['access']['rows'] = policy
client.update_table(table, ['access'])
