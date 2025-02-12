from fastapi import FastAPI
from core.api import api

app = FastAPI()
app.mount("/api", api)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
