from fastapi import FastAPI, Form
import requests
from fastapi.responses import HTMLResponse
from typing import Annotated

app = FastAPI()


# Function to trigger Jenkins job
def trigger_jenkins_job(bucket_name):
    jenkins_url = (
        "http://localhost:8080"  # Assuming Jenkins is running locally on port 8080
    )
    job_name = ""
    user_name = ""
    api_token = ""

    url = f"{jenkins_url}/job/{job_name}/buildWithParameters"
    params = {"token": api_token, "bucket_name": bucket_name}

    response = requests.post(url, params=params, auth=(user_name, api_token))

    if response.status_code == 201:
        print(f"Jenkins job {job_name} triggered successfully.")
    else:
        print(
            f"Failed to trigger Jenkins job {job_name}. HTTP Code: {response.status_code}"
        )


@app.post("/create_bucket", response_class=HTMLResponse)
async def create_bucket(bucket_name: Annotated[str, Form()]):
    print(f"Bucket Name: {bucket_name}")
    response = f"Bucket Name: {bucket_name}<br>"
    trigger_jenkins_job(bucket_name)
    return response
