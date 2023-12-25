from google.cloud import aiplatform
from google.oauth2 import service_account
import os

def create_pipeline_schedule():
    kfp_registry_url = os.environ.get('KFP_REGISTRY_URL')
    schedule_display_name = os.environ.get('SCHEDULE_DISPLAY_NAME', "data-cleaning-pipeline")
    if not kfp_registry_url:
        raise ValueError("KFP_REGISTRY_URL environment variable is not set.")
    template_path = f"{kfp_registry_url}/hts-core-request-cleaning-pipeline/latest"
    credentials = service_account.Credentials.from_service_account_file(
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'], 
        scopes=['https://www.googleapis.com/auth/cloud-platform']
    )
    previous_schedules = aiplatform.PipelineJobSchedule.list(project="your-project", location="us-west1", filter=f'display_name="{schedule_display_name}"', credentials=credentials)
    print(f"Found {len(previous_schedules)} previous schedules.")
    for schedule in previous_schedules:
        print(f"Deleting schedule with name: {schedule.display_name}")
        schedule.delete(sync=True)

    pipeline_job = aiplatform.PipelineJob(
        template_path=template_path,
        display_name="data-cleaning-pipeline",
        credentials=credentials,
        location="us-west1",
    )

    pipeline_job_schedule = aiplatform.PipelineJobSchedule(
        pipeline_job=pipeline_job,
        display_name=schedule_display_name
    )

    pipeline_job_schedule.create(
        cron="1 0 * * *",
        max_concurrent_run_count=1,
        max_run_count=1000,
    )

if __name__ == "__main__":
    create_pipeline_schedule()
