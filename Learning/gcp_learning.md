Google Cloud Platform
=====

To create projects, use this https://console.cloud.google.com/. Free credit of 271 euros for a trial period of 91 days as of 8 May 2023.  

To interact with GCP system, then we need Google Cloud SDK. Install it using brew.

        brew install --cask google-cloud-sdk

Next step is to set the authentication key for the SDK.

We can create a service user and create key for the user and download it to local system. Then set the environment variable as

        export GOOGLE_APPLICATION_CREDENTIALS="/path/to/googlecloud/key.json"

To authenticate the user with above credentials, we need to run SDK command as

        gcloud auth application-default login

This will enable OAuth authentication, make google cloud SSO login.


We are planning to create:

1. Google Cloud Storage - Like S3 - A data lake
2. BigQuery - Data Warehouse

Add required permission for the service account created for (Google cloud storage and BigQuery):
    Service User should:
        Create bucket
        Create objects
                Respective roles as of - Storage Admin and Storage Object Admin
        Interact with BigQuery
                Respective role is - BigQuery Admin

GCP CLI interact with GCP using the API. So, we need to OAuth the APIs in order for us to allow the right permission holding service user to access the actual services.
    APIs:
      IAM -  https://console.cloud.google.com/marketplace/details/google/iam.googleapis.com?project=<project-unique-id>
      IAM Credentials - https://console.cloud.google.com/marketplace/details/google/iamcredentials.googleapis.com?project=<project-unique-id>

    API Documentation:
        https://cloud.google.com/iam/docs/reference/credentials/rest - IAM Credentials