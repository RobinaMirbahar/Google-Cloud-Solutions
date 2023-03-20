from google.cloud import bigquery
from google.cloud.iam import Policy

# Instantiate a client
client = bigquery.Client()

# Get the IAM policy for a dataset
dataset = client.get_dataset('my_project.my_dataset')
policy = client.get_iam_policy(dataset.reference)

# Add a new member to the policy
policy.bindings.append(
    Policy.Binding(
        'roles/bigquery.dataViewer',
        ['user:jane@example.com']
    )
)

# Update the IAM policy for the dataset
client.set_iam_policy(dataset.reference, policy)





