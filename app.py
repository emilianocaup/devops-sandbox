from fastapi import FastAPI

app = FastAPI(title="DevOps Sandbox")


@app.get("/")
def root():
    return {"message": "DevOps Sandbox en marcha"}


@app.get("/health")
def health():
    return {"status": "ok"}