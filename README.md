# Data Clean Pipeline

The **Data Clean Pipeline** is a demonstration of a [Vertex AI Kubeflow Pipeline](https://cloud.google.com/vertex-ai/docs/pipelines) with the intent to showcase a generic data cleaning process. This pipeline leverages the [Kubeflow Pipelines SDK](https://www.kubeflow.org/docs/pipelines/sdk/sdk-overview/) to automate the cleaning of data from a source, perform necessary transformations, and store the processed data.

## Overview
The purpose of this Data Clean Pipeline is to automatically clean and transform data from a specified source. The cleaning process involves identifying outliers, addressing specific data issues, and ensuring that the data meets certain standards.

### Components
1. **query_data_source_component:** This component connects to the designated data source and retrieves data suitable for automated cleaning. The criteria for selection depend on the specific requirements of the data cleaning process.
2. **clean_data_component:** This component iterates through the data, applies cleaning transformations, and returns the resulting dataframes.
3. **write_cleaned_data_component:** The cleaned and transformed data is then loaded into the destination table or storage.

### Component Images
Each component in the pipeline has an associated Docker image used to instantiate a container for component execution at runtime. These images include all necessary libraries and dependencies required for the component tasks. Images are built and deployed to a Google Cloud Artifact Registry, accessible by Vertex AI each time a pipeline run is initiated. The registry must be a Docker-specific registry.

### Kubeflow Pipeline Template
The pipeline template is a YAML file compiled from the Python source code in the `pipeline/data_cleaning_pipeline.py`. This file defines the pipeline, specifying the flow of data from one component to another. The template is compiled and deployed to a Kubeflow-specific Artifact Registry in Google Cloud. This deployment is part of the CI/CD process, ensuring that the latest version of the template is available.

#### Pipeline Metadata
An environment variable called `PIPELINE_JOB_NAME_PLACEHOLDER` is accessible in Kubeflow pipelines running in Vertex AI. It contains the pipeline run name, captured by the pipeline template at runtime. This value is written to a metadata column in the destination data storage, allowing tracing of pipeline runs for each row of cleaned data.

### CI/CD and Deployment
The CI/CD process involves the following stages:
1. **Build and Push Docker Images:** The images are built and pushed by the `build_images` stage of the CI/CD job. This stage is manually initiated when image updates need to be deployed.
2. **Compile and Upload Pipeline Template:** The pipeline template is compiled and uploaded to the Kubeflow Artifact Registry as part of the `compile_and_upload_pipeline_template` stage. This stage is run automatically whenever code changes are made to the repository.

### Vertex AI Scheduler
The pipeline can be scheduled to run at specified intervals using Vertex AI Scheduler. The schedule is defined in the `create_pipeline_schedule.py` file and deployed as part of the `create_pipeline_schedule` stage of the CI/CD job. The deployment ensures that the latest version of the pipeline template and schedule is used, preventing multiple instances of the pipeline from running concurrently.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/emainwaring/data-cleaning-pipeline/
   cd data-cleaning-pipeline
