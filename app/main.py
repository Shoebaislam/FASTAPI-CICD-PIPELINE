from fastapi import FastAPI

app = FastAPI(title="CI/CD Pipeline Demo")


@app.get("/")
def root():
    return {"message": "CI/CD pipeline is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}