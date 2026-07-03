from fastapi import FastAPI

app = FastAPI(title="Enterprise AI Operations Assistant")


@app.get("/health")
def health():
    return {"status": "healthy"}
