# Discover the world, your way! 

- This application allows you to create a personalized plan for travelling solo. Created for womxn by womxn. 
- This project aims to combat United Nation's Sustainabilty goals 
`5.2 - Eliminate all forms of violence against all women and girls in the public and private spheres, including trafficking and sexual and other types of exploitation.`
`5.B - Enhance the use of enabling technology, in particular information and communications technology, to promote the empowerment of women.`



## Overview

This app demonstrates the power of
- Gemini's Generative Model `gemini-1.5-pro`
- Streamlit for UI
- Cloud Run for deploying

## Prerequisites

- A Google Cloud project with billing enabled
- APIs for Vertex AI, and Cloud Run enabled

## To run the app on your local machine: 
- Authenticate your local machine with your project name
`gcloud config set project your-project-id`
- Run `bash setup.sh`

This script will:

- Connect to the Vertex AI API
- Install Python and packages
- Start the app

## Deploy the app to Cloud Run

When deploying this app to Cloud Run, a best practice is to [create a service
account](https://cloud.google.com/iam/docs/service-accounts-create) to attach
the following roles to, which are the permissions required for the app to read
data from BigQuery, run BigQuery jobs, and use resources in Vertex AI:

- [Vertex AI User](https://cloud.google.com/vertex-ai/docs/general/access-control#aiplatform.user) (`roles/aiplatform.user`)


```shell
gcloud run deploy she-builds-with-ai-2024 --allow-unauthenticated --region us-central1 --service-account SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com --source .
```
