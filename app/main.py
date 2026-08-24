import os

from fastapi import FastAPI


app = FastAPI(
    title="DevOps Platform Lab API",
    description="API used to demonstrate an end-to-end DevOps platform.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "application": "devops-platform-lab",
        "environment": os.getenv("APP_ENV", "local"),
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.get("/version")
def version():
    return {
        "version": os.getenv("APP_VERSION", "1.0.0"),
    }


@app.get("/feature")
def feature():
    feature_enabled = os.getenv("FEATURE_FLAG", "false").lower() == "true"

    return {
        "feature_enabled": feature_enabled,
    }
