#!/usr/bin/env bash

# Enable Vertex AI and BigQuery
gcloud services enable aiplatform.googleapis.com
gcloud services enable bigquery.googleapis.com
gcloud services enable bigquerydatatransfer.googleapis.com

# Copy dataset
# bq mk --force=true --dataset she_builds_with_ai_2024
# bq mk \
#   --transfer_config \
#   --data_source=cross_region_copy \
#   --target_dataset=she_builds_with_ai_2024 \
#   --display_name='Personalized solo travel guide - She Builds with AI 2024' \
#   --schedule_end_time="$(date -u -d '5 mins' +%Y-%m-%dT%H:%M:%SZ)" \
#   --params='{
#       "source_project_id":"eax-apps",
#       "source_dataset_id":"she_builds_with_ai_2024",
#       "overwrite_destination_table":"true"
#       }'

# Install Python
export PYTHON_PREFIX=~/miniforge
curl -Lo ~/miniforge.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash ~/miniforge.sh -fbp ${PYTHON_PREFIX}
rm -rf ~/miniforge.sh

# Install packages
${PYTHON_PREFIX}/bin/pip install -r requirements.txt

# Run app
${PYTHON_PREFIX}/bin/streamlit run form.py --server.enableCORS=false --server.enableXsrfProtection=false --server.port 8080
